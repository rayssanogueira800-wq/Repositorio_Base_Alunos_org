from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.get("/api/soma/<int:num1>/<int:num2>")
def soma(num1,num2):
    resultado = num1 + num2
    return f"A soma de {num1} + {num2} = {resultado}"

@app.get("/api/subtracao/<int:num1>/<int:num2>")
def subtrair(num1,num2):
    resultado = num1 - num2
    return f"A soma de {num1} - {num2} = {resultado}"

@app.get("/api/divisao/<int:num1>/<int:num2>")
def dividir(num1,num2):
    resultado = num1 / num2
    return f"A soma de {num1} / {num2} = {resultado}"

@app.get("/api/multiplicacao/<int:num1>/<int:num2>")
def multiplicar(num1,num2):
    resultado = num1 * num2
    return f"A soma de {num1} * {num2} = {resultado}


if __name__ == "__main__":
    app.run(debug=True)
