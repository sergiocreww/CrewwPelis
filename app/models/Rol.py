from app import db

class Rol(db.Model):
    idRol = db.Column(db.Integer, primary_key=True)
    NombreRol = db.Column(db.String(45), nullable=True)