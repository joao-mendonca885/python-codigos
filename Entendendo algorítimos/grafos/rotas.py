# precisamos de 3 tabelas hash:
# 1 - grafos 
# 2 - custos
# 3 - pai

def ache_o_vertice_menor_custo(custos, processados):
    custo_mais_baixo = infinito
    no = None
    for nodo in custos:
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            no = nodo
    return no

# tomando de exemplo o grafo do exemplo do claude
def dijkstra(grafo, custos, pai, processados):
    vertice = ache_o_vertice_menor_custo(custos, processados) # procurando o vértice de menor custo: 0
    while vertice != t and vertice is not None: # enquanto o vértice nao for o destino(4)
        processados.append(vertice) # marca esse vértice como processado: 0 foi processado
        custo = custos[vertice] # guardamos o custo do vértice: 0
        vizinhos = grafo[vertice] # [1, 2]
        for n in vizinhos.keys(): # [1, 2]
            novo_custo = custo + vizinhos[n] # 0 + 10 ou 3
            if novo_custo < custos[n]: # custos[n] == infinito se o custo atual for maior que o novo custo
                custos[n] = novo_custo # o novo custo passa a ser o atual 
                pai[n] =  vertice # o pai de n passa a ser o vertice em processamento
        vertice = ache_o_vertice_menor_custo(custos, processados)

def checagem_t_and_s(s, t, grafo):
    return 0 <= s < n and 0 <= t < n

def montagem_dos_pais(pai, grafo):
    for n in grafo.keys():
        pai[n] = None
    
def montagem_dos_grafos(grafo):
    for _ in range(m):
        u, v, w = map(int, input().split())
        if u not in grafo:
            grafo[u] = {}
        grafo[u][v] = w

def montagem_dos_custos(custos):
    for c in range(n):
        if c != s:
            custos[c] = float("inf")
        else:
            custos[c] = 0

def construcao_do_caminho(pai):
    atual = t
    comeco = s
    if custos[t] == infinito:
        print(-1)
        return
    lista = [t] # {piano}
    print(custos[t])
    while s != atual:
        lista.append(pai[atual]) # pai do piano == bateria 
        atual = pai[atual] # t agora é a bateria
    for vertice in lista[::-1]:
        print(f"{vertice}", end=" ")
    

n , m = map(int, input().split())
grafo = {}
custos = {}
pai = {}
montagem_dos_grafos(grafo)
s, t = map(int, input().split())
if not checagem_t_and_s(s, t, n):
    print("Erro: vértices de origem e destino inválidos.")
    exit()
montagem_dos_custos(custos)
infinito = float("inf")
processados = []
montagem_dos_pais(pai, grafo)
dijkstra(grafo, custos, pai, processados)
construcao_do_caminho(pai)


