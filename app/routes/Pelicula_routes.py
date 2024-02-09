from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Pelicula import Pelicula
from app import db
import os

bp = Blueprint('pelicula', __name__)

@bp.route('/Pelicula/VerPelicula', methods=['GET', 'POST'])
def Upload():
    if request.method == 'POST':     
 
         return redirect(url_for('pelicula.Upload'))
    
    return render_template('Peliculas/VerPelicula.html')
  




