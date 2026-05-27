from flask import Blueprint, render_template

bloque9_bp = Blueprint("bloque9", __name__, template_folder="templates")

@bloque9_bp.route("/")
def home():
    return render_template("bloque9.html")

