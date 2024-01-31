from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

from sqlalchemy import Column, Integer, String
from .declarative_base import Base

class Usuario(Base):
    __tablename__ = 'Usuario'
    idUsuario = Column(Integer, primary_key=True)
    NombreUsuario = Column(String)
    ContrasenaUsuario = Column(String)

class Pelicula(Base):
    __tablename__ = 'Pelicula'
    idPelicula = Column(Integer, primary_key=True)
    NombrePelicula = Column(String)
    GeneroPelicula_idGeneroPelicula = Column(String, ForeignKey('GeneroPelicula_idGeneroPelicula.idGeneroPelicula'))   

class GeneroPelicula(Base):
    idGeneroPelicula = Column(Integer, primary_key=True)
    NombreGenero = Column(String)

class Favorito(Base):
    idFavorito = Column(Integer, primary_key=True) 
    Pelicula_idPelicula = Column(Integer, foreing_key=True)
    Usuario_idUsuario = Column(Integer,foreing_key=True)


engine = create_engine('mysql://root:c1E3g4HC25h2CA5HHgedDd6D6-f6DE3H@monorail.proxy.rlwy.net:29549/Crewwpelis')