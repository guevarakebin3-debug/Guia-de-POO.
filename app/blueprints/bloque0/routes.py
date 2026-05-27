from flask import Blueprint, render_template

bloque0_bp = Blueprint(
    "bloque0", __name__,
    template_folder="templates"
)

@bloque0_bp.route("/")
def home():
    return render_template("bloque0.html")
