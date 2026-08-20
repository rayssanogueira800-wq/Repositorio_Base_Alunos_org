from flask import Flask, jsonify

app = Flask(__name__) #Criara app (nossa api)
app.json.ensure_ascii = False # Para não ter problema com a acentuação

cursos = [
    {
        "id": 1,
        "nome": "python",
        "area": "programação",
        "carha_horaria": 40,
        "ativo": True
    },
    {
        "id": 2,
        "nome": "Ingles",
        "area": "linguas",
        "carha_horaria": 30,
        "ativo": True
    },
    { 
        "id": 3,
        "nome": "matemática",
        "area": "ciencias",
        "carha_horaria": 40,
        "ativo": True
    }
]

@app.get("/") #Caminho endereço/
def inicio():
    return "Hello, World!"


@app.get("/api/status")
def status():
    return jsonify({ #JSON
        "status":"online",
        "mensagem":"API funcionando!"
    })

@app.get("/api/cursos")
def get_cursos():
    return jsonify(cursos)

@app.get("/api/cursos/<int:id>")
def get_curso(id):
    for curso in cursos:
        if curso["id"] == id:
            return jsonify(curso)
    return jsonify({"mensagemJ": "curso n encontrado"}), 404

app.run(debug=True) 