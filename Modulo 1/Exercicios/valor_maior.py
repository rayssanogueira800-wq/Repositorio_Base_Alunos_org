numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 == numero2:
    print("Os números são iguais!")
elif numero1 > numero2: 
    print(f"{numero1}é maior que {numero2}!")
else:
    print(f"{numero2} é maior que {numero1}!")