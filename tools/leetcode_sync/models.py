from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

LEETCODE_URL = "https://leetcode.com"


@dataclass(frozen=True)
class Problem:
    frontend_id: str
    title: str
    slug: str
    difficulty: str
    tags: List[str]

    @property
    def is_numbered(self) -> bool:
        return self.frontend_id.isdigit()

    @property
    def url(self) -> str:
        return f"{LEETCODE_URL}/problems/{self.slug}/"


@dataclass(frozen=True)
class AcceptedSubmission:
    submission_id: int
    language: str


@dataclass(frozen=True)
class Language:
    slug: str
    name: str
    extension: str
    comment_prefix: str
    file_suffix: str = ""

    def comment(self, line: str) -> str:
        return f"{self.comment_prefix} {line}" if line else self.comment_prefix


KNOWN_LANGUAGES = [
    Language("python3", "Python3", "py", "#"),
    Language("python", "Python", "py", "#", "python2"),
    Language("pythondata", "Pandas", "py", "#", "pandas"),
    Language("cpp", "C++", "cpp", "//"),
    Language("c", "C", "c", "//"),
    Language("java", "Java", "java", "//"),
    Language("csharp", "C#", "cs", "//"),
    Language("javascript", "JavaScript", "js", "//"),
    Language("typescript", "TypeScript", "ts", "//"),
    Language("golang", "Go", "go", "//"),
    Language("kotlin", "Kotlin", "kt", "//"),
    Language("swift", "Swift", "swift", "//"),
    Language("rust", "Rust", "rs", "//"),
    Language("ruby", "Ruby", "rb", "#"),
    Language("scala", "Scala", "scala", "//"),
    Language("php", "PHP", "php", "//"),
    Language("dart", "Dart", "dart", "//"),
    Language("elixir", "Elixir", "ex", "#"),
    Language("erlang", "Erlang", "erl", "%"),
    Language("racket", "Racket", "rkt", ";"),
    Language("bash", "Bash", "sh", "#"),
    Language("mysql", "MySQL", "sql", "--"),
    Language("postgresql", "PostgreSQL", "sql", "--", "postgresql"),
    Language("mssql", "MS SQL Server", "sql", "--", "mssql"),
    Language("oraclesql", "Oracle", "sql", "--", "oracle"),
]

_LANGUAGES_BY_SLUG = {language.slug: language for language in KNOWN_LANGUAGES}


def language_by_slug(slug: str) -> Optional[Language]:
    return _LANGUAGES_BY_SLUG.get(slug)
