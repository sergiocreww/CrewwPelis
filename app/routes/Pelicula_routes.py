from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from app.models.Pelicula import Pelicula
from app.models.GeneroPelicula import Genero 
from app import db
from app.forms.forms import PeliculaForm
import os
import app

from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




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

    form.GeneroPelicula_idGeneroPelicula.choices = [(g.idGenero, g.NombreGenero) for g in Genero.query.all()]

    if form.validate_on_submit():
        nombre_pelicula = form.NombrePelicula.data
        genero_id = form.GeneroPelicula_idGeneroPelicula.data

        imagen = form.Imagen.data

        if imagen and allowed_file(imagen.filename):
            filename = secure_filename(imagen.filename)

            # Guardar la imagen de forma segura en el sistema de archivos
            ruta_imagen = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            imagen.save(ruta_imagen)

            # Almacenar el nombre del archivo en la base de datos
            nueva_pelicula = Pelicula(
                NombrePelicula=nombre_pelicula,
                GeneroPelicula_idGeneroPelicula=genero_id,
                Imagen=filename  # Guardar el nombre del archivo, no la ruta completa
            )

            db.session.add(nueva_pelicula)
            db.session.commit()

            flash('Película insertada correctamente', 'success')
            return render_template('Peliculas/Agregar.html')

    return render_template('Peliculas/Agregar.html', form=form)





  




