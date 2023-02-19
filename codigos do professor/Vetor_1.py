from random import randint
L=[]
for i in range(10):
    L.append(randint(1,50))

print(L)
menor = L[0]
maior = L[0]

for i in range(1,10):
    if (L[i] < menor):
        menor = L[i]
    else:
        if (L[i] > maior):
            maior = L[i]

print("Maior valor = ", maior)
print("Menor valor = ", menor)


