from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector

import mysql.connector
from flask import Flask

app = Flask(__name__)
app.secret_key = 'alexis'

db = mysql.connector.connect(
    host="alexisAA.mysql.pythonanywhere-services.com",
    user="alexisAA",
    password="",
    database="alexisAA$tienda_peluches"
)

cursor = db.cursor()


@app.route('/')
def home():
    return render_template('inicio.html')



@app.route('/peluches', methods=['GET', 'POST'])
def peluches():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    cursor = db.cursor()
    resultados = None
    buscar_palabra = ''

    if request.method == 'POST':
        buscar_palabra = request.form['buscar']
        query = "SELECT * FROM peluches WHERE nombre LIKE %s"
        cursor.execute(query, ('%' + buscar_palabra + '%',))
    else:
        cursor.execute("SELECT * FROM peluches")
    
    resultados = cursor.fetchall()
    cursor.close()
    return render_template('peluches.html', data=resultados, buscar_palabra=buscar_palabra)

@app.route('/listar', methods=['GET', 'POST'])
def listar():
    cursor = db.cursor()
    resultados = None
    buscar_palabra = ''

    if request.method == 'POST':
        buscar_palabra = request.form['buscar']
        query = "SELECT * FROM peluches WHERE nombre LIKE %s"
        cursor.execute(query, ('%' + buscar_palabra + '%',))
    else:
        cursor.execute("SELECT * FROM peluches")
    
    resultados = cursor.fetchall()
    cursor.close()
    return render_template('listar.html', data=resultados, buscar_palabra=buscar_palabra)
    

@app.route('/agregar/producto', methods=['GET', 'POST'])
def agregar_producto():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        nom = request.form['nombre']
        pre = request.form['precio']
        ima = request.form['imagen']
        imagen_path = f"static/images/{ima}.png"
        cursor = db.cursor()
        query = "INSERT INTO peluches (nombre, precio, imagen) VALUES (%s, %s, %s)"
        cursor.execute(query, (nom, pre, imagen_path))
        db.commit()  # Confirmar los cambios
        cursor.close()
        flash('Producto agregado correctamente', 'success')
        return redirect(url_for('peluches'))
    else:
        return render_template('agregar.html')
@app.route('/ver/<int:id>', methods=['GET', 'POST'])
def ver_producto(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM peluches WHERE id=%s", (id,))
    producto = cursor.fetchone()
    cursor.close()
    return render_template('ver.html', producto=producto)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    if 'usuario' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        imagen = request.form['imagen']
        cursor = db.cursor()
        query = "UPDATE peluches SET nombre=%s, precio=%s, imagen=%s WHERE id=%s"
        cursor.execute(query, (nombre, precio, imagen, id))
        db.commit()
        cursor.close()
        flash('Producto actualizado correctamente', 'success')
        return redirect(url_for('peluches'))
    else:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM peluches WHERE id=%s", (id,))
        producto = cursor.fetchone()
        cursor.close()
        return render_template('editar.html', producto=producto)

@app.route('/borrar/<int:id>', methods=['POST'])
def borrar_producto(id):
    if 'usuario' not in session:
        return redirect(url_for('login'))

    cursor = db.cursor()
    query = "DELETE FROM peluches WHERE id=%s"
    cursor.execute(query, (id,))
    db.commit()
    cursor.close()
    flash('Producto eliminado correctamente', 'success')
    return redirect(url_for('peluches'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['contraseña']
        cursor = db.cursor()
        query = "SELECT * FROM administrador WHERE nombre = %s AND contraseña = %s"
        cursor.execute(query, (nombre, contrasena))
        user = cursor.fetchone()
        cursor.close()
        if user:
            session['usuario'] = nombre
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('home'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Has cerrado sesión exitosamente', 'success')
    return redirect(url_for('home'))

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/enviar_mensaje', methods=['POST'])
def enviar_mensaje():
    nombre = request.form['nombre']
    mensaje = request.form['mensaje']

    cursor = db.cursor()
    sql = "INSERT INTO mensaje (nombre, mensaje) VALUES (%s, %s)"
    val = (nombre, mensaje)

    try:
        cursor.execute(sql, val)
        db.commit()
        flash('Mensaje enviado exitosamente.', 'success')
    except Exception as e:
        db.rollback()
        flash(f'Error al enviar el mensaje: {str(e)}', 'danger')
    finally:
        cursor.close()

    return redirect(url_for('contacto'))

@app.route('/listarc', methods=['GET', 'POST'])
def listarc():
    if 'carrito' not in session:
        session['carrito'] = []

    cursor = db.cursor()
    resultados = None
    buscar_palabra = ''

    if request.method == 'POST' and 'buscar' in request.form:
        buscar_palabra = request.form['buscar']
        query = "SELECT * FROM peluches WHERE nombre LIKE %s"
        cursor.execute(query, ('%' + buscar_palabra + '%',))
    else:
        cursor.execute("SELECT * FROM peluches")
    
    resultados = cursor.fetchall()
    
    # Obtener detalles de los productos en el carrito
    productos_carrito = []
    for producto_id in session['carrito']:
        cursor.execute("SELECT * FROM peluches WHERE id = %s", (producto_id,))
        producto = cursor.fetchone()
        if producto:
            productos_carrito.append(producto)

    if request.method == 'POST' and 'producto_id' in request.form:
        producto_id = int(request.form['producto_id'])
        if producto_id not in session['carrito']:
            session['carrito'].append(producto_id)
            session.modified = True
    
    cursor.close()
    return render_template('listar.html', data=resultados, buscar_palabra=buscar_palabra, productos_carrito=productos_carrito)
@app.route("/carrito")
def carrito():
    if 'carrito' not in session:
        session['carrito'] = []
    
    productos_carrito = []
    try:
        cursor = db.cursor()
        
        for producto_id in session['carrito']:
            cursor.execute("SELECT * FROM peluches WHERE id = %s", (producto_id,))
            producto = cursor.fetchone()
            if producto:
                productos_carrito.append(producto)
        
        cursor.close()
        return render_template("carrito.html", productos_carrito=productos_carrito)
    
    except mysql.connector.Error as err:
        return f"Error: {err}"

    
if __name__ == "__main__":
    app.run(debug=True)
