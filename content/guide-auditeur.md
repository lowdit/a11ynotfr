---
title: "Guide auditeur"
description: "Comment utiliser les Nots comme support de formation et de calibration en audit."
layout: a11ynot
type: a11ynot
menus:
  main:
    name: Guide
    weight: 4
---

Ce guide s’adresse aux **auditeurs**, **reviewers** et **formateurs** qui s’appuient sur a11yNot comme **banque de contre-exemples**, pas comme preuve de conformité d’un site client.

## Intérêt de cette section

[a11yNot](https://a11ynot.com/) répond à un manque : beaucoup de ressources montrent le « bon » accessibilité, peu montrent des **erreurs isolées** et reproductibles. Chaque page ici contient **une** violation volontaire, dans un cadre encadré — même idée que la démo W3C [Before and After](https://www.w3.org/WAI/demos/bad/), mais découpée en fiches courtes.

**Pourquoi ce site reprend ce corpus**

- **Former l’œil** : relier une règle abstraite (WCAG, règle d’outil) à un rendu concret.
- **Calibrer les outils** : vérifier qu’axe, WAVE ou autre remonte bien le type de problème attendu sur la page.
- **Préparer l’audit réel** : entraînement sans confondre avec un constat sur un produit en production.

Cette version française ajoute navigation, cadre pédagogique et **fiches auditeur** (statut, observation, apport) autour des démos d’origine.

## Trois statuts de Not

| Statut | Signification | Usage en audit |
|--------|----------------|--------------|
| **Héritage (2016)** | Reprise du dépôt a11yNot / techniques WCAG 2.0 de l’époque | Utile pour la pédagogie et les outils ; attention aux patterns datés (JS inline, vieux API). |
| **Toujours d’actualité** | Problème encore courant aujourd’hui | Prioriser en formation et en contrôle outil + manuel. |
| **Ajout communautaire** | Nouveau Not sur a11yNot FR | Complète le corpus (RGAA, composants récents, retours terrain). |

Les badges apparaissent sur chaque fiche Not. La documentation détaillée est **progressive** : les Nots les plus utiles en audit sont documentés en premier dans `data/a11ynot/nots.yaml`.

## Protocole recommandé (une fiche)

1. Lire **Pour l’auditeur** (statut, en bref, apport).
2. Parcourir **Début / Fin de l’exemple** sans modifier le DOM.
3. Lancer **un outil automatique** adapté au type de Not (contraste, ARIA, formulaires…).
4. Compléter par **test manuel** si le critère l’exige (clavier, zoom 200 %, lecteur d’écran, désactivation CSS/images).
5. Ouvrir **Code de cet exemple** (Gist) pour lier la violation au snippet.
6. Noter dans votre rapport : règle, preuve (capture, extrait code), gravité — **jamais** « non conforme car similaire à a11yNot » sur un site client.

## Ce que cette ressource ne remplace pas

- Une **grille RGAA / WCAG** appliquée au périmètre réel du site audité.
- Des **parcours utilisateur** complets (plusieurs pages, authentification, états dynamiques).
- Une **décision de conformité** : les Nots sont des micro-scénarios didactiques.

## Enrichir le corpus

- Métadonnées auditeur : `data/a11ynot/nots.yaml` (voir [Maintenance des fiches](/maintenance-donnees/)).
- Regénération des démos Jekyll : `scripts/convert_a11ynot_jekyll.py` (ne pas écraser les champs `not_status` / doc sans fusion).
- Nouveaux Nots : slug sous `content/`, `not_status: nouveau`, démo isolée dans `.rendered-not`.
