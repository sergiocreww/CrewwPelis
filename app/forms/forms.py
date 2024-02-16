from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FileField, SubmitField
from wtforms.validators import DataRequired
from app.models.GeneroPelicula import Genero  # Asegúrate de importar la clase Genero desde tus modelos

class PeliculaForm(FlaskForm):
    NombrePelicula = StringField('Nombre de la Película', validators=[DataRequired()])
    
    # Cambiamos IntegerField por SelectField para el género
    GeneroPelicula_idGeneroPelicula = SelectField('Género', coerce=int, validators=[DataRequired()])

    # Cambiamos FileField a StringField para almacenar el nombre del archivo
    Imagen = StringField('Imagen de la Película', validators=[DataRequired()])

    submit = SubmitField('Insertar Película')

    def __init__(self, *args, **kwargs):
        super(PeliculaForm, self).__init__(*args, **kwargs)

        # Populate choices for GeneroPelicula_idGeneroPelicula with genre names
        self.GeneroPelicula_idGeneroPelicula.choices = [(g.idGenero, g.NombreGenero) for g in Genero.query.all()]

