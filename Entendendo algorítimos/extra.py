from collections import deque

def buscaBinaria(alvo, array, inicio, fim):
    if inicio > fim:
        return -1 #nao encontrou o elemento
    meio = int((inicio+fim)//2)
    if alvo == array[meio]:
        return meio
    elif alvo > meio:
        return buscaBinaria(alvo, array, meio+1, fim)
    else:
        return buscaBinaria(alvo, array, inicio, meio-1)


def bfs(nome, alvo):
    filaDePesquisa = deque() #criando a fila
    filaDePesquisa += grafo[nome] # adicionando os vizinhos desse nome à fila de pesquisa
    verficados = set()
    while filaDePesquisa:
        pessoa = filaDePesquisa.popleft()
        if pessoa not in verificados:
            if pessoa == alvo:
                return True
            else:
                verificados.add(pessoa)
                filaDePesquisa += grafo[pessoa]
    return False

def fib(n, memo=None):
    if memo is None:
        memo = {}
    if n < 2:
        return n
    
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return fib[n]


arr1 = [1, 2, 3, 4, 5]
#arr2 = reduce(lambda x, y: x + y + z, arr1)


def maior_substring(string1, string2):
    matriz = [[0] * (len(string2)) for _ in range(len(string1))]
    #string2 : coluna
    #string1 : linha
    for linha in range(len(string1)):
        for coluna in range(len(string2)):
            if string2[coluna] == string1[linha]:
                if 0 <= linha-1 < len(string1) and 0 <= coluna-1 < len(string2):
                    matriz[linha][coluna] = matriz[linha-1][coluna-1] + 1
                else:
                    matriz[linha][coluna] += 1
    return matriz
def montagem_strings_para_encontrar_maior_substring():
    string1 = "hish"
    string2 = "fish"
    matriz = maior_substring(string1, string2)
    for i in range(len(string1)):
        for j in range(len(string2)):
            print(f"{matriz[i][j]} ", end="")
        print()


def criar_pilha():
    pilha = []
    return pilha

def push(pilha, valor):
    return pilha.append(valor)

def pop(pilha):
    return pilha.pop()

def top(pilha):
    return pilha[len(pilha) - 1]

def esta_vazia(pilha):
    if pilha:
        return False
    else:
        return True