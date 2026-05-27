from flask import Blueprint, render_template

bloque15_bp = Blueprint("bloque15", __name__, template_folder="templates")

@bloque15_bp.route("/")
def home():
    return render_template("bloque15.html")
