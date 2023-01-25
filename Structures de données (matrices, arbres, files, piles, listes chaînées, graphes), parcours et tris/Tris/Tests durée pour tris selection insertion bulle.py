# -*- coding: UTF-8 -*-
import time
import random

# Test 1
n=5000
L1 = [random.randint(0,n-1) for k in range(n)]
L2 = L1.copy() # L2 est identique à L1
L3 = L1.copy()
L4 = L1.copy()


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
L1 = [random.randint(0,n-1) for k in range(n)]
L2 = L1.copy() # L2 est identique à L1
L3 = L1.copy()
L4 = L1.copy()


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



