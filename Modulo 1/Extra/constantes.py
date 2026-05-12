TAXA_SERVICO = 0.004
PERCENTUAL_IMPOSTO_RENDA_4 = 0.24 
PERCENTUAL_IMPOSTO_RENDA_3 = 0.2 
PERCENTUAL_IMPOSTO_RENDA_2 = 0.15 
PERCENTUAL_IMPOSTO_RENDA_1 = 0.1
FAIXA_SALARIAL_4 = 10000
FAIXA_SALARIAL_3 = 7500
FAIXA_SALARIAL_2 = 5000
FAIXA_SALARIAL_1 = 2500

print("Calculadora de imposto")

salario_base = float(input("Digite o quanto vc ganha: "))

if salario_base > FAIXA_SALARIAL_4:
    imposto = salario_base * (PERCENTUAL_IMPOSTO_RENDA_4 + TAXA_SERVICO)

elif salario_base > FAIXA_SALARIAL_3: 
    imposto = salario_base * (PERCENTUAL_IMPOSTO_RENDA_3 + TAXA_SERVICO)

elif salario_base > FAIXA_SALARIAL_2: 
    imposto = salario_base * (PERCENTUAL_IMPOSTO_RENDA_2 + TAXA_SERVICO) 

elif salario_base > FAIXA_SALARIAL_1:
    imposto = salario_base * (PERCENTUAL_IMPOSTO_RENDA_1 + TAXA_SERVICO)
else: 
    imposto = 0

print(f"Para a sua faixa salarial o imposto é: {imposto}")