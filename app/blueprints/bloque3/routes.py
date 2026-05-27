from flask import Blueprint, render_template

bloque3_bp = Blueprint("bloque3", __name__, template_folder="templates")

@bloque3_bp.route("/")
def home():
    return render_template("bloque3.html")
