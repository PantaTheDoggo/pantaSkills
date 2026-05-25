"""
Extrai capítulos de arquivos EPUB para texto puro.

Uso:
  python epub_chapter_extractor.py livro.epub --list
  python epub_chapter_extractor.py livro.epub --chapter 3
  python epub_chapter_extractor.py livro.epub --chapter 3 --output cap3.txt

Dependências: pip install ebooklib beautifulsoup4
"""

import argparse
import re
import sys
import warnings
from pathlib import Path


def _check_deps() -> None:
    missing = []
    try:
        import ebooklib  # noqa: F401
    except ImportError:
        missing.append("ebooklib")
    try:
        import bs4  # noqa: F401
    except ImportError:
        missing.append("beautifulsoup4")
    if missing:
        print(f"Dependências ausentes: {', '.join(missing)}", file=sys.stderr)
        print(f"Instale com: pip install {' '.join(missing)}", file=sys.stderr)
        sys.exit(1)


def html_to_text(html_bytes: bytes) -> str:
    from bs4 import BeautifulSoup, NavigableString

    html = html_bytes.decode("utf-8", errors="replace")
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "head", "nav"]):
        tag.decompose()

    parts: list[str] = []

    def walk(node) -> None:
        if isinstance(node, NavigableString):
            text = str(node)
            if text.strip():
                parts.append(text)
            return
        name = getattr(node, "name", None)
        if not name:
            return
        if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            heading = node.get_text(separator=" ", strip=True)
            if heading:
                parts.append(f"\n{'#' * int(name[1])} {heading}\n")
        elif name == "p":
            text = node.get_text(separator=" ", strip=True)
            if text:
                parts.append(f"\n{text}\n")
        elif name == "pre":
            code = node.get_text()
            if code.strip():
                parts.append(f"\n```\n{code.rstrip()}\n```\n")
        elif name in ("ul", "ol"):
            parts.append("")
            for li in node.find_all("li", recursive=False):
                parts.append(f"- {li.get_text(separator=' ', strip=True)}")
            parts.append("")
        elif name == "br":
            parts.append("\n")
        else:
            for child in node.children:
                walk(child)

    walk(soup.find("body") or soup)
    text = "".join(parts)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def _read_epub(epub_path: Path):
    from ebooklib import epub
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return epub.read_epub(str(epub_path))


def _build_chapters(book) -> list[dict]:
    """Flat list of TOC entries: {index, title, href, depth}."""
    chapters: list[dict] = []

    def flatten(items, depth: int = 0) -> None:
        for item in items:
            if isinstance(item, tuple):
                section, children = item
                title = (getattr(section, "title", "") or "").strip()
                href = (getattr(section, "href", "") or "").split("#")[0]
                if title:
                    chapters.append({"index": len(chapters) + 1, "title": title, "href": href, "depth": depth})
                flatten(children, depth + 1)
            else:
                title = (getattr(item, "title", "") or "").strip()
                href = (getattr(item, "href", "") or "").split("#")[0]
                if title:
                    chapters.append({"index": len(chapters) + 1, "title": title, "href": href, "depth": depth})

    flatten(book.toc)

    if not chapters:
        import ebooklib
        for i, (iid, _) in enumerate(book.spine):
            item = book.get_item_with_id(iid)
            if item and item.media_type == "application/xhtml+xml":
                chapters.append({
                    "index": i + 1,
                    "title": Path(item.get_name()).stem,
                    "href": item.get_name(),
                    "depth": 0,
                })

    return chapters


def _find_item(book, href: str):
    import ebooklib
    item = book.get_item_with_href(href)
    if item:
        return item
    for it in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        name = it.get_name()
        if name.endswith(href) or href.endswith(name):
            return it
    return None


def cmd_list(epub_path: Path) -> None:
    book = _read_epub(epub_path)
    chapters = _build_chapters(book)
    print(f"EPUB : {epub_path.name}")
    print(f"{'No':>4}  Titulo")
    print("-" * 60)
    for ch in chapters:
        indent = "  " * ch["depth"]
        print(f"{ch['index']:>4}  {indent}{ch['title']}")
    print(f"\nTotal: {len(chapters)} entradas no indice")


def cmd_extract(epub_path: Path, chapter_num: int, output_path: "Path | None") -> None:
    book = _read_epub(epub_path)
    chapters = _build_chapters(book)

    if not 1 <= chapter_num <= len(chapters):
        print(f"Capitulo {chapter_num} fora do intervalo 1-{len(chapters)}. Use --list para ver os disponiveis.", file=sys.stderr)
        sys.exit(1)

    ch = chapters[chapter_num - 1]
    item = _find_item(book, ch["href"])

    if item is None:
        print(f"Nao foi possivel localizar o arquivo para '{ch['title']}' (href={ch['href']})", file=sys.stderr)
        sys.exit(1)

    body = html_to_text(item.get_content())
    full_text = f"# Capitulo {chapter_num}: {ch['title']}\n\n{body}"

    if output_path:
        output_path.write_text(full_text, encoding="utf-8")
        chars = len(full_text)
        lines = full_text.count("\n")
        print(f"OK '{ch['title']}' -> {output_path}  ({chars:,} chars, {lines:,} linhas)")
    else:
        print(full_text)


def main() -> None:
    parser = argparse.ArgumentParser(description="Extrai capitulos de EPUB para texto puro")
    parser.add_argument("epub", help="Arquivo .epub")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--list", "-l", action="store_true", help="Listar capitulos")
    group.add_argument("--chapter", "-c", type=int, metavar="N", help="Numero do capitulo a extrair")
    parser.add_argument("--output", "-o", metavar="ARQUIVO", help="Arquivo de saida (omitir = stdout)")
    args = parser.parse_args()

    _check_deps()

    epub_path = Path(args.epub)
    if not epub_path.exists():
        print(f"Arquivo nao encontrado: {epub_path}", file=sys.stderr)
        sys.exit(1)

    if args.list:
        cmd_list(epub_path)
    else:
        output = Path(args.output) if args.output else None
        cmd_extract(epub_path, args.chapter, output)


if __name__ == "__main__":
    main()
