# a11yNot FR

Reprise française et évolution du corpus [a11yNot](https://a11ynot.com/) (~2016), en site Hugo **dédié** et **open source**.

## État actuel

- **Corpus WCAG 2.0 + outils** migré depuis le blog (~100+ fiches).
- **Communauté auditeurs** : accès par critère WCAG, guide, contributions open source ([lowdit/a11ynotfr](https://github.com/lowdit/a11ynotfr)).
- **Identité visuelle** : palette teal / bleu-vert (`assets/css/a11ynot.css`).
- **Blog** : [`docs/MIGRATION.md`](docs/MIGRATION.md) — annonce sur `/a11ynot/`, menu → site FR.

## Objectifs produit

1. **Moderniser** la présentation (listes en cartes, navigation cohérente, fiches auditeur).
2. **Publier** comme les autres sites Hugo du workspace (GitHub Pages ou hébergeur statique).
3. **Ouvrir** les contributions (Nots, libellés FR, métadonnées WCAG) — voir [CONTRIBUTING.md](CONTRIBUTING.md).

## Développement local

Thème **higo** via symlink (comme le blog) :

```bash
cd a11ynotfr
ln -sf ../../higo themes/higo   # une fois
hugo server -D
```

En **CI / production** : `config/production/hugo.toml` utilise `theme = ["github.com/lowdit/higo"]` + `hugo mod get` dans le workflow Pages.

## Relation avec bertrandkeller.github.io

Voir [`docs/MIGRATION.md`](docs/MIGRATION.md) — corpus canonique ici, annonce sur le blog.
