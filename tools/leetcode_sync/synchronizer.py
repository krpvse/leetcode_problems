from __future__ import annotations

import logging

from .client import LeetCodeClient, QueryError
from .models import Problem, language_by_slug
from .storage import SolutionFormatter, SolutionStorage

logger = logging.getLogger(__name__)


class Synchronizer:
    def __init__(self, client: LeetCodeClient, storage: SolutionStorage):
        self._client = client
        self._storage = storage

    def run(self) -> int:
        """Exports problems that have no solution files yet; returns how many were added."""
        username = self._client.ensure_signed_in()
        logger.info("Signed in as %s", username)
        solved = self._client.fetch_solved_problems()
        new_problems = [problem for problem in solved if not self._storage.is_synced(problem)]
        logger.info("Solved: %d, new: %d", len(solved), len(new_problems))

        added = 0
        for position, problem in enumerate(new_problems, start=1):
            logger.info("[%d/%d] %s. %s", position, len(new_problems), problem.frontend_id, problem.title)
            try:
                added += self._sync_problem(problem)
            except QueryError as error:
                logger.warning("Skipping %s: %s", problem.slug, error)
        return added

    def _sync_problem(self, problem: Problem) -> bool:
        submission = self._client.fetch_latest_accepted(problem.slug)
        if submission is None:
            logger.warning("No accepted submissions found for %s", problem.slug)
            return False
        language = language_by_slug(submission.language)
        if language is None:
            logger.warning("Skipping %s: unsupported language %s", problem.slug, submission.language)
            return False

        code = self._client.fetch_submission_code(submission.submission_id)
        statement = self._client.fetch_problem_statement(problem.slug)
        self._storage.write(problem, language, SolutionFormatter.format(problem, language, statement, code))
        return True
