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


def breadth_first_search(g, r):
    marcados = []
    fila = []
    marcados.append(r)
    fila.append(r)
    while True:                                 # repete até a fila esvaziar
        if not fila:                            # checa se a fila está vazia
            break
        for i,j in g.items():                   # percorre todo o grafo
            if not fila:                        # checa se a fila está vazia
                break
            if i == fila[0]:                    # checa se o vertice atual é o primeiro da fila
                for x in j:                     # x percorre os vértices adjacentes do primeiro da fila
                    if x not in marcados:       # caso x não tenha sido marcado
                        marcados.append(x)      # marca x
                        fila.append(x)          # e o adiciona ao final da fila
                fila.pop(0)                     # retira o primeiro vértice da fila
    return marcados



grafo = { }
while True:
    x = input("Entre com o vértice ou FIM para encerrar: ")
    if x=='FIM' or x=='fim':
        break
    y = input("Entre com um vertice adjacente:")

    insere_vertice(grafo, x, y)

imprime_grafo(grafo)


r = input("Insira o vértice raiz")
bfs = breadth_first_search(grafo, r)
print(bfs)