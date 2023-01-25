
def triSelection(tab):  # Compléxité n²
    for i in range(1, len(tab)-1):
        iMin = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[iMin]:
                iMin = j
        aux = tab[i]
        tab[i] = tab[iMin]
        tab[iMin] = aux


def triInsertion(tab):  # Compléxité n à n²
    n = len(tab)
    for i in range(1, n):
        aux = tab[i]
        j = i
        while j > 0 and tab[j-1] > aux:
            tab[j] = tab[j-1]
            j = j-1
        tab[j] = aux


def tri_bulle(tab):  # Compléxité n à n²
    change = True
    while change:
        change = False
        for i in range(0, len(tab)-2):
            if tab[i] > tab[i+1]:
                tab[i], tab[i+1] = tab[i+1], tab[i]
            change = True


# Algo glouton
def rendre_la_monnaie(pièces, somme):
    n = len(pièces)
    choix = [0 for k in range(n)]
    for i in range (0, n-1):
        while somme >= pièces[i]:
            somme -= pièces[i]
            choix[i] += 1
    return choix


pièces = [500, 200, 100, 50, 20, 12, 5, 2, 1]
somme = 800
monnaie = rendre_la_monnaie(pièces, somme)
print(monnaie)
somme = 650
monnaie = rendre_la_monnaie(pièces, somme)
print(monnaie)




# -*- coding: UTF-8 -*-
import time
import random

# Test 1
n=5000
L1 = [ random.randint(0,n-1) for k in range(n)]
L2 = L1.copy() # L2 est identique à L1
L3 = L1.copy()
L4 = [ random.randint(0,500-1) for k in range(500)]


debut = time.time()
triSelection(L2)
fin = time.time()
ecart = fin-debut
print (ecart)


debut = time.time()
triInsertion(L3)
fin = time.time()
print( fin-debut)


debut = time.time()
tri_bulle(L4)
fin = time.time()
print( fin-debut)

#---------------------------------------------------------------
# Test 2
n=50000
n=5000
L1 = [ random.randint(0,n-1) for k in range(n)]
L2 = L1.copy() # L2 est identique à L1
L3 = L1.copy()
L4 = L1.copy()


ebut = time.time()
triSelection(L2)
fin = time.time()
ecart = fin-debut
print (ecart)


debut = time.time()
triInsertion(L3)
fin = time.time()
print( fin-debut)


debut = time.time()
tri_bulle(L4)
fin = time.time()
print( fin-debut)
