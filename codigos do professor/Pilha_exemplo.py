def Push(P, topo, v):
    P.insert (topo,v)

# pop remove o ultimo elemento da pilha
def Pop(P):
    P.pop()

P = []*50
topo = 0
while True:
    v = input("Digite o vértice a inserir ou Fim para encerrar: ")
    if v == 'Fim':
        break
    Push (P, topo, v)
    topo += 1

print("Pilha: ", P)

topo -= 1
print("Removendo da pilha o vértice:", P[topo])
Pop(P)
print("Pilha: ", P)

topo -= 1
print("Removendo da pilha o vértice:", P[topo])
Pop(P)
print("Pilha: ", P)






