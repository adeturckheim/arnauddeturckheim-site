# arnauddeturckheim.com

Site d'artiste statique d'Arnaud de Turckheim, sans framework, généré par `build.py`.

## Pages

- `/` accueil : baobab, exposition en cours, citation, liens
- `/photographies/` grille des 18 images, et une page par œuvre (`/photographies/<titre>/`)
- `/expositions/` et `/expositions/ce-qui-demeure/` : infos, intro, œuvres, texte de Pierre El Khoury, contacts
- `/a-propos/` bio, démarche, parcours
- `/contact/` mail d'Arnaud, puis Pierre El Khoury en fin de page

Aucun prix ni numéro de téléphone sur le site.

## Fichiers

- `content.py` : tous les textes éditoriaux et la liste des œuvres
- `content/texte.txt` : texte de Pierre (copie de `Expo/8 - Texte exposition/texte.txt` sur le Drive)
- `style.css`, `favicon.svg`
- `img/works` (2200 px) et `img/thumbs` (900 px), exportés depuis `Expo/1 - Photos/3 - JPEG`
- `CNAME` : domaine personnalisé pour GitHub Pages

## Mettre à jour

Modifier `content.py` ou `style.css`, lancer `python3 build.py`, vérifier avec
`python3 -m http.server 8765`, committer, pousser.
