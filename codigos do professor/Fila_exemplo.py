def Inserir(F, Fim, v):
    F.insert(Fim, v)

def Remover(F, Inicio):
    F.pop(Inicio)

F = []*50
Inicio=0
Fim=0

while True:
    v = input("Digite o vértice ou Fim para encerrar:")
    if (v=='Fim'):
        break
    Inserir(F, Fim, v)
    Fim += 1

print ("Fila: ", F)

print("Removendo o elemento: ", F[Inicio])
Remover (F, Inicio)
Fim -= 1

print ("Fila: ", F)





