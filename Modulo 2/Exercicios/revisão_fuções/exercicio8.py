def situacao_aluno(media, freq):
    if freq < 75: return "reprovado"
    if media > 7: return "aprovado"
    if media > 5: return "recuperação"
    return "reprovado"

print(situacao_aluno(8, 80))
print(situacao_aluno(6, 80))
print(situacao_aluno(6, 70))
print(situacao_aluno(4, 90))