# a11yNot FR

Reprise française et évolution du corpus [a11yNot](https://a11ynot.com/) (~2016), en site Hugo **dédié** et **open source**.

## État actuel

- **Squelette** de dépôt dans `sites/hugo/a11ynotfr/` (config, layouts cartes, navigation).
- **Corpus complet** encore dans [`bertrandkeller.github.io`](../bertrandkeller.github.io/) (`content/a11ynot/`, etc.) — migration à planifier.

## Objectifs produit

1. **Moderniser** la présentation (listes en cartes, navigation cohérente, fiches auditeur).
2. **Publier** comme les autres sites Hugo du workspace (GitHub Pages ou hébergeur statique).
3. **Ouvrir** les contributions (Nots, libellés FR, métadonnées WCAG) — voir [CONTRIBUTING.md](CONTRIBUTING.md).

## Développement local

```bash
cd a11ynotfr
hugo mod get
hugo server -D
```

(`baseURL` et déploiement à configurer avant mise en production.)

## Relation avec bertrandkeller.github.io

Tant que la migration n’est pas faite, le blog peut garder une section `/a11ynot/` qui **pointe** vers ce site ou réutilise un **module Hugo** — à trancher (SEO, une vs deux URLs).
