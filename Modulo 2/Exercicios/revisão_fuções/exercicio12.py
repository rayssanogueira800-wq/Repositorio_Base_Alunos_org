def gerar_tabuada(num):
    tab = []
    for i in range(1, 11):
        tab.append(num * i)
    return tab

print(gerar_tabuada(5))
print(gerar_tabuada(3))