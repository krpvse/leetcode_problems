from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

from .html_text import HtmlToText
from .models import KNOWN_LANGUAGES, Language, Problem

STATEMENT_UNAVAILABLE = "Problem statement is not available."


class SolutionFormatter:
    """Builds a solution file: the problem statement as a comment header followed by the code."""

    @staticmethod
    def format(problem: Problem, language: Language, statement_html: Optional[str], code: str) -> str:
        statement = HtmlToText.convert(statement_html) if statement_html else STATEMENT_UNAVAILABLE
        header = [
            f"{problem.frontend_id}. {problem.title}",
            f"Difficulty: {problem.difficulty}",
            f"Topics: {', '.join(problem.tags) or '-'}",
            problem.url,
            "",
            *statement.splitlines(),
        ]
        comment = "\n".join(language.comment(line) for line in header)
        return f"{comment}\n\n{code.strip()}\n"


class SolutionStorage:
    """Solution files in the problems directory: `<0001>-<slug>[-<suffix>].<ext>`, one per problem."""

    def __init__(self, problems_dir: Path):
        self._problems_dir = problems_dir

    def path(self, problem: Problem, language: Language) -> Path:
        return self._problems_dir / self._file_name(problem, language)

    def is_synced(self, problem: Problem) -> bool:
        return any(self.path(problem, language).exists() for language in KNOWN_LANGUAGES)

    def write(self, problem: Problem, language: Language, content: str) -> None:
        """Writes atomically, so an interrupted run never leaves a truncated file that counts as synced."""
        self._problems_dir.mkdir(parents=True, exist_ok=True)
        path = self.path(problem, language)
        temporary_path = path.with_name(path.name + ".tmp")
        temporary_path.write_bytes(content.encode("utf-8"))
        os.replace(temporary_path, path)

    @staticmethod
    def _file_name(problem: Problem, language: Language) -> str:
        number = problem.frontend_id.zfill(4) if problem.is_numbered else problem.frontend_id
        suffix = f"-{language.file_suffix}" if language.file_suffix else ""
        return f"{number}-{problem.slug}{suffix}.{language.extension}"
