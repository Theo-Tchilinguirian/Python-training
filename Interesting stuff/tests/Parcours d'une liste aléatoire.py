
from random import *

ListeAleatoire = [randint(0, 100) for k in range(1000)]
print(ListeAleatoire)
n = 0
for k in ListeAleatoire:
    if k == 69:
        n += 1
print(n)
for k in range(n):
    print('Nice !', k)  # Pour chaque élément de la liste étant égal à 69.


n = 50
x = 0
ListeAleatoire = list(set([randint(0, 100) for k in range(n)]))
while not len(ListeAleatoire) == n:  # Condition d'arrêt : n est 50.
    ListeAleatoire = list(set([randint(0, 100) for k in range(n)]))
    x += 1
    print(x)
print(ListeAleatoire)