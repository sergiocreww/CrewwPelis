from app import create_app, db
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.routes.auth_routes import auth_bp
import os


app = create_app()
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:c1E3g4HC25h2CA5HHgedDd6D6-f6DE3H@monorail.proxy.rlwy.net:29549/peliculas'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

app.register_blueprint(auth_bp, url_prefix='/auth')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))