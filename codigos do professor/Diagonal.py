from random import randint
M=[0]*5
for i in range(5):
    M[i] = [0]*5
    for j in range (5):
       M[i][j] = randint(1,50)

print("Matriz gerada \n")
for i in range(0, 5):
    for j in range(0, 5):
        print("[{:^2}] ".format(M[i][j]),end='')
    print()

print("Diagonal principal")
for i in range(5):
    print("[{:^2}] ".format(M[i][i]), end='')

print("\nDiagonal Secundaria:")
for i in range(5):
    print("[{:^2}] ".format(M[i][4-i]), end='')






