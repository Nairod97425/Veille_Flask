### Énoncés (15 exercices)

1. Crée une route `/hello` qui retourne "Hello World".
2. Crée une page `/contact` qui retourne du HTML simple (titre + paragraphe).
3. Crée une route avec paramètre `/user/<name>` qui salue l’utilisateur.
4. Mets en place un `base.html` et un `index.html` qui l’étend (héritage Jinja).
5. Ajoute un formulaire `/age` (GET/POST) qui affiche "Tu as X ans".
6. Définis une liste Python `articles=[{"title":..., "author":...}, ...]` et affiche‑la dans un template avec une boucle Jinja.
7. Ajoute un fichier `static/style.css` et utilise‑le via `url_for('static', ...)`.

8. Crée une route `/api/ping` qui retourne du JSON `{ "ping": "pong" }` avec `jsonify`.
9. Utilise SQLite pour créer une table `users(name TEXT)` et insérer un utilisateur via une route.
10. Crée `/users` qui liste les utilisateurs depuis SQLite dans un template.
11. Ajoute un gestionnaire d’erreur 404 personnalisé avec un template `404.html`.
12. Lis un paramètre de **query string** `/search?q=...` et affiche la requête.
13. Crée un **Blueprint** `blog` avec une route `/blog` séparée dans un module.
14. (SQLAlchemy) Crée un modèle `Note(title, body)` avec Flask‑SQLAlchemy, routes pour créer et lister.
15. Crée une endpoint `/api/patients` qui renvoie la liste des patients depuis SQLite en JSON (prépare pour le projet e‑santé).
