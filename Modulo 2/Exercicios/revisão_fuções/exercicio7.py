def classificar_idade(idade):
    if idade < 0: return "idade invalida"
    if idade < 12: return "criança"
    if idade < 17: return "adolesente"
    if idade < 59: return "adulto"
    return "idoso"

print(classificar_idade(-2))
print(classificar_idade(10))
print(classificar_idade(16))
print(classificar_idade(30))
print(classificar_idade(65))