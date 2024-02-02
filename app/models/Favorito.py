from app import db

class Favorito(db.Model):
    __tablename__ =  "favorito"
    idFavorito = db.Column(db.Integer, primary_key=True)
    Pelicula_idPelicula = db.Column(db.Integer, db.ForeignKey('pelicula.idPelicula'))
    Usuario_idUsuario = db.Column(db.Integer, db.ForeignKey('usuario.idUsuario'))