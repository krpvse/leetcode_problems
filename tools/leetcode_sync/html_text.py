from __future__ import annotations

import textwrap
from html.parser import HTMLParser
from typing import List


class HtmlToText(HTMLParser):
    """Converts LeetCode problem statement HTML into wrapped plain text."""

    WIDTH = 100
    BLOCK_TAGS = {"p", "div", "pre", "ul", "ol", "li", "br", "h1", "h2", "h3", "h4", "table", "tr"}
    LIST_TAGS = {"ul", "ol"}
    CELL_TAGS = {"td", "th"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self._lines: List[str] = []
        self._fragments: List[str] = []
        self._in_pre = False
        self._list_depth = 0
        self._open_list_items = 0

    @classmethod
    def convert(cls, html: str) -> str:
        parser = cls()
        parser.feed(html)
        parser.close()
        parser._flush()
        return parser._text()

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag in self.BLOCK_TAGS:
            self._flush()
        if tag == "pre":
            self._in_pre = True
        elif tag in self.LIST_TAGS:
            self._list_depth += 1
        elif tag == "li":
            self._open_list_items += 1
        elif tag in self.CELL_TAGS and "".join(self._fragments).strip():
            self._fragments.append(" | ")
        elif tag == "sup":
            self._fragments.append("^")
        elif tag == "sub":
            self._fragments.append("_")
        elif tag == "img":
            self._fragments.append(f"[image: {dict(attrs).get('src', '')}]")

    def handle_endtag(self, tag: str) -> None:
        if tag in self.BLOCK_TAGS:
            self._flush()
        if tag == "pre":
            self._in_pre = False
            self._lines.append("")
        elif tag == "li":
            self._open_list_items = max(self._open_list_items - 1, 0)
        elif tag in self.LIST_TAGS:
            self._list_depth = max(self._list_depth - 1, 0)
            if not self._list_depth:
                self._lines.append("")

    def handle_data(self, data: str) -> None:
        self._fragments.append(data.replace("\xa0", " "))

    def _flush(self) -> None:
        text = "".join(self._fragments)
        self._fragments = []
        if self._in_pre:
            self._lines.extend(line.rstrip() for line in text.strip("\n").split("\n") if text.strip())
            return
        text = " ".join(text.split())
        if not text:
            return
        if self._open_list_items:
            indent = "  " * max(self._list_depth - 1, 0)
            self._lines.extend(
                textwrap.wrap(text, self.WIDTH, initial_indent=f"{indent}- ", subsequent_indent=f"{indent}  ")
            )
        else:
            self._lines.extend(textwrap.wrap(text, self.WIDTH))
            self._lines.append("")

    def _text(self) -> str:
        result: List[str] = []
        for line in self._lines:
            if line or (result and result[-1]):
                result.append(line)
        return "\n".join(result).strip("\n")
