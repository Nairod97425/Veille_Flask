from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3
print(sqlite3.sqlite_version)
app = Flask(__name__)


# exo 1
@app.route("/hello")
def hello_World():
    return "Hello world"


# exo 2
@app.route("/contact")
def contact():
    return "<h1>titre</h1><p>paragraphe</p>"


# exo3
@app.route("/user/<name>")
def user(name):
    return f"hello {name}"


# exemple et exo4
@app.route("/index")
def index():
    return render_template("index.html")


# exemple 
@app.route("/perso/<name>")
def perso(name):
    return render_template("perso.html", username=name)


# exemple
@app.route("/add/<string:task>")
def add(task):
    con = sqlite3.connect("tasks.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY, task TEXT)")
    cur.execute("INSERT INTO todo (task) VALUES (?)", (task,))
    con.commit()
    con.close()
    return f"Tâche '{task}' ajoutée !"


# exo5
@app.route("/form_age", methods=["GET", "POST"])
def age2():
    if request.method == "POST":
        age = request.form["age"]
        return f"Tu as {age} ans."
    return '''
        <form methods="post">
            <input type="text" name="age">
            <input type="submit" value="Envoyer">
        </form>
'''

# exo6
@app.route("/age", methods=["GET", "POST"])
def age():
    if request.method == "POST":
        # Récupère l'âge saisi dans le formulaire
        age_str = request.form.get("age", type="int")
        try:
            age = int(age_str)
            # Passe l'âge au template pour l'afficher
            return render_template('age.html', age=age)
        except (ValueError, TypeError):
            error = "Veuillez entrer un âge valide (un nombre entier)."
            return render_template('age.html', error=error)
    # Si c'est une requête GET, affiche juste le formulaire
    return render_template('age.html')


# exemple 
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f"Bonjour {name} !"
    return '''
        <form methods="post">
            <input type="text" name="name">
            <input type="submit" value="Envoyer">
        </form>
'''
# exo7

@app.route("/artiste", methods=["GET","POST"])
def artiste():
    articles = [
        {"title":"article1",
        "author":"author1"},
        {"title":"article2",
        "author":"author2"},
        {"title":"article3",
        "author":"author3"},
        {"title":"article3",
        "author":"author3"},
    ]
    return render_template("artiste.html", articles=articles)

# exo8
@app.route("/api/ping", methods=["GET"])
def ReturnJSON():
    if request.method=="GET":
        data = {"ping": "pong"}
        return jsonify(data)

# exo9
def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS PARTICIPANTS (name TEXT)')

init_db()

@app.route("/sqlite")
def sqlite():
    return render_template('sqlite.html')

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        name = request.form['name']
        try:
            with sqlite3.connect("database.db") as users:
                cursor = users.cursor()
                cursor.execute("INSERT INTO PARTICIPANTS (name) VALUES (?)", (name,))
                users.commit()
        except sqlite3.Error as e:
            print(f"Erreur lors de l'insertion : {e}")
        return redirect(url_for('participants'))  # Redirige vers la liste des participants
    else:
        return render_template('join.html')


@app.route('/participants')
def participants():
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM PARTICIPANTS')

    data = cursor.fetchall()
    return render_template("participants.html", data=data)


if __name__ ==  '__main__':
    app.run(debug=True)