from app import db
from flask_login import UserMixin 

class Usuario(UserMixin, db.Model):
    __tablename__ =  "usuario"
    idUsuario = db.Column(db.Integer, primary_key=True)
    NombreUsuario = db.Column(db.String(50), nullable=False)
    ContrasenaUsuario = db.Column(db.String(256), nullable=False)
    Rol = db.Column(db.String(20), nullable=False, default="Usuario")

    def __repr__(self):
        return f"Usuario('{self.NombreUsuario}', '{self.Rol}')"    
    
    favoritos = db.relationship('Favorito', backref='usuario', lazy=True)

    def get_id(self):
        return str(self.idUsuario)