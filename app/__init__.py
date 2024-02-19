from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import secrets
from flask_login import LoginManager
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config') 
    migrate = Migrate(app, db)
    app.secret_key = secrets.token_hex(16) 
    login_manager = LoginManager() 
    login_manager.init_app(app)

    app.config['UPLOAD_FOLDER'] = './app/static/images'

    @login_manager.user_loader
    def load_user(idUsuario):
        from app.models.Usuario import Usuario
        return Usuario.query.get(int(idUsuario))    

    
    db.init_app(app)

    from app.routes import Favorito_routes, GeneroPelicula_routes, Pelicula_routes, Usuario_routes
    app.register_blueprint(Favorito_routes.bp)
    app.register_blueprint(GeneroPelicula_routes.bp)
    app.register_blueprint(Pelicula_routes.bp)
    app.register_blueprint(Usuario_routes.bp)


    return app