from flask import Blueprint, render_template

bloque6_bp = Blueprint("bloque6", __name__, template_folder="templates")

@bloque6_bp.route("/")
def home():
    return render_template("bloque6.html")
