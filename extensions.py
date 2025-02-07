# Este archivo nos ayudará a evitar las importaciones circulares

from flask_sqlalchemy import SQLAlchemy

# creamos un objeto de tipo SQLAlchemy que va a controlar toda la base de datos
db_s = SQLAlchemy()