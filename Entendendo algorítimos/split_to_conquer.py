def mdca(a, b):
    if b == 0: #quando o resto zera, achamos o mdc
        return a
    return mdca(b, a % b) # chamada recursiva com (menor, resto)


resultado = mdca(1680, 640) # 80
print(resultado)


def pesquisa_em_largura(fila, processados):
    while fila:
        pessoa = fila.popleft()
        if pessoa not in processados:
            if pessoa_e_um_vendedor_de_manga(pessoa):
                return pessoa
            else:
                fila = fila + grafo[pessoa]
                processados.append(pessoa)
    return False



def quicksort(lista):
    if len(lista) < 2:
        return lista
    pivo = lista[0]
    menores = [i for i in lista[1:] if i <= pivo] # [elemento, iteravel, condicao]
    maiores = [i for i in lista[1:] if i > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)



for x, y in movimentos:

for i in range(8):
    for j in range(8):
        matriz[i][j] = 0