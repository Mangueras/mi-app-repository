
from flask import Flask, redirect, render_template, request


# Importamos la clase de mascota.py

from mascota import Mascota

app = Flask(__name__)

@app.route("/")

def index():

   # Invocamos al método de clase get all para obtener todas las mascotas

   mascotas = Mascota.get_all()

   print(mascotas)

   #Crea un archivo index.html para que se por lo pronto

   return render_template("index.html")

@app.route("/crear_mascota", methods=['POST'])
def crear_mascota():
   datos = {
       "nombre": request.form['nombre'],
       "tipo": request.form['tipo'],
       "color": request.form['color']
   }
   Mascota.save(datos)
   return redirect('/')

if __name__ == "__main__":

   app.run(debug=True)

