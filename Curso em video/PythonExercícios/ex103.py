def ficha(nome="<desconhecido>", gols=0):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato")


n = str(input("Digite o nome do jogador: ")).strip()
g = str(input("Digite a quantidade de gols: ")).strip()
if n == "" and g == "":
    ficha()
elif n == "":
    ficha(gols=g)
elif g == "":
    ficha(n)
else: ficha(n, g)
