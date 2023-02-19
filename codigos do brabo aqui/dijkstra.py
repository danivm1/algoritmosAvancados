# Feito por Daniel, Helena e Janaina

import sys
import numpy as np


order = int(input('Informe a quantidade de cidades: '))
# order = 5

grafo = np.arange(order*order).reshape(order,order)

for i in range(order):
    for j in range(order):
        print('Informe a distância da cidade {} à cidade {}: '.format(i, j), end="")
        grafo[i][j] = int(input())

# grafo = [[0, 10, 0, 5, 0], [0, 0, 1, 2, 0], [0, 0, 0, 0, 2], [0, 3, 9, 0, 2], [7, 0, 6, 0, 0]]

for i in range(order):
    for j in range(order):
        print(grafo[i][j], end=" ")
    print()

origin = int(input("Origem: "))
destiny = int(input("Destino: "))

# origin = 0
# destiny = 2
mark = ['']*order
heapDist = ['']*order
prior = [-1]*order

for i in range(order):
    mark[i] = False
    heapDist[i] = sys.maxsize

city = origin
heapDist[city] = 0

while (city != destiny) and (city != -1):
    for i in range(order):
        if (grafo[city][i] != 0) and (not mark[i]):
            newDist = heapDist[city] + grafo[city][i]
            if newDist < heapDist[i]:
                heapDist[i] = newDist
                prior[i] = city

    mark[city] = True
    minimun = sys.maxsize
    city = -1

    for i in range(order):
        if (not mark[i]) and (heapDist[i] < minimun):
            minimun = heapDist[i]
            city = i

inversePath = []
path = []

if city == destiny:
    print("O caminho mais curto é: ", end="")
    inversePath.append(city)

    while city != origin:
        city = prior[city]
        inversePath.append(city)

    for i in range(len(inversePath)-1,-1,-1):
        path.append(inversePath[i])

    for i in path:
        print(i, end=" ")

else:
    print("Não existe caminho unindo as duas cidades")