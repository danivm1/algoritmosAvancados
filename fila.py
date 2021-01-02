def bota(f, x):
    f.append(x)

def tira(f):
    f.pop(0)

f = []

while True:
    x = input("Insira o vertice: ")

    if x == "fim":
        break

    bota(f, x)

while True:
    x = input("Remover?")
    if x == "s":
        tira(f)
        for i in f:
            print(i)
    else:
        break

print(f)