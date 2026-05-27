from flask import Blueprint, render_template

bloque7_bp = Blueprint("bloque7", __name__, template_folder="templates")

@bloque7_bp.route("/")
def home():
    return render_template("bloque7.html")
