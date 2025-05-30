# TODO: Refatorar esse código nojento

# exe A
def insere_vertice(g: dict[str, set], a, b):
    if a == b: return
    if a not in g: g[a] = set()
    if b not in g: g[b] = set()
    
    g[a].add(b)
    g[b].add(a)


# exe B
def imprime_grafo(g):
    for v,a in g.items():
        print("="*50)
        print(f'Vertice: {v}')
        print(f'Adjacentes: {a}')


def checa_vertice(g, v):
    return v in g.keys()

    
def imprime_aresta(g: dict):
    arestas = []
    
    for v, a in g.items():
        for i in a:
            if not (v+i in arestas or i+v in arestas):
                arestas.append(v+i)
    print(f"Arestas: {arestas}")

# exe C
def imprime_adjacencia(g, x):
    m=0
    n=0
    if not checa_vertice(g, x): return print("Vértice inexistente", end="")
    for v, a in g.items():
        if v==x: return print(a, end="")

# exe D
def verifica_aresta(g, v1, v2):
    x=0
    if not checa_vertice(g, v1): return print("Vértice inexistente", end="")
    if not checa_vertice(g, v2): return print("Vértice inexistente", end="")
    for v, a in g.items():
        for i in a:
            if v==v1 and i==v2:
                return print("Os vértices '{}' e '{}' estão ligados por uma aresta".format(v1, v2), end="")
    print("Os vértices '{}' e '{}' NÃO estão ligados por uma aresta".format(v1, v2), end="")

# exe E
def imprime_grau_vertice(g: dict, v):
    if not checa_vertice(g, v): print("Vértice inexistente", end="")
    else: print(len(g[v]))

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
                        if set(j).issubset(set(marcados)):        # checa se os vértices adjacentes já estão marcados
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
print("="*50)
imprime_aresta(grafo)

print("\n\n", grafo)

x = input("\nDeseja saber a adjacência de algum vértice? s/n: ")
if x=="s" or x=="sim":
    y = input("Qual vértice?: ")
    imprime_adjacencia(grafo, y)
x = input("\nDeseja saber a existência de uma aresta entre dois vértices? s/n: ")
if x=="s" or x=="sim":
    y = input("Insira o primeiro vértice: ")
    z = input("Insira o segundo vértice: ")
    verifica_aresta(grafo, y, z)
x = input("\nDeseja saber o grau de algum vértice? s/n: ")
if x=="s" or x=="sim":
    y = input("Qual vértice?: ")
    imprime_grau_vertice(grafo, y)

x = input("\nDeseja realizar uma busca por largura? s/n: ")
if x=="s" or x=="sim":
    y = input("Qual o vértice raiz?: ")
    print(breadth_first_search(grafo, y))

x = input("\nDeseja realizar uma busca por profundidade? s/n: ")
if x=="s" or x=="sim":
    y = input("Qual o vértice raiz?: ")
    print(depth_first_search(grafo, y))