from flask import Blueprint, render_template

bloque12_bp = Blueprint("bloque12", __name__, template_folder="templates")

@bloque12_bp.route("/")
def home():
    return render_template("bloque12.html")
