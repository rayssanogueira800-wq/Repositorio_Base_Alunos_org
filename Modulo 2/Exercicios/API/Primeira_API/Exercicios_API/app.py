from flask import Flask, jsonify


app = Flask(__name__)


@app.get("/api/soma/<int:num1>/<int:num2>")
def soma(num1,num2):
    resultado = num1 + num2
    return jsonify(resultado)


# Dobro do número


@app.get("/api/dobro/<int:numero>")
def dobro(numero):
    dobro_numero = numero * 2
    return jsonify({
        "numero":numero,
        "dobro":dobro_numero
    })


@app.get("/pedro")
def ola_pedro():
    return jsonify({
        "mensagem":"Olá Pedro!"
    })




if __name__ == "__main__":
    app.run(debug=True)

