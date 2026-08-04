def criar_saudacao(nome, periodo):
    p = periodo.lower()
    if p == "manhã": return f"bom dia,{nome}!"
    elif p == "tarde": return f"bom tarde,{nome}!"
    elif p == "noite": return f"bom noite,{nome}!"

print(criar_saudacao("Ana", "manhã"))
print(criar_saudacao("Carlos", "TARDE"))
print(criar_saudacao("Beatriz", "NOITE"))