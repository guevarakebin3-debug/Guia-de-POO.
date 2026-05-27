from flask import Blueprint, render_template

bloque11_bp = Blueprint("bloque11", __name__, template_folder="templates")

@bloque11_bp.route("/")
def home():
    return render_template("bloque11.html")
