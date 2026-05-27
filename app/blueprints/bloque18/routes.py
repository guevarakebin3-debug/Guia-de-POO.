from flask import Blueprint, render_template

bloque18_bp = Blueprint("bloque18", __name__, template_folder="templates")

@bloque18_bp.route("/")
def home():
    return render_template("bloque18.html")
