# auth_blueprint.py

from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from app.models.Usuario import Usuario  # Ajusta la importación según tu estructura de archivos

bp = Blueprint('login', __name__)
bcrypt = Bcrypt()

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        NombreUsuario = request.form.get('nombre_usuario')
        ContrasenaUsuario = request.form.get('contrasena')
        usuario = Usuario.query.filter_by(NombreUsuario=NombreUsuario).first()

        if usuario and bcrypt.check_password_hash(usuario.ContrasenaUsuario, ContrasenaUsuario):
            login_user(usuario)
            return redirect(url_for('login.protected'))

    return render_template('Usuarios/Login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index2'))

@bp.route('/protected')
@login_required
def protected():
    return render_template('protected.html')
