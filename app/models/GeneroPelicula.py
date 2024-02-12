from app import db
#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:c1E3g4HC25h2CA5HHgedDd6D6-f6DE3H@monorail.proxy.rlwy.net:29549/peliculas'  # Cambia esto según tu configuración de base de datos
#db = SQLAlchemy(app)

class Genero(db.Model):
    __tablename__ = "genero"
    idGenero = db.Column(db.Integer, primary_key=True)
    NombreGenero = db.Column(db.String(50), nullable=False)

