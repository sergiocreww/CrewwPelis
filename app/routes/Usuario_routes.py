from flask import Flask, Blueprint, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from app.models.Usuario import Usuario
from app import db


bp = Blueprint('usuario', __name__)

login_manager = LoginManager()


@bp.route('/Index')
def index():
    data = Usuario.query.all()
    return render_template('Usuarios/index2.html', data=data)

@bp.route('/Usuario/Registro', methods=['GET', 'POST'])
def Registro():
    if request.method == 'POST':
        NombreUsuario = request.form['Nombre']
        ContrasenaUsuario = request.form['Contrasena']

        # Utiliza las variables obtenidas de la solicitud en lugar de cadenas constantes
        hashed_password = generate_password_hash(ContrasenaUsuario)
        new_usuario = Usuario(NombreUsuario=NombreUsuario, ContrasenaUsuario=hashed_password)
        db.session.add(new_usuario)
        db.session.commit()

        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return render_template('Usuarios/Login.html')

    return render_template('Usuarios/Registro.html')

@bp.route('/Usuario/IniciarSesion', methods=['GET', 'POST'])
def IniciarSesion():
    if request.method == 'POST':
        NombreUsuario = request.form['Nombre']
        ContrasenaUsuario = request.form['Contrasena']

        usuario = Usuario.query.filter_by(NombreUsuario=NombreUsuario).first()

        if usuario and check_password_hash(usuario.ContrasenaUsuario, ContrasenaUsuario):
            login_user(usuario)
            session['rol'] = Usuario.Rol
            flash('Inicio de sesión exitoso.', 'success')
            session['user_id'] = usuario.idUsuario 
            session['user_username'] = usuario.NombreUsuario
            return render_template('Usuarios/index2.html')
        else:
            flash('Credenciales incorrectas. Inténtalo de nuevo.', 'danger')
            return render_template('Usuarios/Login.html')

    return render_template('Usuarios/Login.html')

@bp.route('/admin_dashboard')
def admin_dashboard():
    # Verificar si el usuario tiene el rol de Administrador
    if 'rol' in session and session['rol'] == 'Administrador':
        return render_template('Usuarios/index2.html')
    else:
        flash('Acceso no autorizado', 'error')
        return render_template('Usuarios/index2.html')


@bp.route('/Usuario/CerrarSesion')
@login_required
def CerrarSesion():
    logout_user()
    flash('Cierre de sesión exitoso.', 'success')
    return redirect(url_for('usuario.index2'))


 

