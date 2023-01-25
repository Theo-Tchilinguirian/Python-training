def helListe(l, n):
    if len(l) % n == 0:
        return list(map(lambda i: l[i:i+n], range(0, len(l), n)))  # range est une liste d'indices d'éléments de l, le pas est de n. exemple : pour n=5, et len(l)=10 : range renvoie 0, 5 et 10.
    else:
        print("erreur :", len(l), " n'est pas multiple de", n)


l = [1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
n = 5
resultat = helListe(l, n)
print(resultat)
