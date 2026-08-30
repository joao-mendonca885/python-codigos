def ache_o_vertice_de_menor_custo(custos): #levando em conta o processados
    menorCusto = float("inf")
    nodoMenorCusto = None
    for nodo in custos:
        custo = custos[nodo]
        if custo < custoAtual and not in processados:
            menorCusto = custo
            nodoMenorCusto = nodo
    return nodoMenorCusto



def Dijkstra(grafo, custos, pai):
    nodo = ache_o_vertice_de_menor_custo(custos) # 1 - vertice de menor custo: B
    while nodo is not None: #enquanto ainda nao chegou no fim
        custo = custos[nodo] #custo do vertice B: 2
        vizinhos = grafo[nodo] #vizinhos de B: A e Fim
        for n in vizinhos.keys(): # para cada vizinho de B
            novo_custo = custo + vizinhos[n] #novo custo = custo até B: 2 + custo de B até o vizinho de b(A): 3
            if custos[n] > novo_custo: # se o custo do inicio até o A for maior que o custo de inicio -> B -> A
                custos[n] = novo_custo # O custo até A é atualizado
                pai[n] = nodo # o pai de A será atualizado
        processados.append(nodo) # processamos o B
        nodo = ache_o_vertice_de_menor_custo(custo) # repetimos o processo









