from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
@app.route('/loteria')
def loteria():
    colors = ['red', 'blue', 'green']
    return render_template('loteria.html', rows=4,cols=4,colors=colors)

@app.route('/<int:rows>/<int:cols>')
def rows(rows, cols):
    colors = ['#287fe4', '#eadb00', '#dda8c5']
    return render_template('loteria.html', rows=rows, cols=cols, colors=colors)

if __name__ == '__main__':
    app.run(debug=True)


    