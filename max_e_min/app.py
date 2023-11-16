from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calcular_maximo(x):
    V = x * (1 - 2*x)**2
    return V

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    x = float(data['x'])

    if 0 <= x <= 0.5:
        resultado = calcular_maximo(x)
        x_maximo = 1/6  

        if x == x_maximo:
            mensagem = f"Parabéns! Você inseriu o valor que produz o máximo de V(x): {x_maximo}"
        else:
            mensagem = f"O valor de V(x) para x = {x} é {resultado}"
    else:
        mensagem = "Por favor, insira um valor válido para x dentro do intervalo [0, 0.5]."

    return jsonify({'resultado': mensagem})

if __name__ == '__main__':
    app.run(debug=True)
