from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Pelicula import Pelicula
from app import db
import os

bp = Blueprint('pelicula', __name__)

@bp.route('/peliculas')
def mostrar_peliculas():
    # Obtener todas las películas desde la base de datos
    peliculas = Pelicula.query.all()

    # Iterar sobre las películas e imprimir información (puedes cambiar esto por renderizar en HTML)
    for pelicula in peliculas:
        print(f"ID: {pelicula.idPelicula}, Título: {pelicula.NombrePelicula}, Género: {pelicula.GeneroPelicula_idGeneroPelicula}")

    # Renderizar una plantilla HTML que muestre la información de las películas
    return render_template('Peliculas/VerPelicula.html', peliculas=peliculas)




  




