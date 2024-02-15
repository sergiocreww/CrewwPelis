from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.GeneroPelicula import Genero
from app import db

bp = Blueprint('genero', __name__)

@bp.route('/')
def index():
    generos = Genero.query.all()
    return render_template('Usuarios/index2.html', generos=generos)
