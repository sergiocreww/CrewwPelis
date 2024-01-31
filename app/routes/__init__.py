from flask import Blueprint

bp = Blueprint('main', __name__)

from app.routes import Favorito_routes, GeneroPelicula_routes, Pelicula_routes, Usuario_routes