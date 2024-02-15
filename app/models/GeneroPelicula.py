from app import db

class Genero(db.Model):
    __tablename__ = "genero"
    idGenero = db.Column(db.Integer, primary_key=True)
    NombreGenero = db.Column(db.String(50), nullable=False)

