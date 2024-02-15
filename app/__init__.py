from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config') 
    app.secret_key = secrets.token_hex(16)  
    login_manager = LoginManager(app)
    login_manager.init_app(app)

    
    db.init_app(app)

    from app.routes import Favorito_routes, GeneroPelicula_routes, Pelicula_routes, Usuario_routes
    app.register_blueprint(Favorito_routes.bp)
    app.register_blueprint(GeneroPelicula_routes.bp)
    app.register_blueprint(Pelicula_routes.bp)
    app.register_blueprint(Usuario_routes.bp)


    return app