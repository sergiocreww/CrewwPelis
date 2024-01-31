from app import db

class Favorito(db.Model):
    idFavorito = db.Column(db.Integer, primary_key=True)
    Pelicula_idPelicula = db.Column(db.Integer, foreing_key=True)
    Usuario_idUsuario = db.Column(db.Integer, foreing_key=True)