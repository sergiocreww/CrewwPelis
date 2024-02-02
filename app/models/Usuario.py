from app import db

class Usuario(db.Model):
<<<<<<< HEAD
    __tablename__ =  "usuario"
=======
    __tablename__ = "usuario"
>>>>>>> ae0bc9fdd88f2714af209493c1f3e71242d62278
    idUsuario = db.Column(db.Integer, primary_key=True)
    NombreUsuario = db.Column(db.String(50), nullable=False)
    ContrasenaUsuario = db.Column(db.String(20), nullable=False)
    Rol_idRol = db.Column(db.Integer, db.ForeignKey('rol.idRol'))
    
    favoritos = db.relationship('Favorito', backref='usuario', lazy=True)