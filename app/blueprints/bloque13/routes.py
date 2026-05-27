from flask import Blueprint, render_template

bloque13_bp = Blueprint("bloque13", __name__, template_folder="templates")

@bloque13_bp.route("/")
def home():
    return render_template("bloque13.html")
