porcentagem = [30, 50, 10, 10]
categories = ["Food", "Entertainment", "Business"]
lista_dezenas = [dezena for dezena in range(100, -1, -10)]
linhas = []
for idx in range(len(lista_dezenas)):
    dezena = f"{lista_dezenas[idx]:>3}| "
    celula = ["o " for p in porcentagem if p >= lista_dezenas[idx]]
    espacado = " ".join(celula)
    linhas.append(dezena + espacado)
primeira_parte = "\n".join(linhas)
#segunda parte
quatro_espacos = "    "
resto = "---" * len(celula) + "-"
segunda_parte = quatro_espacos + resto
# terceira parte
maior = max(len(categoria) for categoria in categories)
terceira_parte = []

for i in range(maior):
    linha = "   "
    for categoria in categories:
        if i < len(categoria):
            linha += "  " + categoria[i]
        else:
            linha += "   "
    terceira_parte.append(linha)
terceira_parte = "\n".join(terceira_parte)
print(primeira_parte + "\n" + segunda_parte + "\n" + terceira_parte)