from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from app.models.Pelicula import Pelicula
from app.models.GeneroPelicula import Genero 
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
    peliculas = Pelicula.query.all()
    # Renderizar una plantilla HTML que muestre la información de las películas
    return render_template('Usuarios/index2.html', peliculas=peliculas)



@bp.route('/insertar_pelicula', methods=['GET', 'POST']) 
def insertar_pelicula():
    from app import create_app
    app = create_app

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

            new_pelicula = Pelicula(NombrePelicula=NombrePelicula, GeneroPelicula_idGeneroPelicula=GeneroPelicula_idGeneroPelicula, imagen=ruta_imagen)
            db.session.add(new_pelicula)
            db.session.commit()

            return redirect(url_for('usuario.index'))
    generos= Genero.query.all()
    return render_template('Peliculas/Agregar.html', generos = generos)



@bp.route('/buscar_pelicula_por_id/<int:id_pelicula>', methods=['GET', 'POST'])
def buscar_pelicula_por_id(id_pelicula):
    # Buscar la película en la base de datos por su ID
    pelicula = Pelicula.query.get(id_pelicula)

    if pelicula:
        # Devolver la información de la película en formato JSON (puedes cambiar esto según tus necesidades)
        return jsonify({
            'idPelicula': pelicula.idPelicula,
            'NombrePelicula': pelicula.NombrePelicula,
            'GeneroPelicula_idGeneroPelicula': pelicula.GeneroPelicula_idGeneroPelicula,
            'Imagen': pelicula.Imagen
        })
    else:
        # Si no se encuentra la película, devolver un mensaje de error
        return jsonify({'error': 'Película no encontrada'}), 404





  




