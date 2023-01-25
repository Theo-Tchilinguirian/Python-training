def ListImpair(n):
    """
    Données: n un entier positif
    Résultat: Renvoie une liste des n premiers nombres impairs, n compris
    """
    ListImpair = []
    for k in range(n + 1):  # Ou: ListPair += 2*k
        if k%2 == 1:
            ListPair += [k]

    return ListImpair

