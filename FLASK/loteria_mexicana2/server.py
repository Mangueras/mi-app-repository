from flask import Flask, render_template, request
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

numero_secreto = random.randint(1, 54)
intentos_realizados = 0
max_intentos = 5

@app.route('/', methods=['GET', 'POST'])
def index():
    global intentos_realizados
    if request.method == 'POST':
        intento = int(request.form['intento'])
        intentos_realizados += 1
        if intento < numero_secreto:
            mensaje = 'El número es mayor'
        elif intento > numero_secreto:
            mensaje = 'El número es menor'
        else:
            mensaje = '¡Correcto! Has adivinado el número.'
            intentos_realizados = 0
            return render_template('resultado.html', mensaje=mensaje, intentos=intentos_realizados)
        
        if intentos_realizados >= max_intentos:
            mensaje = f'Se han agotado los intentos. El número era {numero_secreto}.'
            intentos_realizados = 0
            return render_template('resultado.html', mensaje=mensaje, intentos=max_intentos)
        
        return render_template('index.html', mensaje=mensaje, intentos=intentos_realizados)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)