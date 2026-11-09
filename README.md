# arnauddeturckheim.com

Site d'artiste statique et bilingue d'Arnaud de Turckheim, sans framework, généré par `build.py`.
Français à la racine, anglais sous `/en/` (`/en/photographs/`, `/en/exhibitions/`, `/en/about/`, `/en/contact/`).
Les titres des œuvres restent en français dans les deux versions.

## Pages

- `/` accueil : baobab, exposition en cours, citation, liens
- `/photographies/` grille des 18 images, et une page par œuvre (`/photographies/<titre>/`)
- `/expositions/` et `/expositions/ce-qui-demeure/` : infos, intro, œuvres, texte de Pierre El Khoury, contacts
- `/a-propos/` bio, démarche, parcours
- `/contact/` mail d'Arnaud, puis Pierre El Khoury en fin de page

Aucun prix ni numéro de téléphone sur le site.

## Fichiers

- `content.py` : textes éditoriaux FR puis EN, et la liste des œuvres
- `build.py` : aussi les libellés d'interface FR/EN (dictionnaire `T`)
- `content/texte-en.txt` : traduction anglaise du texte de Pierre
- `content/texte.txt` : texte de Pierre (copie de `Expo/8 - Texte exposition/texte.txt` sur le Drive)
- `style.css`, `favicon.svg`
- `img/large` (3200 px, visionneuse sur grands écrans), `img/works` (2200 px) et `img/thumbs` (900 px), exportés depuis `Expo/1 - Photos/3 - JPEG`
- `viewer.js` : visionneuse (clavier, clic, swipe, plein écran avec F, lien direct #titre)
- `CNAME` : domaine personnalisé pour GitHub Pages

## Mettre à jour

Modifier `content.py` ou `style.css`, lancer `python3 build.py`, vérifier avec
`python3 -m http.server 8765`, committer, pousser.
