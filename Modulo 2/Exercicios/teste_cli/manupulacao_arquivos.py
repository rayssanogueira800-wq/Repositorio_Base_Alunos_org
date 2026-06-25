# arquivo = open("texto.txt", "r", ecoding="utf-8")
# conteudo = arquivo.read()
# print(conteudo)
# arquivo.close()

### LENDO O CONTEÙDO
with open("texto.txt", "r", encoding="utf-8") as arquivo: 
    conteudo  = arquivo.read()
    print(conteudo)
### ESCREVENDO UM NOVO CONTEÙDO (Modo A)
with open("texto.txt", "a", encoding="utf-8") as arquivo:    
    texto = "\nEu ainda penso em nós, diz se ainda pensa em. Admito que sinto sua falta."
    arquivo.write(texto)