#tentando codificar o problema da mochila do livro

# colunas: peso da mochila
# linhas: cada item(analisando seu respectivo peso e valor)

def lista_itens(matriz, items, c):

    melhores = []
    for linha ,(item, (peso, valor)) in reversed(list(enumerate(items.items()))): #rodando comecando pelo ultimo elemento matriz[-1][-1]
        if c < 0: # se a capacidade - 1 for < 0, significa que nao cabe mais nada lá, quebra
            break
        if linha == 0:
            if matriz[linha][c] > 0:
                melhores.append(item)
        else:
            if matriz[linha][c] > matriz[linha-1][c]:
                melhores.append(item)
                c = c - peso                
    return melhores

def progDinamica(matriz, items):
    maior = 0
    melhores = []
    for l, (item, (peso, valor)) in enumerate(items.items()):
        for c in range(4):
            capacidade = c + 1

            # A) não pegar o item -> herda a linha de cima
            semItem = matriz[l-1][c] if l > 0 else 0

            # B) pegar o item (se couber)
            if peso <= capacidade:
                restante = capacidade - peso
                if restante > 0 and l > 0:
                    comItem = valor + matriz[l-1][restante - 1]
                else:
                    comItem = valor
            else:
                comItem = 0

            matriz[l][c] = max(semItem, comItem)
            maior = max(maior, matriz[l][c])
    melhores = lista_itens(matriz, items, c-1)
    print(maior, matriz, melhores)



matriz = [[0] * 4 for _ in range(3)] 

items = {
    "Radio": (4, 3000), 
    "Notebook": (3, 2000),
    "Violao": (1, 1500) 
}
progDinamica(matriz, items)




