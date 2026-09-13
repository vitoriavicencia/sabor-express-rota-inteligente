from collections import deque
import heapq
import math

bairros = {"Loja": (0,0),
           "Centro": (2,1),
           "Vila_Nova": (4,-5),
           "Jardim_Sul": (5,-1),
           "Bela_Vista": (2,5),
           "Parque_Alto": (2,4),}

ruas = {
    "Loja":        [("Centro", 2.5)],
    "Centro":      [("Loja", 2.5), ("Jardim_Sul", 3.6), ("Parque_Alto", 3.2)],
    "Vila_Nova":   [("Jardim_Sul", 4.1), ("Bela_Vista", 5.0)],
    "Jardim_Sul":  [("Centro", 3.6), ("Vila_Nova", 4.1)],
    "Bela_Vista":  [("Parque_Alto", 1.0), ("Vila_Nova", 5.0)],
    "Parque_Alto": [("Centro", 3.2), ("Bela_Vista", 1.0)],
}


def bfs(grafo, inicio, fim):
    visitados = {inicio}
    fila = deque([(inicio, [inicio])])

    while fila:
        atual, caminho = fila.popleft()

        if atual == fim:
            return caminho

        for vizinho, peso in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, caminho + [vizinho]))

    return None


def dfs(grafo, atual, fim, visitados=None, caminho=None):
    if visitados is None:
        visitados = set()
        caminho = [atual]

    if atual == fim:
        return caminho

    visitados.add(atual)

    for vizinho, peso in grafo[atual]:
        if vizinho not in visitados:
            resultado = dfs(grafo, vizinho, fim, visitados, caminho + [vizinho])
            if resultado is not None:
                return resultado

    return None


def heuristica(bairro_a, bairro_b):
    x1, y1 = bairros[bairro_a]
    x2, y2 = bairros[bairro_b]
    return math.hypot(x2 - x1, y2 - y1)


if __name__ == "__main__":
    caminho = bfs(ruas, "Loja", "Bela_Vista")
    print("Caminho encontrado pelo BFS:", caminho)

    caminho_dfs = dfs(ruas, "Loja", "Bela_Vista")
    print("Caminho encontrado pelo DFS:", caminho_dfs)

    dist = heuristica("Loja", "Centro")
    print("Distância em linha reta Loja -> Centro:", dist)