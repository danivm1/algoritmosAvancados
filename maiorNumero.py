import numpy as np
from random import randint

# função acha maior
def maior(vet):
    m=vet[0]
    for i in range(1,10):
        if (m<vet[i]):
            m=vet[i]
    
    return m


# função main
vet = np.arange(10)

for i in range(10):
    vet[i] = randint(0,100)

m = maior(vet)
print(vet)
print(m)