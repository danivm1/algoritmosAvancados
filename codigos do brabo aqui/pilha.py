def bota(p, x):
    p.append(x)

def tira(p, fim):
    p.pop(fim)

p=[]

fim=0
while True:
    x = input("Insira o vertice: ")

    if x == "fim":
        break

    bota(p, x)
    fim += 1

fim -= 1

while True:
    x = input("Remover?")
    if x == "s":
        tira(p, fim)
        fim -= 1
        for i in p:
            print(i)
    else:
        break

print(p)