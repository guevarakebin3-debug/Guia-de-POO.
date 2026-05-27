from flask import Blueprint, render_template

bloque17_bp = Blueprint("bloque17", __name__, template_folder="templates")

@bloque17_bp.route("/")
def home():
    return render_template("bloque17.html")
