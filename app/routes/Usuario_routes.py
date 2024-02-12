from flask import Flask, Blueprint, render_template, request, redirect, url_for, session
from flask_bcrypt import generate_password_hash
from app.models.Usuario import Usuario
from app import db

bp = Blueprint('usuario', __name__)

@bp.route('/Index')
def index():
    data = Usuario.query.all()
    return render_template('Usuarios/index2.html', data=data)
    #return "entra al index"


@bp.route('/Usuario/Registro', methods=['GET', 'POST'])
def Registro():
    if request.method == 'POST':
        NombreUsuario = request.form['Nombre']
        ContrasenaUsuario = request.form['Contrasena']

        new_usuario = Usuario(NombreUsuario='Nombre', ContrasenaUsuario=generate_password_hash('Contrasena'))
        db.session.add(new_usuario)
        db.session.commit()
 
        return redirect(url_for('usuario.Registro'))
    
    return render_template('Usuarios/Registro.html')








