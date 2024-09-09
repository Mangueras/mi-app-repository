from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "esta es mi llave"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/crear_usuario", methods=['POST'])
def crear_usuario():
    print("Recibiendo información")
    print(request.form)
    session['nombre_usuario'] = request.form['nombre']
    session['gmail_usuario'] = request.form['gmail']
    session['visitas'] = 0
    session['reinicio'] = 0
    return redirect("/mostrar_usuario")

@app.route("/mostrar_usuario")
def mostrar_usuario():
    session['visitas'] += 1
    print("Usuario redirigido")
    print(session['nombre_usuario'])
    print(session['gmail_usuario'])
    print(session['visitas'])
    return render_template("mostrar.html")

@app.route("/destruir_sesion")
def destruir_sesion():
    session.clear()
    return redirect("/")

@app.route("/agregar_visitas", methods=['POST'])
def agregar_visitas():
    session['visitas']= int(request.form['visitas'])
    return redirect("/mostrar_usuario")

@app.route("/agregar_visitas_2")
def agregar_visitas_2():
    session['visitas'] += 1
    return redirect("/mostrar_usuario") 

@app.route("/borrar_visitas")
def borrar_visitas():
    session['visitas'] = 0
    session['reinicio'] += 1
    return redirect("/mostrar_usuario")

if __name__ == "__main__":
    app.run(debug=True)