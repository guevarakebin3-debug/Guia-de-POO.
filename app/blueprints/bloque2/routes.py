from flask import Blueprint, render_template

bloque2_bp = Blueprint(
    "bloque2", __name__,
    template_folder="templates"
)

@bloque2_bp.route("/")
def home():
    return render_template("bloque2.html")
