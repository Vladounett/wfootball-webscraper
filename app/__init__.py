from flask import Flask, render_template
from . import routes, routes_leagues

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes.bp)
    app.register_blueprint(routes_leagues.bp)
    return app