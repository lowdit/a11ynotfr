# Migration blog → a11yNot FR

## Décision

| Avant | Après |
|-------|--------|
| Corpus dans `bertrandkeller.github.io/content/a11ynot/` | **`a11ynotfr`** (dépôt et site dédiés) |
| URLs `/a11ynot/wcag/…` sur le blog | URLs `/wcag/…` sur a11yNot FR |
| Scripts / data / static dans le blog | **`a11ynotfr/scripts`**, `data/a11ynot/`, `static/a11ynot/` |

## Blog (nettoyage)

- Supprimé : contenu WCAG/outils, `data/a11ynot`, `static/a11ynot`, layouts `a11ynot`, scripts de build.
- Conservé : `content/a11ynot/_index.md` (annonce de déménagement).
- Menu principal : lien externe vers le site FR.

## Canon éditorial

Toute évolution du corpus (Nots, libellés, métadonnées) se fait **uniquement** dans `a11ynotfr`. Ne pas recopier dans le blog.

## Regénérer les index

```bash
cd a11ynotfr
python3 scripts/build_a11ynot_wcag_meta.py
python3 scripts/build_a11ynot_outils_meta.py
```

## Anciens liens

Les URL profondes `bertrandkeller.github.io/a11ynot/...` ne redirigent pas automatiquement (GitHub Pages). Mettre à jour les bookmarks et articles qui pointaient vers le blog.
