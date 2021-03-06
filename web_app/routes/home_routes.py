# web_app/routes/home_routes.py

from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    return render_template("prediction_form.html")

@home_routes.route("/hello")
def hello():
    print('VISITNG THE HELLO PAGE')
    x = 2 + 2
    return f"Hello World! {x}"

@home_routes.route("/about")
def about():
    print('VISITNG THE HOME PAGE')
    return "About me"
