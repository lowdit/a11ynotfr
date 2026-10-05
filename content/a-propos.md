---
title: "À propos d'a11yNot sur ce site"
description: "Origine du projet, objectifs et mise à jour de la reprise française."
layout: a11ynot
type: a11ynot
---

## Origine : a11yNot.com

Un **a11yNot** est un fragment de page qui crée une barrière pour certaines personnes en situation de handicap. Le site d’origine vise à :

- rester **conforme** en dehors de la zone de démo ;
- ne faire **échouer les outils** que dans cette zone ;
- documenter des cas typiques remontés par les **tests automatiques**.

Inspiration avouée : [Web Pages That Suck](http://www.webpagesthatsuck.com/) (« apprendre le bon design en regardant le mauvais »), appliquée à l’accessibilité. Voir aussi la démo W3C [Before and After](http://www.w3.org/WAI/demos/bad/) pour un parcours « site entier » avant/après.

## Reprise a11yNot FR

| Aspect | Version d’origine | Cette version |
|--------|-------------------|---------------|
| Langue | Anglais | Interface et guides auditeur en français |
| Public | Développeurs curieux | **Auditeurs**, formateurs, reviewers |
| Contenu démo | Inchangé (violation volontaire) | Inchangé dans `.rendered-not` |
| Pédagogie | Titre + démo + Gist | + statut (héritage / actuel / nouveau), observation, apport |
| Évolution | Dépôt GitHub 2016 | Enrichissement progressif + futurs **Nots nouveaux** |

Source technique : [a11yNot/a11yNot.github.io](https://github.com/a11yNot/a11yNot.github.io). Crédits : [a11ynot.com](https://a11ynot.com/).

## Mise à jour actualisée (vision)

1. **Conserver** le corpus historique comme **référence d’échecs WCAG 2.0** et règles outils — avec badge *Héritage* et mise en garde sur le contexte (JS, HTML ancien).
2. **Marquer** les Nots encore fréquents en audit (*Toujours d’actualité*) et les documenter en priorité dans `data/a11ynot/nots.yaml`.
3. **Ajouter** des Nots *Ajout communautaire* (composants actuels, RGAA 4, focus visible, modales, live regions…) sans mélanger avec les specimens 2016.
4. **Relier** aux ressources accessibilité du site lorsque pertinent — sans transformer cette section en blog.

Pour la méthode de lecture en audit : **[guide auditeur](/guide-auditeur/)**.
