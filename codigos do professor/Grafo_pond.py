
def imprime_grafo(G):
    for v,a in G.items():
        print("="*50)
        print('Vertice:', v)
        print('Adjacentes/Peso:', a)

def soma_pesos(G,v):
    if v in G:
        soma = 0
        for lista in G[v]:
            soma += lista[1]

        print("Soma dos pesos = ", soma)

G = {'A': [['B',2], ['C',3], ['D',1], ['E',2]],
     'B': [['A',2], ['C',1]],
     'C': [['A',3], ['B',1], ['F',2]],
     'D': [['A',1], ['F',4]],
     'E': [['A',2]],
     'F': [['C',2],['D',4]]}

# 1.) CRIAR A TABELA COM AS ARESTAS E ORDENA-LA
# 2.) ALGORITMO PARA INSERIR ARESTAS NA AGM = {}
# 3.) ALGORITMO PARA VERIFICAR SE O GRAFO É CONEXO (ESTÁ CONECTADO)
# 4.) ALGORITMO PARA VERIFICAR SE A ARESTA A SER INSERIDA FORMA CICLO NA AGM

# 5.) O ALGORITMO TERMINA QUANDO A AGM ESTIVER PRONTA OU SEJA:
#     TODOS OS VÉRTICES FORAM INSERIDOS E A AGM ESTÁ CONEXA
# 6.) Custo da AGM: SOMAR OS PESOS DAS ARESTAS INSERIDAS NA AGM

# tab = [['A','B',2], ['A','C',3],['A','D',1],['A','E',2],...]


imprime_grafo(G)
v = input("Digite o vértice para somar os pesos de suas adjacencias:")
soma_pesos(G,v)


