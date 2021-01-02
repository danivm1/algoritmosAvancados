# Daniel, Janaina e Helena

# grafo = {
#     'a': {'b': 0, 'd': 1, 'e': 2},
#     'b': {'a': 0, 'c': 4, 'e': 5},
#     'c': {'b': 4, 'e': 7},
#     'd': {'a': 1, 'e': 9},
#     'e': {'a': 2, 'b': 5, 'c': 7, 'd': 9, 'f': 14},
#     'f': {'e': 14}
# }

# grafo = {
#     'a': {'b': 7, 'd': 5},
#     'b': {'a': 7, 'c': 8, 'd': 9, 'e': 7},
#     'c': {'b': 8, 'e': 5},
#     'd': {'a': 5, 'b': 9, 'e': 15, 'f': 6},
#     'e': {'b': 7, 'c': 5, 'd': 15, 'f': 8, 'g': 9},
#     'f': {'d': 6, 'e': 8, 'g': 11},
#     'g': {'e': 9, 'f': 11},
# }

grafo = {
    'a': {'b': 4, 'h': 8},
    'b': {'a': 4, 'c': 8, 'h': 11},
    'c': {'b': 8, 'd': 7, 'f': 4, 'i': 1},
    'd': {'c': 7, 'e': 9, 'f': 3},
    'e': {'d': 9, 'f': 10},
    'f': {'c': 4, 'd': 3, 'e': 10, 'g': 2},
    'g': {'f': 2, 'h': 1, 'i': 6},
    'h': {'a': 8, 'b': 11, 'g': 1, 'i': 2},
    'i': {'c': 1, 'g': 6, 'h': 2}
}

# TODO Implementar funções para que o usuário também possa digitar seu próprio grafo


# def insere_vertice(g, a, b):
#     if a not in g:
#         g[a]=[]
#     if b not in g:
#         g[b]=[]
#     g[a].append(b)
#     g[b].append(a)

# def imprime_grafo(g):
#     for v,a in g.items():
#         print("="*50)
#         print('Vertice:', v)
#         print('Adjacentes:', a)

def ordena(vetor,inicio,fim):
    if(inicio < fim):
        q = pivoOrdena(vetor,inicio,fim)
        ordena(vetor, q[1],q[0]-1)
        ordena(vetor, q[0]+1,q[2])

def pivoOrdena(vetor,inicio,fim):
    pivo = vetor[fim]
    i = inicio-1

    for j in range(inicio,fim):
        if(peso(grafo, vetor[j]) <= peso(grafo, pivo)):
            i += 1
            vetor[i],vetor[j] = vetor[j],vetor[i]

    vetor[i+1],vetor[fim] = vetor[fim],vetor[i+1]
    return i+1,inicio,fim

def peso(grafo, aresta):
    return grafo[aresta[0]][aresta[1]]

def ordena_arestas(grafo):
    arestas_ordenadas = []
    for u,vizinhos in grafo.items():
        for v in vizinhos.keys():
            arestas_ordenadas.append(tuple([u, v]))
    ordena(arestas_ordenadas,0,len(arestas_ordenadas)-1)
    return arestas_ordenadas

sets = {}

# Cria sets pra poder utilizar subset no union-find
def criaSet(x):
    sets[x] = set([x])


# Método union-find para verificar existência de ciclos
def encontra(x):
    for representative,subset in sets.items():
        if x in subset:
            return representative
    return None

def une(x, y):
    xRepresentative = encontra(x)
    yRepresentative = encontra(y)
    sets[yRepresentative] = sets[yRepresentative].union(sets[xRepresentative])
    del sets[xRepresentative]

def kruskal(grafo):
    arestas_ordenadas = ordena_arestas(grafo)
    arvore_geradora_minima = []
    for v in grafo.keys():
        criaSet(v)
    for aresta in arestas_ordenadas:
        if encontra(aresta[0]) != encontra(aresta[1]):
            arvore_geradora_minima.append(aresta)
            une(aresta[0], aresta[1])

    return arvore_geradora_minima




arvore_geradora_minima = kruskal(grafo)

print(arvore_geradora_minima)