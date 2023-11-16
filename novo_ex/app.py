from flask import Flask, render_template, request
from sympy import symbols

app = Flask(__name__)

# Função para calcular o volume da caixa
def calcular_volume(x_value):
    x = symbols('x')
    volume = x * (30 - 2 * x) * (20 - 2 * x) 
    volume = volume.subs(x, x_value)  
    return volume

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        x_value = float(request.form['x_value'])
        resultado = calcular_volume(x_value)
        return render_template('index.html', resultado=resultado)
    return render_template('index.html', resultado=None)

if __name__ == '__main__':
    app.run(debug=True)
