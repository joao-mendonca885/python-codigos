from collections import deque

# Grafo direcionado do exemplo (lista de adjacencia como dicionario).
# Cada chave e um vertice; o valor e a lista de vizinhos que ele aponta.
#   A -> B, A -> C
#   B -> D, B -> E
#   C -> E
grafo = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["E"],
    "D": [],
    "E": [],
}


def menor_caminho(grafo, origem, destino):
    """Retorna a lista de vertices do menor caminho (em numero de saltos)
    de 'origem' ate 'destino', ou None se nao existir caminho."""

    if origem == destino:
        return [origem]

    # 'pai[v]' guarda de qual vertice chegamos em v pela PRIMEIRA vez.
    # Como a BFS visita por camadas, essa primeira chegada ja e a mais curta.
    # A origem tem pai None (e o ponto de partida).
    pai = {origem: None}

    fila = deque([origem])  # deque + popleft() = O(1). Nunca use list.pop(0) aqui.

    while fila:
        atual = fila.popleft()

        for vizinho in grafo[atual]:
            if vizinho not in pai:          # ainda nao visitado
                pai[vizinho] = atual        # registra quem trouxe a gente ate aqui
                if vizinho == destino:      # achou o destino: pode parar
                    return reconstruir(pai, destino)
                fila.append(vizinho)

    return None  # esvaziou a fila sem achar o destino


def reconstruir(pai, destino):
    """Sobe pela cadeia de 'pais' do destino ate a origem e inverte."""
    caminho = []
    no = destino
    while no is not None:
        caminho.append(no)
        no = pai[no]
    caminho.reverse()  # estava de tras pra frente
    return caminho


# --- Demonstracao ---
for alvo in ["B", "E", "D"]:
    caminho = menor_caminho(grafo, "A", alvo)
    if caminho:
        print(f"A -> {alvo}: {' -> '.join(caminho)}  ({len(caminho) - 1} saltos)")
    else:
        print(f"A -> {alvo}: sem caminho")