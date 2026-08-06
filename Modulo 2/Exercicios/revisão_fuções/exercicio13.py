def encontar_maior(numeros):
    if not numeros: return None
    maior = numeros[0]
    for n in numeros:
        if n > maior: maior = n 
    return maior 

print(encontar_maior([3,9,2,7]))
print(encontar_maior([]))
print(encontar_maior([-5,-2,-8]))
