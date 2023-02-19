# exe A
def insere_vertice(g, a, b):
    if a not in g:
        g[a]=[]
    if b not in g:
        g[b]=[]
    g[a].append(b)
    g[b].append(a)

# exe B
def imprime_grafo(g):
    for v,a in g.items():
        print("="*50)
        print('Vertice:', v)
        print('Adjacentes:', a)

def imprime_aresta(g):
    arestas = []
    for v,a in g.items():
        for i in a:
            x = v + i
            y = i + v
            s = 0
            for z in arestas:
                if z == y:
                   s += 1 
            if s == 0:
                arestas.append(x)
    print ("Arestas: ", arestas)

# exe C
def imprime_adjacencia(g, x):
    m=0
    n=0
    for v, a in g.items():
        if v==x: print(a, end="")
        else: m+=1
        n+=1
    print("Vértice inexistente " if m==n else "", end="")

# exe D
def verifica_aresta(g, v1, v2):
    x=0
    for v, a in g.items():
        for i in a:
            if v==v1 and i==v2:
                print("Os vértices '{}' e '{}' estão ligados por uma aresta".format(v1, v2), end="")
                x-=1
        if v!=v1 or i!=v2: x+=1
    if x==len(g.items()): print("Os vértices '{}' e '{}' NÃO estão ligados por uma aresta".format(v1, v2), end="")

# exe E
def imprime_grau_vertice(g, y):
    x=0
    for v, a in g.items():
        if v!=y: x+=1
    if x==len(g.items()): print("O vértice '{}' não existe".format(y))
    else: 
        for v, a in g.items(): 
            if v==y: print(len(a))


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

x = input("\nDeseja saber a adjacência de algum vértice? s/n")
if x=="s" or x=="sim":
    y = input("Qual vértice?")
    imprime_adjacencia(grafo, y)

x = input("\nDeseja saber a existência de uma aresta entre dois vértices? s/n")
if x=="s" or x=="sim":
    y = input("Insira o primeiro vértice")
    z = input("Insira o segundo vértice")
    verifica_aresta(grafo, y, z)

x = input("\nDeseja saber o grau de algum vértice? s/n")
if x=="s" or x=="sim":
    y = input("Qual vértice?")
    imprime_grau_vertice(grafo, y)