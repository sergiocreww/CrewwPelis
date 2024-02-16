from app import db
from flask_login import UserMixin 

class Usuario(UserMixin, db.Model):
    __tablename__ =  "usuario"
    idUsuario = db.Column(db.Integer, primary_key=True)
    NombreUsuario = db.Column(db.String(50), nullable=False)
    ContrasenaUsuario = db.Column(db.String(256), nullable=False)
    Rol_idRol = db.Column(db.Integer, db.ForeignKey('rol.idRol'))
    Rol = db.Column(db.String(20), nullable=False, default="Usuario")
    
    favoritos = db.relationship('Favorito', backref='usuario', lazy=True)

    def get_id(self):
        return str(self.idUsuario)