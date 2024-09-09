from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    print("total frutas : ", int(request.form['fresa']) + int(request.form['frambuesa']) + int(request.form['manzana']))
    return render_template("checkout.html")

@app.route('/frutas')         
def fruits():
    return render_template("frutas.html")

if __name__=="__main__":   
    app.run(debug=True)    