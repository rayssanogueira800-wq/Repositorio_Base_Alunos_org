#Funções das operações básicas.
def somar(n1,n2):
    return n1 + n2

def subitrair(n1,n2):
    return n1 - n2 

def multiplicar(n1,n2):
    return n1 * n2

#Boa pràtrica (enviar erro.)
def dividir(n1,n2):
    return n1 / n2

def calcular(n1,n2,operacao):
    if operacao == "+":
        return somar(n1,n2)
    elif operacao == "-":
        return subitrair(n1,n2)
    elif operacao == "*":
        return multiplicar(n1,n2)
    elif operacao == "/":
        return dividir(n1,n2)
    else:
        return "operacao invalida."