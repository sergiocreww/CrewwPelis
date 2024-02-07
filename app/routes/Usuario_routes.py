from flask import Flask, Blueprint, render_template, request, redirect, url_for, session
from app.models.Usuario import Usuario
from app import db

bp = Blueprint('usuario', __name__)

@bp.route('/')
def index():
    data = Usuario.query.all()
    return render_template('Usuarios/index2.html', data=data)
    #return "entra al index"


@bp.route('/Usuario/Registro', methods=['GET', 'POST'])
def Registro():
    if request.method == 'POST':
        NombreUsuario = request.form['Nombre']
        ContrasenaUsuario = request.form['Contrasena']

        new_usuario = Usuario(NombreUsuario=NombreUsuario, ContrasenaUsuario=ContrasenaUsuario)
        db.session.add(new_usuario)
        db.session.commit()
 
        return redirect(url_for('usuario.Registro'))
    
    return render_template('Usuarios/Registro.html')

@bp.route('/Usuario/Login', methods=['GET' , 'POST'])
def Login():
    if request.method == 'POST':
        NombreUsuario = request.form['Nombre']
        ContrasenaUsuario = request.form['Contrasena']

        usuario = Usuario.query.filter_by(NombreUsuario=NombreUsuario, ContrasenaUsuario=ContrasenaUsuario).first()

        if usuario:
            # Iniciar sesión y redirigir a la página principal (o a donde desees)
            session['idUsuario'] = usuario.idUsuario
            return render_template('Usuarios/index2.html')
        else:
            # Mostrar un mensaje de error si las credenciales son incorrectas
            error = 'Credenciales incorrectas. Inténtalo de nuevo.'
            return render_template('Usuarios/Registro.html', error=error)




