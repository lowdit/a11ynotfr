#!/usr/bin/env python3
"""Génère data/a11ynot/wcag_meta.yaml (titres FR, regroupement par critère WCAG)."""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
WCAG_DIR = REPO / "content" / "wcag"
OUT = REPO / "data" / "a11ynot" / "wcag_meta.yaml"
LABELS_PATH = REPO / "data" / "a11ynot" / "failure_labels_fr.yaml"

# Libellés WCAG 2.0 (réf. courante en audit FR / RGAA)
SC_NAMES_FR: dict[str, str] = {
    "1.1.1": "Contenu non textuel",
    "1.3.1": "Informations et relations",
    "1.3.2": "Ordre significatif",
    "1.4.1": "Utilisation de la couleur",
    "1.4.2": "Contrôle du son",
    "1.4.3": "Contraste (minimum)",
    "1.4.4": "Redimensionnement du texte",
    "1.4.6": "Contraste (amélioré)",
    "1.4.8": "Présentation visuelle",
    "2.1.1": "Clavier",
    "2.2.1": "Réglage du délai",
    "2.2.2": "Pause, arrêt, masquage",
    "2.2.4": "Interruption et reprise",
    "2.4.3": "Parcours du focus",
    "2.4.4": "Lien — fonction du lien",
    "2.4.7": "Focus visible",
    "2.4.9": "Lien — fonction du lien (sans contexte)",
    "3.2.1": "Focus",
    "3.2.2": "Saisie",
    "3.2.5": "Changement de contexte",
    "4.1.1": "Analyse syntaxique",
    "4.1.2": "Nom, rôle, valeur",
}

FAILURE_CRITERIA: dict[str, list[str]] = {
    "F1": ["1.3.2"],
}


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


def load_failure_labels_fr() -> dict[str, str]:
    labels: dict[str, str] = {}
    if not LABELS_PATH.exists():
        return labels
    in_labels = False
    for line in LABELS_PATH.read_text(encoding="utf-8").splitlines():
        if line.strip() == "labels:":
            in_labels = True
            continue
        if not in_labels or not line.strip() or line.strip().startswith("#"):
            continue
        m = re.match(r'^\s+([A-Z0-9-]+):\s*"(.*)"\s*$', line)
        if m:
            labels[m.group(1)] = m.group(2)
    return labels


def load_persisted_title_en() -> dict[str, str]:
    if not OUT.exists():
        return {}
    text = OUT.read_text(encoding="utf-8")
    titles: dict[str, str] = {}
    current: str | None = None
    for line in text.splitlines():
        m = re.match(r'\s+"([^"]+)":\s*$', line)
        if m and re.match(r"^F", m.group(1)):
            current = m.group(1)
            continue
        if current and line.strip().startswith("title_en:"):
            val = line.split("title_en:", 1)[1].strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1].replace('\\"', '"')
            if val.startswith("W3:"):
                titles[current] = val
    return titles


def resolve_w3_title_en(
    meta: dict[str, str],
    body: str,
    failure_id: str,
    persisted: dict[str, str],
) -> str:
    if meta.get("w3_title_en", "").startswith("W3:"):
        return meta["w3_title_en"]
    title = meta.get("title", "")
    if title.startswith("W3:"):
        return title
    if failure_id in persisted:
        return persisted[failure_id]
    m = re.search(r'Example Page for (W3:[^"]+)"', body)
    if m:
        return m.group(1).strip()
    return title


def extract_criteria(title: str, failure_id: str) -> list[str]:
    if failure_id in FAILURE_CRITERIA:
        return FAILURE_CRITERIA[failure_id]
    found = re.findall(r"\d+\.\d+\.\d+", title)
    if found:
        seen: set[str] = set()
        out: list[str] = []
        for sc in found:
            if sc not in seen:
                seen.add(sc)
                out.append(sc)
        return out
    return ["0.0.0"]


def parse_w3_title(title: str) -> tuple[str, str, str]:
    m = re.match(r"W3:\s*([^:]+):\s*(.+)", title, re.S)
    if not m:
        return "", title, ""
    fid = m.group(1).strip().replace(" ", "")
    rest = m.group(2).strip()
    due = ""
    if " due to " in rest:
        _, due = rest.split(" due to ", 1)
    elif re.search(r"Failure of Success Criterion", rest, re.I):
        due = re.sub(
            r"^Failure of Success Criterion\s+[\d., and]+\s+(?:due to|for)\s+",
            "",
            rest,
            flags=re.I,
        )
    elif fid == "F1":
        due = rest
    return fid, rest, due


def label_for_failure(failure_id: str, labels: dict[str, str], name_fr: str) -> str:
    if failure_id in labels:
        return labels[failure_id]
    base = failure_id.split("-")[0]
    if base in labels:
        return labels[base]
    return f"Technique d’échec {failure_id} ({name_fr})"


def sync_page_front_matter(path: Path, title_fr: str, w3_title_en: str) -> None:
    meta, body = parse_front_matter(path)
    if not meta and not body:
        return
    raw = path.read_text(encoding="utf-8")
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return
    fm_lines = parts[1].splitlines()
    out_fm: list[str] = []
    has_title = False
    has_w3 = False
    for line in fm_lines:
        if line.startswith("title:"):
            out_fm.append(f"title: {yq(title_fr)}")
            has_title = True
        elif line.startswith("w3_title_en:"):
            out_fm.append(f"w3_title_en: {yq(w3_title_en)}")
            has_w3 = True
        else:
            out_fm.append(line)
    if not has_title:
        out_fm.insert(0, f"title: {yq(title_fr)}")
    if not has_w3 and w3_title_en.startswith("W3:"):
        out_fm.insert(1 if has_title else 0, f"w3_title_en: {yq(w3_title_en)}")
    path.write_text(f"---\n" + "\n".join(out_fm) + f"\n---{parts[2]}", encoding="utf-8")


def sc_sort_key(sc: str) -> tuple[int, ...]:
    parts = sc.split(".")
    return tuple(int(p) for p in parts)


def yq(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def main() -> None:
    if not WCAG_DIR.is_dir():
        raise SystemExit(f"Missing {WCAG_DIR} — migrer le contenu wcag d’abord.")

    labels_fr = load_failure_labels_fr()
    persisted_en = load_persisted_title_en()
    nots: dict[str, dict] = {}
    by_criterion: dict[str, list[dict]] = {}
    missing_labels: list[str] = []

    for path in sorted(WCAG_DIR.glob("w3-*.md")):
        meta, body = parse_front_matter(path)
        failure_id = meta.get("a11ynot_id", path.stem.replace("w3-", "").upper())
        slug = path.stem
        title_en = resolve_w3_title_en(meta, body, failure_id, persisted_en)
        fid, _rest, _due = parse_w3_title(title_en)
        if fid:
            failure_id = fid
        criteria = extract_criteria(title_en, failure_id)
        primary = criteria[0]
        name_fr = SC_NAMES_FR.get(primary, "Critère WCAG")
        label_fr = label_for_failure(failure_id, labels_fr, name_fr)
        if failure_id not in labels_fr and failure_id.split("-")[0] not in labels_fr:
            missing_labels.append(failure_id)
        title_fr = f"Critère {primary} — {label_fr} (échec {failure_id})"
        summary_fr = (
            f"Démonstration d’un échec au critère WCAG {primary} ({name_fr}), "
            f"technique W3C {failure_id} — {label_fr}."
        )
        rel = f"/wcag/{slug}/"
        entry = {
            "failure_id": failure_id,
            "slug": slug,
            "label_fr": label_fr,
            "title_fr": title_fr,
            "title_en": title_en,
            "summary_fr": summary_fr,
            "primary_criterion": primary,
            "criteria": criteria,
            "url": rel,
        }
        nots[failure_id] = entry
        sync_page_front_matter(path, title_fr, title_en)
        for sc in criteria:
            by_criterion.setdefault(sc, []).append(
                {
                    "failure_id": failure_id,
                    "label_fr": label_fr,
                    "title_fr": title_fr,
                    "url": rel,
                }
            )

    grouped = []
    for sc in sorted(by_criterion.keys(), key=sc_sort_key):
        if sc == "0.0.0":
            continue
        grouped.append(
            {
                "id": sc,
                "name_fr": SC_NAMES_FR.get(sc, "Critère WCAG"),
                "examples": sorted(by_criterion[sc], key=lambda x: x["failure_id"]),
            }
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Généré par scripts/build_a11ynot_wcag_meta.py — ne pas éditer à la main.",
        "sc_names:",
    ]
    for sc, name in sorted(SC_NAMES_FR.items(), key=lambda x: sc_sort_key(x[0])):
        lines.append(f'  "{sc}": "{name}"')
    lines.append("by_criterion:")
    for block in grouped:
        lines.append(f'  - id: "{block["id"]}"')
        lines.append(f'    name_fr: "{block["name_fr"]}"')
        lines.append("    examples:")
        for ex in block["examples"]:
            lines.append(f'      - failure_id: "{ex["failure_id"]}"')
            lines.append(f"        label_fr: {yq(ex['label_fr'])}")
            lines.append(f"        title_fr: {yq(ex['title_fr'])}")
            lines.append(f'        url: "{ex["url"]}"')
    lines.append("nots:")
    for fid in sorted(nots.keys(), key=lambda x: (sc_sort_key(nots[x]["primary_criterion"]), x)):
        e = nots[fid]
        lines.append(f'  "{fid}":')
        lines.append(f'    primary_criterion: "{e["primary_criterion"]}"')
        lines.append("    criteria:")
        for sc in e["criteria"]:
            lines.append(f'      - "{sc}"')
        lines.append(f"    label_fr: {yq(e['label_fr'])}")
        lines.append(f"    title_fr: {yq(e['title_fr'])}")
        lines.append(f"    summary_fr: {yq(e['summary_fr'])}")
        lines.append(f"    title_en: {yq(e['title_en'])}")
        lines.append(f'    slug: "{e["slug"]}"')
        lines.append(f'    url: "{e["url"]}"')

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(nots)} nots, {len(grouped)} criteria groups → {OUT}")
    if missing_labels:
        print(f"Warning: no FR label for: {', '.join(sorted(set(missing_labels)))}")


if __name__ == "__main__":
    main()
