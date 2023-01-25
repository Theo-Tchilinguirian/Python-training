def ListPair(n):
    """
    Données: n un entier positif
    Résultat: Renvoie une liste des n premiers nombres pairs, n compris
    """
    ListPair = []
    for k in range(n + 1):  # Ou: ListPair += 2*k
        if k%2 == 0:
            ListPair += [k]

    return ListPair

