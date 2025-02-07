# Este archivo va a almacenar única y exclusivamente rutas de nuestro servidor
from flask import Flask, render_template, request, redirect, url_for

from methods import crear_cuenta, iniciar_sesion

def cargar_rutas(app):
# Este bloque de código es la base para todas rutas
  @app.route('/')
  def pagina():
    return render_template('index.html')

  # Esta es otra ruta
  @app.route('/login')
  def informacion_jose():
    return render_template('login.html')

  # Esta es otra ruta
  @app.route('/signup')
  def datos():
    return render_template('signup.html')

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

    iniciar_sesion()

    return redirect(url_for('pagina'))

  # Interceptamos la información del Sign Up del usuario
  @app.route('/datos_crear_cuenta', methods=['POST'])
  def obtener_datos_cuenta():
    nombre = request.form.get('name')
    correo = request.form.get('email')
    password = request.form.get('password')

    print(f'''
    nombre: {nombre}
    correo: {correo}
    passowrdo: {password}
  ''')
    
    crear_cuenta(nombre, correo, password)

    return redirect(url_for('pagina'))