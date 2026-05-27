from flask import Blueprint, render_template

bloque4_bp = Blueprint("bloque4", __name__, template_folder="templates")

@bloque4_bp.route("/")
def home():
    return render_template("bloque4.html")
