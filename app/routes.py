from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/bloque/<int:num>")
def bloque(num):
    return render_template(f"bloque{num}.html", bloque=num)
