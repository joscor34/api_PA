# Este archivo nos ayudará a evitar las importaciones circulares

from flask_sqlalchemy import SQLAlchemy


# JWTManager es una clase que a través de atributos y de métodos
# controla los procesos para generar JWTs y utilizarlos
from flask_jwt_extended import JWTManager

# creamos un objeto de tipo SQLAlchemy que va a controlar toda la base de datos
db_s = SQLAlchemy()

# Creamos un objeto de esa clase
jwt = JWTManager()