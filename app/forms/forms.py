from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField, SubmitField
from wtforms.validators import DataRequired

class PeliculaForm(FlaskForm):
    NombrePelicula = StringField('Nombre de la Película', validators=[DataRequired()])
    GeneroPelicula_idGeneroPelicula = IntegerField('ID del Género', validators=[DataRequired()])
    Imagen = FileField('Imagen de la Película', validators=[DataRequired()])
    submit = SubmitField('Insertar Película')
