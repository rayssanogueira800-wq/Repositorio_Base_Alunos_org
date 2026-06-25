import os
os.system("cls")

def limpar_tela():
    os.system("cls")

print("Seja bem-vindo ao sistema de Notas 🤖")
while True:
    opcao = input("[1] - cadastrar aluno e nota\n" \
    "[2] - Listar alunos\n" \
    "[3] - listar alunos com nota\n" \
    "[0] - sair\nSua opção: ")

    if opcao == "1":
        nome = input("Digite o nome do(a) alunoa(a): ")
        idade = int(input("Digite a idade do(a) aluno(a): "))
        nota = float(input("Digite a nota do(a) aluno(a): "))
        with open("aluno.csv", "a", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([nome,idade,nota])

    elif opcao == "2":
        with open("aluno.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                print(linha)

        print("Listar alunos")
    elif opcao == "3":
        print("Listar alunos com nota acima de 8")
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção invalida.")

    input("Aperte ENTER para continuar")
    limpar_tela()


