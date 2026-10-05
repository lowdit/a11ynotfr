#!/usr/bin/env python3
"""Génère data/a11ynot/outils_meta.yaml et synchronise les titres FR des pages outils."""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
OUTILS_DIR = REPO / "content" / "outils"
LABELS_PATH = REPO / "data" / "a11ynot" / "outils_labels_fr.yaml"
OUT = REPO / "data" / "a11ynot" / "outils_meta.yaml"
WCAG_SC = REPO / "data" / "a11ynot" / "wcag_meta.yaml"


def yq(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def load_sc_names() -> dict[str, str]:
    names: dict[str, str] = {}
    if not WCAG_SC.exists():
        return names
    in_sc = False
    for line in WCAG_SC.read_text(encoding="utf-8").splitlines():
        if line.strip() == "sc_names:":
            in_sc = True
            continue
        if in_sc and line.strip().startswith("by_criterion:"):
            break
        if in_sc:
            m = re.match(r'\s+"(\d+\.\d+\.\d+)":\s*"(.*)"\s*$', line)
            if m:
                names[m.group(1)] = m.group(2)
    return names


def parse_labels_file() -> tuple[dict[str, dict], dict[str, dict]]:
    themes: dict[str, dict] = {}
    labels: dict[str, dict] = {}
    if not LABELS_PATH.exists():
        return themes, labels
    section: str | None = None
    current_id: str | None = None
    for line in LABELS_PATH.read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("#") or not line.strip():
            continue
        if line.strip() == "themes:":
            section = "themes"
            continue
        if line.strip() == "labels:":
            section = "labels"
            current_id = None
            continue
        if section == "themes":
            m = re.match(r"^\s+(\w+):\s*$", line)
            if m:
                current_id = m.group(1)
                themes[current_id] = {}
                continue
            if current_id and "name_fr:" in line:
                themes[current_id]["name_fr"] = line.split("name_fr:", 1)[1].strip().strip('"')
            if current_id and "order:" in line:
                themes[current_id]["order"] = int(line.split("order:", 1)[1].strip())
        if section == "labels":
            m = re.match(r"^\s+([A-Za-z0-9_]+):\s*$", line)
            if m:
                current_id = m.group(1)
                labels[current_id] = {}
                continue
            if not current_id:
                continue
            if "theme:" in line:
                labels[current_id]["theme"] = line.split("theme:", 1)[1].strip()
            elif "title_fr:" in line:
                labels[current_id]["title_fr"] = line.split("title_fr:", 1)[1].strip().strip('"')
            elif "summary_fr:" in line:
                labels[current_id]["summary_fr"] = line.split("summary_fr:", 1)[1].strip().strip('"')
            elif line.strip().startswith("wcag:"):
                labels[current_id]["wcag"] = []
            elif "wcag" in labels[current_id] and re.match(r'\s+-\s+"(\d+\.\d+\.\d+)"', line):
                labels[current_id]["wcag"].append(re.match(r'\s+-\s+"(\d+\.\d+\.\d+)"', line).group(1))
    return themes, labels


def parse_front_matter(path: Path) -> tuple[dict[str, str], str]:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        return {}, raw
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return {}, raw
    meta: dict[str, str] = {}
    for line in parts[1].splitlines():
        m = re.match(r'^([\w_]+):\s*"(.*)"\s*$', line.strip())
        if m:
            meta[m.group(1)] = m.group(2).replace('\\"', '"')
        else:
            m = re.match(r"^([\w_]+):\s*(.+)$", line.strip())
            if m:
                meta[m.group(1)] = m.group(2)
    return meta, parts[2]


def sync_title(path: Path, title_fr: str, tool_id: str) -> None:
    raw = path.read_text(encoding="utf-8")
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return
    fm_lines = parts[1].splitlines()
    out_fm: list[str] = []
    has_title = False
    has_id = False
    for line in fm_lines:
        if line.startswith("title:"):
            out_fm.append(f"title: {yq(title_fr)}")
            has_title = True
        elif line.startswith("a11ynot_id:"):
            out_fm.append(f"a11ynot_id: {tool_id}")
            has_id = True
        else:
            out_fm.append(line)
    if not has_title:
        out_fm.insert(0, f"title: {yq(title_fr)}")
    if not has_id:
        out_fm.insert(1, f"a11ynot_id: {tool_id}")
    path.write_text(f"---\n" + "\n".join(out_fm) + f"\n---{parts[2]}", encoding="utf-8")


def wcag_lines(sc_list: list[str], sc_names: dict[str, str]) -> list[str]:
    out: list[str] = []
    for sc in sc_list:
        name = sc_names.get(sc, "")
        out.append(f"{sc} — {name}" if name else sc)
    return out


def main() -> None:
    if not OUTILS_DIR.is_dir():
        raise SystemExit(f"Missing {OUTILS_DIR} — migrer le contenu outils d’abord.")

    themes, labels = parse_labels_file()
    sc_names = load_sc_names()
    nots: dict[str, dict] = {}
    by_theme: dict[str, list[dict]] = {}

    for path in sorted(OUTILS_DIR.glob("ax-*.md")):
        meta, _body = parse_front_matter(path)
        tool_id = meta.get("a11ynot_id", "").upper() or path.stem.upper().replace("-", "_")
        if tool_id == "AX_TABLE_01A":
            tool_id = "AX_TABLE_01a"
        if tool_id == "AX_TABLE_01B":
            tool_id = "AX_TABLE_01b"
        info = labels.get(tool_id, {})
        title_short = info.get("title_fr") or tool_id
        title_fr = f"{title_short} ({tool_id})"
        summary_fr = info.get("summary_fr") or "Contre-exemple lié aux règles des outils de développement."
        theme = info.get("theme") or "aria"
        sc_list = info.get("wcag", [])
        slug = path.stem
        url = f"/outils/{slug}/"
        entry = {
            "tool_id": tool_id,
            "slug": slug,
            "theme": theme,
            "title_short_fr": title_short,
            "title_fr": title_fr,
            "label_fr": title_short,
            "summary_fr": summary_fr,
            "wcag": sc_list,
            "wcag_fr": wcag_lines(sc_list, sc_names),
            "url": url,
        }
        nots[tool_id] = entry
        by_theme.setdefault(theme, []).append(
            {
                "tool_id": tool_id,
                "label_fr": title_short,
                "title_fr": title_fr,
                "url": url,
            }
        )
        sync_title(path, title_fr, tool_id)

    grouped = []
    for key, items in by_theme.items():
        th = themes.get(key, {})
        grouped.append(
            {
                "id": key,
                "name_fr": th.get("name_fr", key),
                "order": th.get("order", 99),
                "examples": sorted(items, key=lambda x: x["tool_id"]),
            }
        )
    grouped.sort(key=lambda x: (x["order"], x["id"]))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Généré par scripts/build_a11ynot_outils_meta.py — ne pas éditer à la main.",
        "by_theme:",
    ]
    for block in grouped:
        lines.append(f'  - id: "{block["id"]}"')
        lines.append(f'    name_fr: "{block["name_fr"]}"')
        lines.append("    examples:")
        for ex in block["examples"]:
            lines.append(f'      - tool_id: "{ex["tool_id"]}"')
            lines.append(f"        label_fr: {yq(ex['label_fr'])}")
            lines.append(f"        title_fr: {yq(ex['title_fr'])}")
            lines.append(f'        url: "{ex["url"]}"')
    lines.append("nots:")
    for tid in sorted(nots.keys()):
        e = nots[tid]
        lines.append(f'  "{tid}":')
        lines.append(f'    theme: "{e["theme"]}"')
        lines.append(f"    title_short_fr: {yq(e['title_short_fr'])}")
        lines.append(f"    title_fr: {yq(e['title_fr'])}")
        lines.append(f"    label_fr: {yq(e['label_fr'])}")
        lines.append(f"    summary_fr: {yq(e['summary_fr'])}")
        lines.append("    wcag:")
        for sc in e["wcag"]:
            lines.append(f'      - "{sc}"')
        lines.append("    wcag_fr:")
        for line in e["wcag_fr"]:
            lines.append(f"      - {yq(line)}")
        lines.append(f'    slug: "{e["slug"]}"')
        lines.append(f'    url: "{e["url"]}"')

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    missing: list[str] = []
    for p in OUTILS_DIR.glob("ax-*.md"):
        meta, _ = parse_front_matter(p)
        tid = meta.get("a11ynot_id", "")
        if tid and tid not in labels:
            missing.append(tid)
    print(f"Wrote {len(nots)} outils, {len(grouped)} themes → {OUT}")
    if missing:
        print("Warning: no label for:", ", ".join(missing))


if __name__ == "__main__":
    main()
