from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Pelicula import Pelicula
from app import db
import os

bp = Blueprint('pelicula', __name__)

@bp.route('/Pelicula/VerPelicula', methods=['GET', 'POST'])
def Upload():
 
         return redirect(url_for('pelicula.Upload'))

  




