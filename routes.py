# Este archivo va a almacenar única y exclusivamente rutas de nuestro servidor
from flask import Flask, render_template, request, redirect, url_for, make_response

from methods import crear_cuenta, iniciar_sesion, encontrar_todos_los_usuarios

def cargar_rutas(app):
# Este bloque de código es la base para todas rutas
  @app.route('/')
  def pagina():
    # Buscamos todos los datos en la tabla "usuarios"

    return render_template('index.html')

  # Esta es otra ruta
  @app.route('/login')
  def informacion_jose():

    resultado = request.args.get('status')

    return render_template('login.html', estado=resultado)

  # Esta es otra ruta
  @app.route('/signup')
  def datos():

    resultado = request.args.get('status') 

    return render_template('signup.html', estado=resultado)

  # Esta ruta va a manejar la información
  # Este método solo funcionará para el inicio de sesión
  @app.route('/manipulacion', methods=['POST'])
  def manipular_datos():
    correo = request.form.get('email')
    password = request.form.get('password')

    print(f'''
      Correo: {correo}
      Contraseña: {password}
  ''')

    respuesta_login = iniciar_sesion(correo, password)


    if respuesta_login['status'] == 'error':
      return redirect(url_for('informacion_jose', status=respuesta_login['status']))

    # Si lo de arriba no se cumple, significa que tenemos un token
    respuesta = make_response(redirect(url_for('pagina')))

    respuesta.set_cookie('access_token', respuesta_login['token'], secure=True, max_age=3600)

    return respuesta

  # Interceptamos la información del Sign Up del usuario
  @app.route('/datos_crear_cuenta', methods=['POST'])
  def obtener_datos_cuenta():
    nombre = request.form.get('name')
    correo = request.form.get('email')
    password = request.form.get('password')

    print(f'''
    nombre: {nombre}
    correo: {correo}
    passoword: {password}
  ''')
    
    respuesta_signup = crear_cuenta(nombre, correo, password)

    print(respuesta_signup)

    if respuesta_signup['status'] == 'error':
      return redirect(url_for('datos', status=respuesta_signup['status']))

    return redirect(url_for('pagina', status=respuesta_signup['status']))
  



  @app.route('/error')
  def pantalla_error():
    return render_template('error.html')