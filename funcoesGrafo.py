# Arquivo que contém as funções de manipulação de grafos

def busca_largura(grafo, aeroporto_origem, aeroporto_destino):
    fila = []
    visitados = []
    largura = {}
    ctdLargura = 1
    nivel = {}
    pai = {}

    fila.append(aeroporto_origem)
    largura[aeroporto_origem] = ctdLargura
    nivel[aeroporto_origem] = 1
    pai[aeroporto_origem] = None

    while len(fila):
        vertice = fila.pop(0)
        print(grafo.get(vertice))
        for vizinho in grafo.get(vertice):
            if not largura.get(vizinho):
                fila.append(vizinho)
                ctdLargura += 1
                largura[vizinho] = ctdLargura
                pai[vizinho] = vertice
                nivel[vizinho] = nivel[vertice] + 1
                if vizinho == aeroporto_destino:
                    return largura, nivel, pai
    return 0

def constroi_menor_caminho(pai, aeroporto_origem, aeroporto_destino):
    menor_caminho = []
    while aeroporto_destino != aeroporto_origem and pai[aeroporto_destino] != None:
        menor_caminho.insert(0, aeroporto_destino)
        aeroporto_destino = pai[aeroporto_destino]

    menor_caminho.insert(0, aeroporto_origem)
    return menor_caminho

def inverte_grafo(grafo):
    grafo_invertido = {}    
    print('Grafo Reverso')
    for no, vizinhos in grafo.items():
        for vizinho in vizinhos:
            vizin = []
            if vizinho in grafo_invertido:
                grafo_invertido[vizinho].append(no)
            else:
                vizin.append(no)
                grafo_invertido[vizinho] = vizin
    print(grafo_invertido)
    return grafo_invertido


def verifica_ciclos(grafo, no):
    nos_visitados = set()
    nos_restantes = [no]

    while nos_restantes:
        no_atual = nos_restantes.pop()
        nos_visitados.add(no_atual)

        for vizinho in grafo[no_atual]:
            if vizinho in nos_visitados:
                return True

            nos_restantes.append(vizinho)

    return False