def insere_vertice(g, a, b):
    if a not in g:
        g[a]=[]
    if b not in g:
        g[b]=[]
    g[a].append(b)
    g[b].append(a)

def imprime_grafo(g):
    for v,a in g.items():
        print("="*50)
        print('Vertice:', v)
        print('Adjacentes:', a)

def bota(v, x):
    v.append(x)

def tira_fila(f):
    f.pop(0)

def tira_pilha(p):
    p.pop()

def confirmaVertice(g, v):
    if v in g.keys():
        return True
    else:
        return False

def breadth_first_search(g, r):
    if not confirmaVertice(g, r): return "raiz não consta no grafo"
    marcados = []
    fila = []
    bota(marcados, r)
    bota(fila, r)
    while True:                                 # repete até a fila esvaziar
        if not fila:                            # checa se a fila está vazia
            break
        for i,j in g.items():                   # percorre todo o grafo
            if not fila:                        # checa se a fila está vazia
                break
            if i == fila[0]:                    # checa se o vertice atual é o primeiro da fila
                for x in j:                     # x percorre os vértices adjacentes do primeiro da fila
                    if x not in marcados:       # caso x não tenha sido marcado
                        bota(marcados, x)       # marca x
                        bota(fila, x)           # e o adiciona ao final da fila
                tira_fila(fila)                 # retira o primeiro vértice da fila
    return marcados

def depth_first_search(g, r):
    if not confirmaVertice(g, r): return "raiz não consta no grafo"
    marcados = []
    pilha = []
    bota(marcados, r)
    bota(pilha, r)
    while True:                                     # repete até esvaziar a pilha
        if not pilha:                               # checa se a pilha está vazia
                break
        for i,j in g.items():                       # percorre todo grafo
            if not pilha:                           # checa se a pilha está vazia
                break
            if i == pilha[len(pilha)-1]:            # checa se o vértice atual é o último da pilha
                for x in j:                         # percorre os vértices adjacentes ao vértice atual
                    if x not in marcados:           # checa se o adjacente não está marcado
                        bota(marcados, x)           # marca o adjacente
                        bota(pilha, x)              # coloca esse no final da pilha
                        break
                    else:
                        if set(j).issubset(set(marcados)):  # checa se os vértices adjacentes já estão marcados
                            tira_pilha(pilha)                     # tira último vértice da pilha
                            break

    return marcados


grafo = { }
while True:
    x = input("Entre com o vértice ou FIM para encerrar: ")
    if x=='FIM' or x=='fim':
        break
    y = input("Entre com um vertice adjacente:")

    insere_vertice(grafo, x, y)

imprime_grafo(grafo)

print("\n\nBusca por largura:")
r = input("Insira o vértice raiz: ")
bfs = breadth_first_search(grafo, r)
print(bfs)

print("\n\nBusca por profundidade:")
r = input("Insira o vértice raiz: ")
dfs = depth_first_search(grafo, r)
print(dfs)