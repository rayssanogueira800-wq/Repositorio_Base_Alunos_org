def eh_bissexto(ano):
    return ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)

print(eh_bissexto(2024))
print(eh_bissexto(1900))
print(eh_bissexto(2000))

