from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from app.models.Pelicula import Pelicula
from app.models.GeneroPelicula import Genero
from app.models.Usuario import Usuario 
from app import db
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
    generos = Genero.query.all()
    peliculas = Pelicula.query.all()
    return render_template('Usuarios/index2.html', peliculas=peliculas, generos=generos)



@bp.route('/ver_pelicula_externa', methods=['GET'])
def ver_pelicula_externa():
    # Obtener el nombre de la película desde los parámetros de la solicitud
    nombre_pelicula = request.args.get('NombrePelicula')

    # Verificar si el nombre de la película no es None
    if nombre_pelicula is not None and nombre_pelicula.strip():
        # Obtener el nombre de la película desde la base de datos (por ejemplo, usando SQLAlchemy)
        pelicula = Pelicula.query.filter_by(NombrePelicula=nombre_pelicula).first()

        # Verificar si se encontró la película en la base de datos
        if pelicula:
            # Formatear el nombre de la película según tus requisitos (minúsculas y guiones bajos)
            nombre_pelicula_formateado = (
            pelicula.NombrePelicula.lower()
            .replace(' ', '-')
            .replace(':', '-')
        )
            # Construir la URL de la página web externa con el nombre de la película formateado
            url_externa = f'https://www.tokyvideo.com/es/video/{nombre_pelicula_formateado}'

            # Redirigir a la página web externa
            return redirect(url_externa)
        else:
            return "Error: Película no encontrada en la base de datos."
    else:
        # Manejar el caso en que el nombre de la película sea None o una cadena vacía
        return "Error: Nombre de película no proporcionado o inválido."

# Resto de tus rutas y funciones...






@bp.route('/insertar_pelicula', methods=['GET', 'POST']) 
def insertar_pelicula():
    from app import create_app
    app = create_app()

    if request.method == 'POST': 
            NombrePelicula = request.form['NombrePelicula']
            GeneroPelicula_idGeneroPelicula = request.form['GeneroPelicula'] 

            imagen = request.files['ImagenPelicula']

            if imagen:
                 filename = secure_filename(imagen.filename)
                 imagen.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                 ruta_imagen = filename
            else:
                 ruta_imagen = 'static/images/defaul.jpg'

            new_pelicula = Pelicula(NombrePelicula=NombrePelicula, GeneroPelicula_idGeneroPelicula=GeneroPelicula_idGeneroPelicula, Imagen=ruta_imagen)
            db.session.add(new_pelicula)
            db.session.commit()

            return redirect(url_for('usuario.index'))
    generos= Genero.query.all()
    return render_template('Peliculas/Agregar.html', generos = generos)


@bp.route('/EliminarPelicula', methods=['GET'])
def editar_eliminar_pelicula():
    peliculas = Pelicula.query.all()
    return render_template('Peliculas/EditarEliminar.html', peliculas=peliculas)

@bp.route('/procesar_edicion_eliminacion', methods=['POST'])
def procesar_edicion_eliminacion():
    peliculas_seleccionadas = request.form.getlist('seleccionadas')

    if len(peliculas_seleccionadas) == 1:
        return redirect(url_for('pelicula.editar_pelicula', idPelicula=peliculas_seleccionadas[0]))
    elif len(peliculas_seleccionadas) > 1:
        for idPelicula in peliculas_seleccionadas:
            pelicula = Pelicula.query.get_or_404(idPelicula)
            db.session.delete(pelicula)
        db.session.commit()
        flash('Películas eliminadas correctamente', 'success')

    return redirect(url_for('pelicula.editar_eliminar_pelicula'))

@bp.route('/eliminar_pelicula', methods=['POST'])
def eliminar_pelicula():
    peliculas_seleccionadas = request.form.getlist('seleccionadas')

    for idPelicula in peliculas_seleccionadas:
        pelicula = Pelicula.query.get_or_404(idPelicula)
        db.session.delete(pelicula)
    db.session.commit()
    flash('Películas eliminadas correctamente', 'success')

    return redirect(url_for('pelicula.editar_eliminar_pelicula'))
    







