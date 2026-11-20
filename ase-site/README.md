# Site ASE – Agriculture, Services et Expertise

Site vitrine statique (HTML/CSS/JS), sans dépendance ni outil de build requis.

## Structure
- `*.html` : pages (accueil, qui-sommes-nous, expertises, equipe, actualites, contact, mentions-legales, confidentialite)
- `css/style.css` : styles (couleurs #286B45 / #78A96B en variables en haut du fichier)
- `js/config.js` : configuration du formulaire ; `js/main.js` : envoi du formulaire
- `images/` : logo et photos ; `build.py` : génère les pages (optionnel, on peut aussi éditer les .html)

## Tester en local
Ouvrir `index.html` dans un navigateur, ou lancer `python3 -m http.server` dans ce dossier puis aller sur http://localhost:8000.

## Compléter les contenus
Les passages marqués « À compléter » / « Contenu provisoire » sont des emplacements : adresse, téléphone, e-mail, équipe, actualités, prestations, mentions légales, politique de confidentialité, liens LinkedIn / Facebook / YouTube (remplacer les `href="#"`).
Photos : déposer les fichiers optimisés (JPEG/WebP, idéalement < 200 Ko) dans `images/` et remplacer les blocs `.ph` par `<img src="images/..." alt="description" loading="lazy">`. Utiliser uniquement des photos dont le cabinet détient les droits.

## Activer le formulaire de contact
1. Créer un formulaire sur un service d'envoi (ex. Formspree) avec l'adresse e-mail du cabinet.
2. Copier l'URL fournie dans `js/config.js` (`formEndpoint`).
3. Tester l'envoi une fois le site en ligne.

## Publier
Déposer tout le dossier chez un hébergeur de sites statiques (OVH, Netlify, GitHub Pages, etc.) ou par FTP à la racine du site. Penser à : nom de domaine, HTTPS, ajout de `sitemap.xml` avec l'adresse définitive, et vérification des mentions légales.
