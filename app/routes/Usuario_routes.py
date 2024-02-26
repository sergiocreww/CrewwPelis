from flask import Flask, Blueprint, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt, generate_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from app.models.Pelicula import Pelicula
from app.models.GeneroPelicula import Genero
from app.models.Usuario import Usuario
from app import db
app = Flask(__name__)

bp = Blueprint('usuario', __name__)

login_manager = LoginManager()
app = Flask(__name__)
bcrypt=Bcrypt(app) 

# Esta función verifica si un usuario ha iniciado sesión
def verificar_sesion():
    return current_user.is_authenticated

@bp.route('/Index')
def index():
    peliculas = Pelicula.query.all()
    generos = Genero.query.all()
    if verificar_sesion():
        return render_template('Usuarios/index2.html', Usuario=current_user, peliculas=peliculas, generos=generos)
    else:   
        data = Usuario.query.all()
        return render_template('Usuarios/index2.html', data=data)

@bp.route('/Usuario/Registro', methods=['GET', 'POST'])
def Registro():
    if request.method == 'POST':
        NombreUsuario = request.form['Nombre']
        ContrasenaUsuario = request.form['Contrasena']

        # Utiliza las variables obtenidas de la solicitud en lugar de cadenas constantes
        hashed_password = generate_password_hash(ContrasenaUsuario).decode('utf-8')
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

        if not NombreUsuario or not ContrasenaUsuario:
            flash('Todos los campos son obligatorios', 'error')
            return render_template('Usuarios/Login.html') 

        usuario = Usuario.query.filter_by(NombreUsuario=NombreUsuario).first()

        if usuario:
            if bcrypt.check_password_hash(usuario.ContrasenaUsuario, ContrasenaUsuario):
                login_user(usuario)
                session['idUsuario'] = usuario.idUsuario
                session['NombreUsuario'] = usuario.NombreUsuario
                session['Rol'] = usuario.Rol_idRol

                flash('Inicio de Sesion Exitoso', 'succes')
                return redirect(url_for('usuario.index'))
            else:
                flash('Usuario o Contrasenas Incorrectas', 'error')
    if current_user.is_authenticated:
        return redirect(url_for('usuario.index'))
    return render_template('Usuarios/Login.html')

@bp.route('/admin_dashboard')
def admin_dashboard():
    # Verificar si el usuario tiene el rol de Administrador
    if current_user.is_authenticated and current_user.Rol == 'Administrador':
        return render_template('Usuarios/index2.html')
    else:
        flash('Acceso no autorizado', 'error')
        return render_template('Usuarios/index2.html')


@bp.route('/Usuario/CerrarSesion')
@login_required
def CerrarSesion():
    logout_user()
    session.clear()  # Limpiar la sesión manualmente
    flash('Cierre de sesión exitoso.', 'success')
    return redirect(url_for('usuario.index'))


@bp.route('/usuario/<int:idUsuario>', methods=['GET'])
def mostrar_usuario(idUsuario):
    usuarios = Usuario.query.all()
    usuario_seleccionado = Usuario.query.get_or_404(idUsuario)
    return render_template('Usuarios/ModificarUsuario.html', usuarios=usuarios, usuario_seleccionado=usuario_seleccionado)


@bp.route('/modificar_eliminar_usuario', methods=['POST'])
def modificar_eliminar_usuario():
    id_usuario_seleccionado = request.form.get('usuario')
    nuevo_rol = request.form.get('nuevo_rol')
    accion = request.form.get('accion')

    if id_usuario_seleccionado:
        usuario = Usuario.query.get_or_404(int(id_usuario_seleccionado))

        if accion == 'guardar_cambios':
            # Modificar el rol
            if nuevo_rol:
                usuario.rol = nuevo_rol
                db.session.commit()
                flash('Rol del usuario modificado correctamente', 'success')
            else:
                flash('No se proporcionó un nuevo rol', 'warning')

        elif accion == 'eliminar':
            # Eliminar el usuario
            db.session.delete(usuario)
            db.session.commit()
            flash('Usuario eliminado correctamente', 'success')

    else:
        flash('Por favor, selecciona un usuario antes de realizar la acción.', 'warning')

    return redirect(url_for('usuario.mostrar_usuario', idUsuario=id_usuario_seleccionado))






 

