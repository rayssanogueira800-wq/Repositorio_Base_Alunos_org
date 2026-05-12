numero = int(input("Digite o numero da tabuada: "))
numero_inicio = int(input("Digite da onde a tabuada começa: "))
numero_fianal = int(input("Digite até qual número vai: "))

for i in range(numero_inicial,numero_final+1):
    print(i)
    print(f" {numero} x {i} = {i * numero}")