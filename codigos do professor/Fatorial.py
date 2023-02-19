n = int(input("Digite um numero:"))
if (n<0):
    print("Nao existe fatorial de numeros negativos!")
else:
    fat = 1
    for i in range(n, 1, -1):
        fat *= i

    print("Fatorial =  ", fat)


    