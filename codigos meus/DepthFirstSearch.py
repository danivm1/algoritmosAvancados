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

def depth_first_search(g, r):
    marcados = []
    pilha = []
    marcados.append(r)
    pilha.append(r)
    while True:                                     # repete até esvaziar a pilha
        if not pilha:                               # checa se a pilha está vazia
                break
        for i,j in g.items():                       # percorre todo grafo
            if not pilha:                           # checa se a pilha está vazia
                break
            if i == pilha[len(pilha)-1]:            # checa se o vértice atual é o último da pilha
                for x in j:                         # percorre os vértices adjacentes ao vértice atual
                    if x not in marcados:           # checa se o adjacente não está marcado
                        marcados.append(x)          # marca o adjacente
                        pilha.append(x)             # coloca esse no final da pilha
                        break
                    else:
                        if set(j).issubset(set(marcados)):  # checa se os vértices adjacentes já estão marcados
                            pilha.pop()                     # tira último vértice da pilha
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

for i in grafo.keys():
    print(i, "  |  ", end="")

r = input("Insira o vértice raiz")
dfs = depth_first_search(grafo, r)
print(dfs)