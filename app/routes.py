 from flask import render_template, request, redirect, url_for
from app import app

recipes = []
comments = []
authors = ["Mary Berry", "Duff Goldman", "Gordon Ramsay"]

@app.route("/")
def home():
    return render_template("home.html", recipes=recipes)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        image = request.form["image"]
        ingredients = request.form["ingredients"].split(",")
        recipes.append({"title": title, "image": image, "ingredients": ingredients})
        return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/comments", methods=["GET", "POST"])
def comment():
    if request.method == "POST":
        user = request.form["user"]
        message = request.form["message"]
        comments.append({"user": user, "message": message})
    return render_template("comments.html", comments=comments)

@app.route("/authors")
def authors_page():
    return render_template("authors.html", authors=authors)

@app.route("/login")
def login():
    return render_template("login.html")
