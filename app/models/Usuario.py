from app import db

class Usuario(db.Model):
    idUsuario = db.Column(db.Integer, primary_key=True)
    NombreUsuario = db.Column(db.String(50), nullable=False)
    ContrasenaUsuario = db.Column(db.String(20), nullable=False)
    Rol_idRol = db.Column(db.Integer, foreing_key=True)