from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/contacto', methods=['POST'])
def contacto():
    nombre = request.form['nombre']
    email = request.form['email']
    mensaje = request.form['mensaje']

    print("Nuevo mensaje recibido:")
    print(f"Nombre: {nombre}")
    print(f"Email: {email}")
    print(f"Mensaje: {mensaje}")

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)