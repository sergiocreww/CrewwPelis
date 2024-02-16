from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from app.models.Pelicula import Pelicula
from app.models.GeneroPelicula import Genero 
from app.forms.forms import PeliculaForm 
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



@bp.route('/insertar_pelicula', methods=['GET', 'POST'])
def insertar_pelicula():
    form = PeliculaForm()

    if form.validate_on_submit():
        nueva_pelicula = Pelicula(
            NombrePelicula=form.NombrePelicula.data,
            GeneroPelicula_idGeneroPelicula=form.GeneroPelicula_idGeneroPelicula.data,
            Imagen=form.Imagen.data
        )
        db.session.add(nueva_pelicula)
        db.session.commit()
        flash('Pelicula insertada correctamente', 'success')
        return render_template('Usuarios/index2.html')

    return render_template('Peliculas/Agregar.html', form=form)




  




