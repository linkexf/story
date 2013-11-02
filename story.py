#coding=utf-8

from flask import Flask, g, request, jsonify, redirect, flash, render_template, url_for
from flask.ext.principal import Principal, identity_loaded
from flask.ext.babel import Babel
from flask.ext.markdown import Markdown
from flaskext.uploads import configure_uploads
from exts import db, mail, photos
from models import User


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config)
    configure_extensions(app)
    Markdown(app)
    configure_i18n(app)
    configure_identity(app)
    configure_errorhandlers(app)
    configure_before_handlers(app)
    configure_uploads(app, (photos,))
    register_blueprints(app)
    return app


def configure_extensions(app):
    db.init_app(app)
    mail.init_app(app)


def configure_i18n(app):

    babel = Babel(app)

    @babel.localeselector
    def get_locale():
        accept_languages = app.config.get('ACCEPT_LANGUAGES',['en','zh'])
        return request.accept_languages.best_match(accept_languages)


def configure_identity(app):
    principal = Principal(app)
    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        g.user = User.query.from_identity(identity)


def configure_before_handlers(app):
    @app.before_request
    def authenticate():
        g.user = getattr(g.identity, 'user', None)


def configure_errorhandlers(app):

    @app.errorhandler(401)
    def unauthorized(error):
        if request.is_xhr:
            return jsonify(error="Login required")
        flash("Please login to see this page", "error")
        return redirect(url_for("home.index", next=request.path))

    @app.errorhandler(403)
    def forbidden(error):
        if request.is_xhr:
            return jsonify(error='Sorry, page not allowed')
        return render_template("errors/403.html", error=error)

    @app.errorhandler(404)
    def page_not_found(error):
        if request.is_xhr:
            return jsonify(error='Sorry, page not found')
        return render_template("errors/404.html", error=error)

    @app.errorhandler(500)
    def server_error(error):
        if request.is_xhr:
            return jsonify(error='Sorry, an error has occurred')
        return render_template("errors/500.html", error=error)


def register_blueprints(app):
    from views import home
    from views import user
    from views import admin
    app.register_blueprint(user)
    app.register_blueprint(home)
    app.register_blueprint(admin)
