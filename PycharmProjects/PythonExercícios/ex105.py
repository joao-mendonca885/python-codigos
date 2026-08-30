#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e 
#vai retornar um dicionário com as seguintes informações:
# Quantidade de notas
# A maior nota
# menor nota
# média da turma
# situação (opcional)

def notas(*notas, sit=False):
    dicionario = dict()
    dicionario["Maior"] = max(notas)
    dicionario["Menor"] = min(notas)
    dicionario["Total"] = len(notas)
    dicionario["Média"] = sum(notas)/len(notas)
    if sit:
        if dicionario["Média"] >= 7:
            dicionario["Situação"] = "BOA"

    return dicionario

print(notas(6.5, 4.5, 9.0, sit=True))