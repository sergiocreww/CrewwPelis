from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Favorito import Favorito
from app import db

bp = Blueprint('favorito', __name__)