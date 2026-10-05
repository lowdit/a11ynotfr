# Contribuer à a11yNot FR

Merci de participer à un corpus **pédagogique** (contre-exemples), pas à un audit de production.

## Idées de contributions

- Libellés français (`data/a11ynot/failure_labels_fr.yaml`, fiches `nots.yaml`).
- Nouveau **Not** : une violation isolée, bannière + zone de démo claire, métadonnées WCAG ou règle outil.
- Corrections **accessibilité du chrome** (navigation, cartes, titres) — pas « réparer » la démo volontaire.
- Signaler un Not **obsolète** (API, pattern 2016) avec proposition de statut (héritage / toujours d’actualité).

## Format d’un Not

- Front matter : `a11ynot_id`, `category` (`wcag` | `outils`), `gistID` si code externe, `layout: a11ynot`.
- Zone de démo entre titres « Début » / « Fin » de l’exemple.
- Fiche « Comprendre cet exemple » alimentée par `data/a11ynot/`.

## Processus

1. Issue ou discussion courte (éviter les doublons avec un Not existant).
2. Pull request ciblée ; description : critère WCAG, comportement attendu des outils, capture si utile.
3. Revue humaine — pas de promesse de conformité légale.

## Code de conduite

Respect, sources citées (W3C, Google ADT), pas de contenu discriminatoire dans les exemples.
