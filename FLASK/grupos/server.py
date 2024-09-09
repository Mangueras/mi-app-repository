from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = "esta es mi llave"

grupos = []  # Esta variable almacena una lista, donde cada elemento es un grupo
# Esta variable grupos hace las veces de una base de datos para almacenamiento
# de información (de los grupos)

class Grupo:
    def __init__(self, id, integrantes, tema, descripcion):
        self.id = id  # Tipo entero
        self.integrantes = integrantes  # Lista de integrantes
        self.tema = tema  # String
        self.descripcion = descripcion  # String

@app.route('/')
# Por omisión, el tipo de solicitud que se atiende acá es de tipo GET
@app.route('/register')
def register():
    # Verificamos la información de cuál es el número del grupo
    # que se está registrando
    if len(grupos) == 0:
        id = 1  # Id es la variable que represente el id del grupo a ser almacenado
    else:
        id = grupos[-1].id + 1
    return render_template('register.html', id=id)

@app.route('/agrega_grupo', methods=['POST', 'GET'])
def add_group():
    if request.method == 'POST':
        if len(grupos) == 0:  # Si es el primer grupo a registrarse
            id = 1  # Pongo id en 1
        else:  # Sino es el primer grupo
            id = grupos[-1].id + 1  # El id es igual al último + 1

        # A continuación, capturamos la información enviada desde el formulario
        # para la creación de un nuevo grupo

        # Partimos con los integrantes
        integrante1 = request.form.get("integrante1")
        integrante2 = request.form.get("integrante2")
        integrante3 = request.form.get("integrante3")
        integrantes = [integrante1, integrante2, integrante3]

        tema = request.form.get("project_title")
        descripcion = request.form.get("project_description")

        # Se crea el objeto grupo a partir de la información anterior
        group = Grupo(id, integrantes, tema, descripcion)

        # Luego se agrega el grupo a la lista de grupos
        grupos.append(group)  # Aquí agregamos un objeto de la clase Grupo a nuestra lista de grupos

        # Una vez terminado el proceso de registro del grupo, se "redirige" a la página
        # encargada de mostrar el listado de los grupos.
        # La redirección se realiza con una función de flask llamada redirect
        return redirect("/lista_grupos")
    else:
        # En caso contrario, la solicitud tiene que ser de tipo GET
        return redirect("/")

@app.route('/lista_grupos', methods=["GET"])
def list_groups():
    return render_template("list_groups.html", grupos=grupos)

if __name__ == '__main__':
    app.run(debug=True)
