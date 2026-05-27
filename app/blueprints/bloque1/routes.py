from flask import Blueprint, render_template

bloque1_bp = Blueprint(
    "bloque1", __name__,
    template_folder="templates"
)

@bloque1_bp.route("/")
def home():
    return render_template("bloque1.html")
