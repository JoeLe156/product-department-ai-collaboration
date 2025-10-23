import os
import glob
import io
import html
import re


BASE_DIR = os.path.dirname(__file__)


def collect_slide_paths(base: str):
    pattern = os.path.join(base, 'slides-*.md')
    paths = sorted(
        glob.glob(pattern),
        key=lambda p: int(os.path.splitext(os.path.basename(p))[0].split('-')[1])
    )
    return paths


def read_utf8(path: str) -> str:
    # Use utf-8-sig to gracefully strip any BOMs present in individual slide files
    with io.open(path, 'r', encoding='utf-8-sig') as f:
        return f.read().strip()


def write_utf8(path: str, content: str):
    with io.open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)


_REF_RE = re.compile(r"^\[([^\]]+)\]:\s+(\S+)")


def extract_link_refs(text: str):
    refs = []
    for line in text.splitlines():
        m = _REF_RE.match(line.strip())
        if m:
            label, url = m.group(1), m.group(2)
            refs.append((label, url))
    # de-duplicate preserving order
    seen = set()
    uniq = []
    for label, url in refs:
        key = (label, url)
        if key in seen:
            continue
        seen.add(key)
        uniq.append((label, url))
    return uniq


def append_sources_footer(text: str) -> str:
    refs = extract_link_refs(text)
    if not refs:
        return text
    links = ' ; '.join(
        f'<a href="{html.escape(url)}" target="_blank" rel="noopener noreferrer">{html.escape(label)}</a>'
        for label, url in refs
    )
    footer = f"\n\n<div class=\"footer\">Sources: {links}</div>\n"
    return text + footer


def build_markdown(slide_paths):
    parts = []
    for p in slide_paths:
        raw = read_utf8(p)
        with_footer = append_sources_footer(raw)
        parts.append(with_footer)
    return "\n\n---\n\n".join(parts) + "\n"


def build_html(markdown_text: str) -> str:
    return (
        "<!doctype html>\n"
        "<html lang=\"en\">\n"
        "  <head>\n"
        "    <meta charset=\"utf-8\" />\n"
        "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n"
        "    <title>Product Management + AI 2025–2030 — Full Deck</title>\n"
        "    <link rel=\"stylesheet\" href=\"https://unpkg.com/reveal.js@4/dist/reveal.css\" />\n"
        "    <link rel=\"stylesheet\" href=\"https://unpkg.com/reveal.js@4/dist/theme/white.css\" id=\"theme\" />\n"
        "    <link rel=\"stylesheet\" href=\"../visual-attributes/theme.css\" />\n"
        "  </head>\n"
        "  <body>\n"
        "    <div class=\"reveal\">\n"
        "      <div class=\"slides\">\n"
        "        <section data-markdown>\n"
        "          <textarea data-template>" + html.escape(markdown_text) + "</textarea>\n"
        "        </section>\n"
        "      </div>\n"
        "    </div>\n"
        "\n"
        "    <script src=\"https://unpkg.com/reveal.js@4/dist/reveal.js\"></script>\n"
        "    <script src=\"https://unpkg.com/reveal.js@4/plugin/markdown/markdown.js\"></script>\n"
        "    <script>\n"
        "      Reveal.initialize({ hash: true, slideNumber: 'c/t', width: 1280, height: 720, plugins: [ RevealMarkdown ] });\n"
        "    </script>\n"
        "  </body>\n"
        "</html>\n"
    )


def main():
    base = BASE_DIR
    slide_paths = collect_slide_paths(base)
    if not slide_paths:
        raise SystemExit("No slide files found in output directory.")

    combined_md = build_markdown(slide_paths)
    deck_md_path = os.path.join(base, 'deck-full.md')
    write_utf8(deck_md_path, combined_md)

    deck_html = build_html(combined_md)
    html_path = os.path.join(base, 'deck-full.html')
    write_utf8(html_path, deck_html)

    print(f"Wrote: {deck_md_path}")
    print(f"Wrote: {html_path}")


if __name__ == '__main__':
    main()
