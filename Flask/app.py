from flask import Flask, render_template, request, redirect
import sqlite3  # You can also use MySQL or PostgreSQL

app = Flask(__name__)

# Create database connection
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            photo BLOB
        )
    ''')
    conn.commit()
    conn.close()

init_db()  # Initialize database

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    photo = request.files["Photo"].read()  # Read the uploaded file

    # Save data to database
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, photo) VALUES (?, ?, ?)", (name, email, photo))
    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
