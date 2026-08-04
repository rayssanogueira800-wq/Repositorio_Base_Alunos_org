def cantar_vogais(textos):
    vogais = "aeiouAEIOU"
    cont = 0 
    for c in textos:
        if c in vogais: cont += 1
    return cont 

print(cantar_vogais("Olá mundo"))
print(cantar_vogais("python"))
print(cantar_vogais("AEIOU"))