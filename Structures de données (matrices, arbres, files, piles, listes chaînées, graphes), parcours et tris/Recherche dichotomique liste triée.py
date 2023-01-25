
def Rech_Dicho(liste, elt):
    """
    Recherche dichotomique dans une liste de nombres triés par ordre croissant.
    On peut d'abord trier la liste pour utiliser cette fonction.
    """

    i = int(len(liste) / 2)

    if len(liste) == 1:
        if liste[0] == elt:
            return 0
        else :
            return False
    if len(liste) == 0:
        return False
    if liste[i] == elt:
        return i

    elif liste[i] > elt:
        return Rech_Dicho(liste[:i], elt)
    elif liste[i] < elt:
        return Rech_Dicho(liste[i:], elt)


print(Rech_Dicho([1, 2, 3, 4, 5], 5))