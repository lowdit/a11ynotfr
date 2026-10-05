#!/usr/bin/env python3
"""Convert a11yNot Jekyll _nots into Hugo content/wcag and content/outils."""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = Path("/tmp/a11yNot.github.io")
# Fichiers servis depuis static/a11ynot/demos/ (comme le blog)
DEMO_URL_PREFIX = "/a11ynot/demos"


def slug_for(basename: str, source: str) -> str:
    if source == "devtools":
        return basename.lower().replace("_", "-")
    return "w3-" + basename.lower()


def transform_body(body: str, gist_id: str, title: str) -> str:
    body = body.replace("{{ page.gistID }}", gist_id)
    body = body.replace("{{ page.title }}", html.escape(title, quote=True))
    body = re.sub(
        r"\{%\s*gist\s+page\.gistID\s*%\}",
        f'<script src="https://gist.github.com/{gist_id}.js"></script>',
        body,
    )

    def iframe_src(m: re.Match[str]) -> str:
        name = m.group(1)
        return f'src="{DEMO_URL_PREFIX}/{name}"'

    body = re.sub(r'src="([^"]+-special\.html)"', iframe_src, body)

    replacements = {
        ">Example Begin<": ">Début de l'exemple<",
        ">Example End<": ">Fin de l'exemple<",
        ">Code for this Example<": ">Code de cet exemple<",
    }
    for old, new in replacements.items():
        body = body.replace(old, new)
    return body.strip() + "\n"


def split_front_matter(raw: str) -> tuple[str, str]:
    if not raw.startswith("---"):
        return "", raw
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return "", raw
    return parts[1], parts[2]


def parse_simple_yaml(fm: str) -> dict:
    data: dict = {}
    current_key: str | None = None
    list_key: str | None = None
    for line in fm.splitlines():
        if not line.strip():
            continue
        if list_key and re.match(r"^-\s+", line):
            data.setdefault(list_key, []).append(re.sub(r"^-\s+", "", line).strip())
            continue
        list_key = None
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        current_key = key
        if val == "":
            list_key = key
            data[key] = []
        else:
            data[key] = val
    return data


def dump_yaml(meta: dict) -> str:
    lines: list[str] = []
    for key, val in meta.items():
        if isinstance(val, list):
            lines.append(f"{key}:")
            for item in val:
                lines.append(f"  - {item}")
        else:
            escaped = str(val).replace('"', '\\"')
            if ":" in str(val) or "&" in str(val) or str(val).startswith("W3"):
                lines.append(f'{key}: "{escaped}"')
            else:
                lines.append(f"{key}: {val}")
    return "\n".join(lines)


def load_tag_names(source: Path) -> dict[str, str]:
    tags_file = source / "_data" / "tags.yml"
    if not tags_file.is_file():
        return {}
    names: dict[str, str] = {}
    slug: str | None = None
    for line in tags_file.read_text(encoding="utf-8").splitlines():
        m = re.match(r"- slug:\s*(\S+)", line)
        if m:
            slug = m.group(1)
            continue
        m = re.match(r"\s+name:\s*(.+)", line)
        if m and slug:
            names[slug] = m.group(1).strip()
    return names


def main() -> int:
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SOURCE
    content_root = REPO_ROOT / "content"
    if not (source / "_nots").is_dir():
        print(f"Missing {source / '_nots'}", file=sys.stderr)
        return 1

    tags_data = load_tag_names(source)

    for sub in ("outils", "wcag"):
        (content_root / sub).mkdir(parents=True, exist_ok=True)

    counts = {"outils": 0, "wcag": 0}
    for path in sorted((source / "_nots").glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        fm_raw, body = split_front_matter(raw)
        meta = parse_simple_yaml(fm_raw)
        basename = path.stem
        source_kind = meta.get("source") or "w3"
        section = "outils" if source_kind == "devtools" else "wcag"
        slug = slug_for(basename, source_kind)
        title = html.unescape(str(meta.get("title") or basename))
        gist_id = str(meta.get("gistID") or "")

        tags = meta.get("tags") or []
        if isinstance(tags, str):
            tags = [tags]

        out_meta = {
            "title": title,
            "a11ynot_id": basename,
            "category": section,
            "gistID": gist_id,
            "original_url": f"http://a11ynot.com/nots/{basename}.html",
            "type": "a11ynot",
            "layout": "a11ynot",
            "tags": tags,
        }
        if meta.get("css") == "custom":
            out_meta["custom_css"] = f"{basename}.css"

        tag_labels = [tags_data.get(t, t) for t in tags]
        if tag_labels:
            out_meta["tag_labels"] = tag_labels

        body_out = transform_body(body, gist_id, title)
        front = dump_yaml(out_meta)
        out_path = content_root / section / f"{slug}.md"
        out_path.write_text(f"---\n{front}\n---\n\n{body_out}", encoding="utf-8")
        counts[section] += 1

    print(f"Wrote {counts['outils']} outils + {counts['wcag']} wcag → {content_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
