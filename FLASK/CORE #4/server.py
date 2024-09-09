from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/', methods=['GET', 'POST'])
def destino():
    if request.method == 'POST':
        session['nombre'] = request.form['nombre']
        return render_template('destino.html')
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)