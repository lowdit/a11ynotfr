# Scripts a11ynotfr

| Script | Rôle |
|--------|------|
| `convert_a11ynot_jekyll.py` | Import depuis un clone Jekyll a11yNot (`_nots/*.md`) → `content/wcag/`, `content/outils/` |
| `build_a11ynot_wcag_meta.py` | Régénère `data/a11ynot/wcag_meta.yaml` + titres FR des pages WCAG |
| `build_a11ynot_outils_meta.py` | Régénère `data/a11ynot/outils_meta.yaml` + titres FR des pages outils |

## Chemins (différences avec le blog)

| Blog `bertrandkeller.github.io` | `a11ynotfr` |
|-----------------------------------|-------------|
| `content/a11ynot/wcag/` | `content/wcag/` |
| `content/a11ynot/outils/` | `content/outils/` |
| URLs `/a11ynot/wcag/…` | URLs `/wcag/…` |

Les démos iframe restent sous **`/a11ynot/demos/`** (`static/a11ynot/demos/`), comme sur le blog, jusqu’à éventuel simplification.

## Usage

```bash
cd a11ynotfr

# 1. Import initial (optionnel, si dépôt Jekyll d’origine)
python3 scripts/convert_a11ynot_jekyll.py /chemin/vers/a11yNot.github.io

# 2. Métadonnées (nécessite content + data/a11ynot/*_labels_fr.yaml)
python3 scripts/build_a11ynot_wcag_meta.py
python3 scripts/build_a11ynot_outils_meta.py
```

Ordre recommandé : WCAG meta d’abord (les libellés critères alimentent outils_meta).

## Source blog

Les versions d’origine vivent encore dans `bertrandkeller.github.io/scripts/` ; après migration du corpus, ne maintenir les scripts **que** dans `a11ynotfr`.
