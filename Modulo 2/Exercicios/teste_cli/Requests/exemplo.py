# Biblioteca Resquests 
"""
Bibloioteca Python que permite se comunicar o protocolo HTTP de forma
facil e intuitiva.

-Requisição
--cabeçalo
--corpo

-resposta
--status
--cabeçalho
--corpo
"""

import requests 

cep = input("06505055")

resposta = requests.get("https://cep.awesomeapi.com.br/json/{06505055}")

print(resposta.status_code)

if resposta.status_code == 200:
    dados = resposta.json()
    print(dados.get("address"))
    print(f"{dados.get("city")} — {dados.get("state")}")
else:
    print("CEP invalido, verifique o CEP e tente novamente.")