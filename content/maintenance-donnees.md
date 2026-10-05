---
title: "Maintenance des fiches auditeur"
description: "Comment éditer data/a11ynot/nots.yaml sans casser le build Hugo."
layout: a11ynot
type: a11ynot
---

Hugo ne charge que des **YAML/JSON/TOML** dans `data/` — pas de Markdown à cet emplacement.

Fichiers :

- **`data/a11ynot/wcag_meta.yaml`** — titres FR et liste par critère WCAG (généré : `python3 scripts/build_a11ynot_wcag_meta.py`).
- **`data/a11ynot/failure_labels_fr.yaml`** — libellés courts FR par technique W3C (F36-1, …) ; source des titres de page.
- **`data/a11ynot/outils_labels_fr.yaml`** / **`outils_meta.yaml`** — libellés FR des règles AX_* ; génération : `python3 scripts/build_a11ynot_outils_meta.py`.
- **`data/a11ynot/nots.yaml`** — fiches détaillées outils / quelques WCAG.

- **`defaults`** : textes pour les Nots sans fiche dédiée (statut *Héritage*, checklist d’observation).
- **`nots.<a11ynot_id>`** : fiche complète (`summary_fr`, `observe`, `apport`, `wcag`, `not_status`, …).

Clé = `a11ynot_id` du front matter (ex. `AX_ARIA_01`, `F65`), pas le slug URL.

## Statuts

| Valeur YAML | Badge |
|-------------|--------|
| `heritage` | Héritage (2016) |
| `actuel` | Toujours d’actualité |
| `nouveau` | Ajout communautaire (a11ynotfr) |

Sans entrée dans `nots`, le gabarit affiche le badge *Héritage* et les listes `defaults`.

## Nouveau Not

1. Fichier sous `content/outils/` ou `wcag/`.
2. Entrée dans `nots.yaml` avec `not_status: nouveau`.
3. Ne pas mettre de ligne `---` en tête de `nots.yaml` (fichier data pur, pas de front matter).
4. Ne pas modifier le HTML de la démo dans `.rendered-not` sauf pour introduire la violation voulue.
