from app import db

class Pelicula(db.Model):
    idPelicula = db.Column(db.Integer, primary_key=True)
    NombrePelicula = db.Column(db.String(50), nullable=False)
    GeneroPelicula_idGeneroPelicula = db.Column(db.Integer, db.ForeignKey('Genero.idGenero'))