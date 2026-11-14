"""Exports accepted LeetCode solutions into this repository."""
from __future__ import annotations

import logging
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

from leetcode_sync import LeetCodeClient, LeetCodeError, SolutionStorage, Synchronizer

ROOT = Path(__file__).resolve().parent.parent


def load_session_cookie() -> str:
    load_dotenv(ROOT / ".env")
    session_cookie = os.getenv("LEETCODE_SESSION")
    if not session_cookie:
        sys.exit("Set LEETCODE_SESSION in .env (see .env.example)")
    return session_cookie


def build_synchronizer(session_cookie: str) -> Synchronizer:
    return Synchronizer(client=LeetCodeClient(session_cookie), storage=SolutionStorage(ROOT / "problems"))


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    session_cookie = load_session_cookie()
    try:
        added = build_synchronizer(session_cookie).run()
    except LeetCodeError as error:
        sys.exit(f"Error: {error}")
    logging.info("Done: %d new problems", added)


if __name__ == "__main__":
    main()
