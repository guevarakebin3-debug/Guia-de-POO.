from flask import Blueprint, render_template

bloque21_bp = Blueprint("bloque21", __name__, template_folder="templates")

@bloque21_bp.route("/")
def home():
    return render_template("bloque21.html")

