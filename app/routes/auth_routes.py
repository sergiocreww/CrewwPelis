# auth_routes.py
from run import app
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, login_required, current_user, logout_user
from flask_login import LoginManager
from app.models import Usuario

login_manager = LoginManager(app)

auth_bp = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(idUsuario):
    user = Usuario.query.get(int(idUsuario))
    return user

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre_usuario = request.form.get('nombre_usuario')
        contrasena = request.form.get('contrasena')

        usuario = Usuario.query.filter_by(NombreUsuario=nombre_usuario, ContrasenaUsuario=contrasena).first()

        if usuario:
            login_user(usuario)
            return redirect(url_for('auth.dashboard'))

    return render_template('Usuarios/login.html')

@auth_bp.route('/dashboard')
@login_required
def dashboard():
    return f'Bienvenido, {current_user.NombreUsuario}! Esta es tu página de inicio.'

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
