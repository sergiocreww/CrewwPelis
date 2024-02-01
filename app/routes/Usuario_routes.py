from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Usuario import Usuario
from app import db

bp = Blueprint('usuario', __name__)

@bp.route('/')
def index():
    data = Usuario.query.all()
    #return render_template('index.html', data=data)
    return "entra al index"


@bp.route('/Usuario/Registro', methods=['GET', 'POST'])
def Registro():
    if request.method == 'POST':
        NombreUsuario = request.form['Nombre']
        ContrasenaUsuario = request.form['Contrasena']

        new_usuario = Usuario(NombreUsuario=NombreUsuario, ContrasenaUsuario=ContrasenaUsuario)
        db.session.Registro(new_usuario)
        db.session.commit()
 
        return redirect(url_for('usuario.Registro'))
    
    return render_template('Usuarios/Registro.html')



