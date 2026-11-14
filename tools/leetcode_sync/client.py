from __future__ import annotations

import random
import time
from typing import List, Optional

import requests

from .models import LEETCODE_URL, AcceptedSubmission, Problem

_USER_STATUS_QUERY = """
query userStatus {
  userStatus { isSignedIn username }
}
"""

_SOLVED_PROBLEMS_QUERY = """
query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList: questionList(categorySlug: $categorySlug, limit: $limit, skip: $skip, filters: $filters) {
    total: totalNum
    questions: data {
      frontendQuestionId: questionFrontendId
      title
      titleSlug
      difficulty
      topicTags { name }
    }
  }
}
"""

_SUBMISSIONS_QUERY = """
query submissionList($offset: Int!, $limit: Int!, $questionSlug: String!, $status: Int) {
  questionSubmissionList(offset: $offset, limit: $limit, questionSlug: $questionSlug, status: $status) {
    submissions { id lang }
  }
}
"""

_SUBMISSION_CODE_QUERY = """
query submissionDetails($submissionId: Int!) {
  submissionDetails(submissionId: $submissionId) { code }
}
"""

_PROBLEM_STATEMENT_QUERY = """
query questionContent($titleSlug: String!) {
  question(titleSlug: $titleSlug) { content }
}
"""


class LeetCodeError(RuntimeError):
    pass


class QueryError(LeetCodeError):
    """A single query failed while the connection and session are fine."""


class LeetCodeClient:
    GRAPHQL_URL = f"{LEETCODE_URL}/graphql/"
    ACCEPTED_STATUS = 10
    PAGE_SIZE = 100
    RETRYABLE_STATUSES = {429, 500, 502, 503, 504}
    REQUEST_DELAY_RANGE = (1.0, 2.0)
    RETRY_BASE_DELAY = 1.0

    def __init__(self, session_cookie: str, max_retries: int = 5):
        self._max_retries = max_retries
        self._last_request_at = 0.0
        self._session = requests.Session()
        self._session.cookies.set("LEETCODE_SESSION", session_cookie, domain=".leetcode.com")
        self._session.headers.update({
            "Content-Type": "application/json",
            "Referer": LEETCODE_URL,
            "Origin": LEETCODE_URL,
            "User-Agent": "Mozilla/5.0 (leetcode-solutions-sync)",
        })

    def ensure_signed_in(self) -> str:
        status = self._query(_USER_STATUS_QUERY, {})["userStatus"]
        if not status["isSignedIn"]:
            raise LeetCodeError("Not signed in: LEETCODE_SESSION is invalid or expired")
        return status["username"]

    def fetch_solved_problems(self) -> List[Problem]:
        problems: List[Problem] = []
        total = None
        while total is None or len(problems) < total:
            variables = {
                "categorySlug": "",
                "skip": len(problems),
                "limit": self.PAGE_SIZE,
                "filters": {"status": "AC"},
            }
            page = self._query(_SOLVED_PROBLEMS_QUERY, variables)["problemsetQuestionList"]
            total = page["total"]
            if not page["questions"]:
                break
            problems.extend(self._to_problem(question) for question in page["questions"])
        return problems

    def fetch_latest_accepted(self, slug: str) -> Optional[AcceptedSubmission]:
        """Returns the newest accepted submission in any language, or None when there is none."""
        variables = {
            "questionSlug": slug,
            "offset": 0,
            "limit": 1,
            "status": self.ACCEPTED_STATUS,
        }
        submissions = self._query(_SUBMISSIONS_QUERY, variables)["questionSubmissionList"]["submissions"]
        return self._to_submission(submissions[0]) if submissions else None

    def fetch_submission_code(self, submission_id: int) -> str:
        details = self._query(_SUBMISSION_CODE_QUERY, {"submissionId": submission_id})["submissionDetails"]
        if details is None:
            raise QueryError(f"Submission {submission_id} is not available")
        return details["code"]

    def fetch_problem_statement(self, slug: str) -> Optional[str]:
        """Returns the statement as HTML, or None when it is hidden (e.g. a premium problem)."""
        question = self._query(_PROBLEM_STATEMENT_QUERY, {"titleSlug": slug})["question"]
        return question["content"] if question else None

    @staticmethod
    def _to_problem(question: dict) -> Problem:
        return Problem(
            frontend_id=question["frontendQuestionId"],
            title=question["title"],
            slug=question["titleSlug"],
            difficulty=question["difficulty"],
            tags=[tag["name"] for tag in question["topicTags"]],
        )

    @staticmethod
    def _to_submission(item: dict) -> AcceptedSubmission:
        return AcceptedSubmission(int(item["id"]), item["lang"])

    def _query(self, query: str, variables: dict) -> dict:
        for attempt in range(1, self._max_retries + 1):
            response = self._post({"query": query, "variables": variables})
            if response is not None and response.status_code not in self.RETRYABLE_STATUSES:
                return self._parse(response)
            if attempt < self._max_retries:
                time.sleep(self.RETRY_BASE_DELAY * 2 ** attempt)
        raise LeetCodeError(f"LeetCode is not responding after {self._max_retries} attempts")

    @staticmethod
    def _parse(response: requests.Response) -> dict:
        if response.status_code in (401, 403):
            raise LeetCodeError("Access denied: refresh LEETCODE_SESSION in .env")
        try:
            payload = response.json()
        except ValueError:
            raise LeetCodeError(f"Unexpected non-JSON response (HTTP {response.status_code})") from None
        if payload.get("errors"):
            raise QueryError(f"GraphQL error: {payload['errors']}")
        if response.status_code >= 400:
            raise LeetCodeError(f"Unexpected HTTP {response.status_code}")
        return payload["data"]

    def _post(self, body: dict) -> Optional[requests.Response]:
        """Returns None on a network failure so the request can be retried."""
        wait = self._last_request_at + random.uniform(*self.REQUEST_DELAY_RANGE) - time.monotonic()
        if wait > 0:
            time.sleep(wait)
        try:
            return self._session.post(self.GRAPHQL_URL, json=body, timeout=30)
        except (requests.ConnectionError, requests.Timeout):
            return None
        finally:
            self._last_request_at = time.monotonic()
