def aplicar_desconto(preco, percentual):
    desconto = preco * percentual / 100
    return preco - desconto 

print(aplicar_desconto(100, 10))
print(aplicar_desconto(50, 20))
print(aplicar_desconto(200, 5))