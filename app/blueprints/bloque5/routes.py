from flask import Blueprint, render_template

bloque5_bp = Blueprint("bloque5", __name__, template_folder="templates")

@bloque5_bp.route("/")
def home():
    return render_template("bloque5.html")
