from flask_cors import CORS
from flask import Flask, render_template
import math as mt
from flask import jsonify

app = Flask(__name__)
CORS(app)

# suma 
@app.route('/')
@app.route('/suma/<float:numero1>/<float:numero2>')
@app.route('/suma/<int:numero1>/<int:numero2>')
@app.route('/suma/<int:numero1>/<float:numero2>')
@app.route('/suma/<float:numero1>/<int:numero2>')
def suma(numero1, numero2):
    titulo = 'Suma'
    resultado = f'el resultado de {numero1} + {numero2} es: {numero1 + numero2}'
    data={
        'resultado' : resultado,
        'operacion' : 'Suma'
    }
    jsonify(data)
    return render_template('index.html', titulo=titulo, resultado=resultado)


# resta 
@app.route('/')
@app.route('/resta/<float:numero1>/<float:numero2>')
@app.route('/resta/<int:numero1>/<int:numero2>')
@app.route('/resta/<int:numero1>/<float:numero2>')
@app.route('/resta/<float:numero1>/<int:numero2>')
def resta(numero1, numero2):
    titulo = 'Resta'
    resultado = f'el resultado de {numero1} - {numero2} es: {numero1 - numero2}'    
    data={
        'resultado' : resultado,
        'operacion' : 'Resta'
    }
    jsonify(data)
    return render_template('index.html', titulo=titulo, resultado=resultado)

# multiplicacion 
@app.route('/')
@app.route('/multiplicacion/<float:numero1>/<float:numero2>')
@app.route('/multiplicacion/<int:numero1>/<int:numero2>')
@app.route('/multiplicacion/<int:numero1>/<float:numero2>')
@app.route('/multiplicacion/<float:numero1>/<int:numero2>')
def multiplicacion(numero1, numero2):
    titulo = 'Multiplicacion'
    resultado = f'el resultado de {numero1} x {numero2} es: {numero1 * numero2}'
    data={
        'resultado' : resultado,
        'operacion' : 'Multiplicacion'
    }
    jsonify(data)
    return render_template('index.html', titulo=titulo, resultado=resultado)

# division 
@app.route('/')
@app.route('/division/<float:numero1>/<float:numero2>')
@app.route('/division/<int:numero1>/<int:numero2>')
@app.route('/division/<int:numero1>/<float:numero2>')
@app.route('/division/<float:numero1>/<int:numero2>')
def division(numero1, numero2):
    titulo = 'Division'
    resultado = f'el resultado de {numero1} ÷ {numero2} es: {numero1 / numero2}'
    data={
        'resultado' : resultado,
        'operacion' : 'Division'
    }
    jsonify(data)
    return render_template('index.html', titulo=titulo, resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
