from flask import Blueprint, render_template

bloque8_bp = Blueprint("bloque8", __name__, template_folder="templates")

@bloque8_bp.route("/")
def home():
    return render_template("bloque8.html")
