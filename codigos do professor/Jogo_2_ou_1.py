a = int(input("A - Digite 2 ou 1:"))
b = int(input("B - Digite 2 ou 1:"))
c = int(input("C - Digite 2 ou 1:"))

if (a==b and a==c):
    print("Jogo terminou empatado!")
else:
    if (a==b):
        print("C é o vencedor!")
    else:
        if (b==c):
            print("A é o vencedor!")
        else:
            print("B é o vencedor!")
