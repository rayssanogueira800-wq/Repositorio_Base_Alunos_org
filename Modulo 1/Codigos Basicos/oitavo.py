nome_produto = input("Digite o nome do produto: ")
preço = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto "))
valor_desconto = preço * desconto / 100
preço_final = preço - valor_desconto
print(f"produto: {nome_produto} - preço final: R$ {preço_final}")

