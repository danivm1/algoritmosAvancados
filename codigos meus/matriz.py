import random
import numpy as np

m = np.arange(25).reshape(5,5)

for i in range(5):
    for j in range(5):
        m[i][j] = random.randint(0,50)

for i in range(5):
    for j in range(5):
        print(m[i][j], end="")
        if(j>=0 and j<=3):
            if(m[i][j]>=0 and m[i][j]<=9):
                print("   |  ", end="")
            else:
                print("  |  ", end="")
    print()

print("\n\nDiagonal principal:")
for i in range(5):
    for j in range(5):
        if(i==j):
            print(m[i][j], end="")
            if(j>=0 and j<=3):
                print("  |  ", end="")