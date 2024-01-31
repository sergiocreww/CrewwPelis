from app import db

class GeneroPelicula(db.Model):
    idGeneroPelicula = db.Column(db.Integer, primary_key=True)
    NombreGenero = db.Column(db.String(50), nullable=False)