import os 
import shutil
#Isso é um comentário, não é execultado peo python.
#os.getcwd() - Mostra a pasta atual 
#os.listdir() - Lista arquivos e pastas
#os.mkdir("pasta") - Cria uma pasta 
#os.remove("pasta") - remove uma pasta  
#shutil("origem") - "destino") - Move uma pasta da orogem ao destino..
#os.system("comando") - Execultar um comando.
import os 
print("Criador de pasta")
pasta = input("Digite o nome da pasta qie deseja criar: ")
print(os.getcwd())
os.mkdir(f"Altomocao/teste_cli/{pasta}")