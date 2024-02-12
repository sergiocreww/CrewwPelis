from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config') 
    
    db.init_app(app)

    from app.routes import Favorito_routes, GeneroPelicula_routes, Pelicula_routes, Usuario_routes, Login_routes 
    app.register_blueprint(Favorito_routes.bp)
    app.register_blueprint(GeneroPelicula_routes.bp)
    app.register_blueprint(Pelicula_routes.bp)
    app.register_blueprint(Usuario_routes.bp)
    app.register_blueprint(Login_routes.bp)

    return app