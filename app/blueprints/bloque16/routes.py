from flask import Blueprint, render_template

bloque16_bp = Blueprint("bloque16", __name__, template_folder="templates")

@bloque16_bp.route("/")
def home():
    return render_template("bloque16.html")
