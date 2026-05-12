peso = float(input("Digite o seu peso em km: "))
altura = float(input("Digite a su a altura em m: "))

imc = peso / (altura * altura)
  
  if imc < 18.5:
      print("Abaixo dom peso.")
elif imc < 24.9:
      print("Peso noramal.")
elif imc < 29.9:
      print("sobrepeso.")