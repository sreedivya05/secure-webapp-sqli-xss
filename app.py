from flask import Flask, request, render_template
import sqlite3
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        # ❌ Vulnerable query (for SQLi learning)
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            message = "Login Successful"
        else:
            message = "Login Failed"

        conn.close()

    return render_template("login.html", message=message)

@app.route("/comment", methods=["GET", "POST"])
def comment():
    comment_text = ""
    if request.method == "POST":
        comment_text = escape(request.form["comment"])  # XSS protection
    return render_template("comment.html", comment=comment_text)

if __name__ == "__main__":
    app.run(debug=True)
