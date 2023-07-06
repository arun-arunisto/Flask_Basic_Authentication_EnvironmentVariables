import os
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_login import LoginManager
from src.accounts.models import User, db
from src.core.views import core_bp
from src.accounts.views import accounts_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.getenv('APP_SETTINGS'))
    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "accounts.login"
    login_manager.login_message_category = "danger"


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()

    @app.errorhandler(401)
    def unauthorized_page(error):
        return render_template("errors/401.html"), 401

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("errors/500.html"), 500

    app.register_blueprint(accounts_bp)
    app.register_blueprint(core_bp)
    return app