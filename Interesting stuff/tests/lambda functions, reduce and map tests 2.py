
f1 = lambda x : x*x
f2 = lambda x : x+x
foncs = [f1, f2]
aux = [[f1(i), f2(i)] for i in range(6)]
print(aux)

aux = [[i*i, i+i] for i in range(6)]
print(aux)

aux = []

f1 = lambda x : x*x
f2 = lambda x : x+x
foncs = [f1, f2]
aux = []
for i in range(6):
    aux.append(list(map(lambda x: x(i), foncs)))
print(aux)

aux = [list(map(lambda x: x(i), foncs)) for i in range(6)]
print(aux)

print("###########################################################################################################################""")








liste = [1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]

def list_func_1(l, n):
    matrice = list(map(list, zip(*[iter(l)]*n)))
    print(matrice)

def list_func_1(l, n):
    k = n
    aux = []
    auxx = []
    for i in range(len(l)):
        aux.append(l[i])
        if i == n-1:
            auxx.append(aux)
            aux = []
            n = n + k
    return auxx

print(list_func_1(liste, 5))

#lambda_var = [lambda l, n : if i == n-1 for i in range(len(l))]






from functools import reduce

l = [1, 5, 6, 3, 19]
s = reduce(lambda x1, x2: x1 + x2, l)
print(s)

def reduce2(l):
    intgr = 0
    for i in range(len(l)):
        intgr += l[i]
    return intgr

print(reduce2(l))

# def list_func_2(l, n):
#     k = n
#
#     aux = [l[i] for i in range(len(l))]
#     print(aux)
#     auxx = [[l[i] for i in range(len(l))] for i in range(len(l)) if i == n-1]
#
#     f1 = lambda auxx, aux: auxx.append(aux)
#     f2 = lambda aux : []
#     f3 = lambda n, k : n + k
#     foncs = [f1, f2, f3]
#     f4 = lambda auxx, aux: [f1(auxx, aux), f2(aux), f3(n, k)]
#
#     for i in range(len(l)):
#         aux.append(l[i])
#         if i == n-1:
#             [list(map(lambda x: x(i), foncs)) for i in range(len(l))]
#             auxx.append(aux)
#             aux = []
#             n = n + k
#
#     return auxx

    # for i in range(len(l)):
    #     aux.append(l[i])
    #     if i == n - 1:
    #         auxx.append(aux)
    #         aux = []
    #         n = n + k
    # return auxx

l = [1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
n = 5

#printlist_func_2(l, n))


#[list(map(lambda x: x)) for i in range(len(l))]








def helListe(l, n):
    f = lambda i: l[i:i+n]
    if len(l) % n == 0:
        return list(map(lambda i: l[i:i+n], range(0, len(l), n)))  # range est une liste d'indices d'éléments de l, le pas est de n. exemple : pour n=5, et len(l)=10 : range renvoie 0, 5 et 10.
    else:
        print("erreur :", len(l), " n'est pas multiple de", n)


l = [1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
n = 5
resultat = helListe(l, n)
print(resultat)
