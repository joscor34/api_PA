from models import Usuario

from extensions import jwt
from flask_jwt_extended import create_access_token

# Un archivo que contiene todas las acciones
# que un usario pueda realizar

# Necesitamos un método para que el usuario pueda crear un cuenta
def crear_cuenta(nombre, correo, password):
    # Creamos un objeto de tipo usuario que contendrá la información para la db

    usuario_existente = Usuario.query.filter_by(email=correo).first()

    # Revisamos si lo que regresa esa query es diferente a None
    if usuario_existente is not None:
        print('El correo ya existe en la db')
        return {'status': 'error', 'error': 'La cuenta ya está registrada'}


    # Esto solo se ejecuta si en la db no existe la cuenta que el usuario
    # está registrando

    nuevo_usuario = Usuario(name=nombre, email=correo)

    nuevo_usuario.hashear_password(password_original=password)

    # Guardamos este nuevo objeto en la db
    nuevo_usuario.save()

    return {'status': 'ok', 'email':correo}


def iniciar_sesion(correo, password):

    # Que contenga usuarios filtrados a través de un parametro
    usuarios_existentes = Usuario.query.filter_by(email=correo).first()
    
    # 1.- Si el usuario existe, entonces puede iniciar sesión

    # 2.- Si el usuario no existe en la db no puede iniciar sesion

    # Si el usuario no existe
    if usuarios_existentes is None:
        print('La cuenta no existe')
        return {'status': 'error', 'error':'La cuenta no existe'}


    # Si la contraseña del formulario es la de la DB
    if usuarios_existentes.verificar_password(password_plano = password):
        print('Inicio de sesión exitoso :D')
        toke_de_acceso = create_access_token(identity=usuarios_existentes.name)
        print(toke_de_acceso)
        return {'status':'ok', 'token': toke_de_acceso}

    
    # Si el usuario existe, pero la contraseña no coincide, entramos en else
    else:
        print('La contraseña es incorrecta')
        return {'status':'error', 'error':'Contraseña incorrecta :('}


def encontrar_todos_los_usuarios():

    # Creamos una variable que contendrá la respuesta de nuestra DB
    usuarios = Usuario.query.all()

    print(usuarios)

    return usuarios