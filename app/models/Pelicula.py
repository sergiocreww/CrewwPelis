from app import db

class Pelicula(db.Model):
    __tablename__ =  "pelicula"
    idPelicula = db.Column(db.Integer, primary_key=True)
    NombrePelicula = db.Column(db.String(50), nullable=False)
    GeneroPelicula_idGeneroPelicula = db.Column(db.Integer, db.ForeignKey('genero.idGenero'))

    favoritos = db.relationship('Favorito', backref='pelicula', lazy=True)