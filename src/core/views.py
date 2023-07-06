from flask import Blueprint, render_template
from flask_login import login_required

core_bp = Blueprint("core", __name__)


@core_bp.route("/")
def home():
    return render_template("core/index.html")

@core_bp.route("/panel")
@login_required
def panel():
    return "hello"