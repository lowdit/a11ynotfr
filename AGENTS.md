# Consignes — a11ynotfr

Site Hugo **autonome** : corpus a11yNot en français, évolution open source du fork hébergé sur `bertrandkeller.github.io/content/a11ynot/`.

Méthode commune : [`../lowtech-dev-method/`](../lowtech-dev-method/).

## Intention

- Publier des **Nots** (démos d’échec isolées) + fiches auditeur.
- Accueillir des **contributions** (contenu, traductions, nouveaux Nots) via GitHub.
- Rester **accessible** sur le chrome du site ; les zones `.rendered-not` restent volontairement défectueuses.

## Zones

| Zone | Usage |
|------|--------|
| `content/` | Pages et fiches Not |
| `data/a11ynot/` | Métadonnées (WCAG, outils, libellés FR) |
| `layouts/a11ynot/` | Présentation (listes en cartes, fiches) |
| `assets/`, `static/a11ynot/` | Styles d’intégration, démos, assets hérités |
| `scripts/` | `build_a11ynot_*.py`, `convert_a11ynot_jekyll.py` (chemins adaptés à ce dépôt) |

## Migration depuis le blog

Source actuelle : `../bertrandkeller.github.io/` (`content/a11ynot/`, `data/a11ynot/`, `layouts/a11ynot/`, `static/a11ynot/`, scripts). Ne pas dupliquer sans plan : soit **import ponctuel**, soit **module Hugo** consommé par le blog pour une URL miroir.

## Exécution IA

- Incrément approuvé dans `lowtech-dev-method/prompts/NEXT.md` ou demande explicite sur ce dépôt.
- Pas de commit, push, publication sans accord humain.
- Qualité web : [`../lowtech-dev-method/WEB-QUALITY.md`](../lowtech-dev-method/WEB-QUALITY.md).
