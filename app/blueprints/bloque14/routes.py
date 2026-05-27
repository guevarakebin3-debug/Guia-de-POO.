from flask import Blueprint, render_template

bloque14_bp = Blueprint("bloque14", __name__, template_folder="templates")

@bloque14_bp.route("/")
def home():
    return render_template("bloque14.html")
