from flask import Blueprint, render_template

bloque19_bp = Blueprint("bloque19", __name__, template_folder="templates")

@bloque19_bp.route("/")
def home():
    return render_template("bloque19.html")
