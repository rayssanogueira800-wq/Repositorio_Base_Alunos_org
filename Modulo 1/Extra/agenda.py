import os

def limpa_tela():
    os.system("cls")

def adicionar_nome(lista_nomes, nome):
    lista_nomes.append(nome) #Adicione o nome na lista_nomes.

def remover_nome(lista_nomes, nome):
     lista_nomes.remove(nome) #Remove nome na lista_nomes.

def mostrar_nome(lista_nomes):
    for nome in lista_nomes: #["joão"," Maria","Ana"]
        print(nome)

nomes = []
while True:
    limpa_tela()
    menu = input("Escolha sua opção:\n[1] - Listar nomes\n[2] - Adicionar nomes\n[3] - remover nomes\n[0] - Sair\nSua opção: ")
    if menu == "0":
        break
    elif menu == "1": 
        mostrar_nome(nomes)
        input("Aperte enter para continuar")
    elif menu == "2":
        nome_salvar = input ("Digite o nome que dseseja adicionar: ")
        adicionar_nome(nomes, nome_salvar)
    elif menu == "3":
        nome_remover = input("Digite o nome que deseja remover: ")
        remover_nome(nomes, nome_salvar)
    else:
        print("Opção invalida.")
        input("Aperte enter para continuar")                                                                                                                                                   