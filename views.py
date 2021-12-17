from flask import Blueprint, render_template, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def homepage():
    return render_template("index.html")

@views.route("/home")
def home_redirect():
    return redirect(url_for("views.homepage"))

@views.route("/admin")
def admin():
    return render_template("admin.html")

@views.route("/story")
def story():
    return render_template("story.html")

@views.route("/story")
def story_redirect():
    return redirect(url_for("views.story"))

@views.route("/locations")
def locations():
    return render_template("locations.html")

@views.route("/locations")
def locations_redirect():
    return redirect(url_for("views.locations"))

@views.route("/classes")
def classes():
    return render_template("classes.html")

@views.route("/classes")
def classes_redirect():
    return redirect(url_for("views.classes"))

@views.route("/enemies")
def enemies():
    return render_template("enemies.html")

@views.route("/enemies")
def enemies_redirect():
    return redirect(url_for("views.enemies"))
