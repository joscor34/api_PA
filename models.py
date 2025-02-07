# SQL -> Querys
# El traductor de python a sql es la herramienta SQLAlchemy
from extensions import db_s

# Vamos a importar el módulo para hashear las contraseñas
from werkzeug.security import check_password_hash, generate_password_hash

# generate_password_hash recibe un texto y lo hashea en una serie de caracteres
# con longitud igual en todos casos


# check_password_hash recibe dos datos:
# 1.- El hash que está en la base de datos
# 2.- Contraseña que el usuario escribió



# Vamos a crear un modelo
# Un modelo es una plano de como se ve la tabla en sql
class Usuario(db_s.Model):
  __tablename__ = 'usuarios'
  id = db_s.Column(db_s.Integer, primary_key=True)
  name = db_s.Column(db_s.String(120), nullable=False)
  email  = db_s.Column(db_s.String(80), nullable=False)
  password = db_s.Column(db_s.String, nullable=False)


  # Tenemos el método para cifrar las contraseña
  def hashear_password(self, password_original):
    self.password = generate_password_hash(password_original)


  def verificar_password(self, password_plano):
    return check_password_hash(self.password, password_plano)

    
  def save(self):
    # Creamos una conexión con la base de datos para añadir información
    db_s.session.add(self)

    # Nos aseguramos de que los cambios se hagan
    db_s.session.commit()

  def delete(self):
    db_s.session.delete(self)

    # Nos aseguramos de que los cambios se guarden
    db_s.session.commit()