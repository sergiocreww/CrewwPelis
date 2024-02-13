from app import db

class Usuario(db.Model):
    __tablename__ =  "usuario"
    idUsuario = db.Column(db.Integer, primary_key=True)
    NombreUsuario = db.Column(db.String(50), nullable=False)
    ContrasenaUsuario = db.Column(db.String(256), nullable=False)
    Rol_idRol = db.Column(db.Integer, db.ForeignKey('rol.idRol'))
    
    favoritos = db.relationship('Favorito', backref='usuario', lazy=True)