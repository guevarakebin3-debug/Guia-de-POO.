from flask import Blueprint, render_template

bloque10_bp = Blueprint("bloque10", __name__, template_folder="templates")

@bloque10_bp.route("/")
def home():
    return render_template("bloque10.html")
