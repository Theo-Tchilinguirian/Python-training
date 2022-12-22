
#Parcours en profondeur d’abord :
def ParcoursProf(graphe, sommet, visités = []):
    visités.append(sommet)
    print(sommet)
    for voisin in graphe[sommet]:
        if voisin not in visités:
            ParcoursProf(graphe, voisin, visités)


#Parcours en largeur d’abord :
def ParcoursLarg(graphe, sommet):
    file = [sommet]
    visités = [sommet]
    while not file == []:
        U = file.pop(0)
        for voisin in graphe[U]:
            if voisin not in visités:
                visités.append(voisin)
                file.append(voisin)
        print(U)


graphe = {1: [2, 3], 2: [1, 3, 5], 3: [1, 2, 4], 4:[5], 5:[]}
ParcoursLarg(graphe, 1)


# def RechercheCheminPlusCourt(graphe, début, fin, chemin = [], plusCourt = None):
#     chemin.append(début)
#     if début == fin:
#         return chemin
#     for voisin in graphe[début]:
#         if voisin not in chemin:
#             if plusCourt == None or len(chemin) < len(plusCourt):
#                 nouveau = RechercheCheminPlusCourt(graphe, voisin, fin, chemin, plusCourt)
#                 if nouveau != None:
#                     plusCourt = nouveau
#     return plusCourt


def RechercheCycle(graphe, sommet):
    niveaux = {sommet: None for sommet in graphe}
    niveaux[sommet] = 0
    file = [sommet]
    while not file == []:
        sommet = file.pop(0)
        for voisin in graphe[sommet]:
            if niveaux[voisin] is None:
                niveaux[voisin] = niveaux[sommet] + 1
                file.append(voisin)
            elif niveaux[voisin] >= niveaux[sommet]:
                return True
    return False

graphe = {1:[2, 3], 2: [1, 3], 3: [2, 1]}

print(RechercheCycle(graphe, 1))



# Recherche de la présence d’un chemin, d’un cycle :
def ExistCheminUV(graphe, u, v):  # Recherche s’il existe un chemin entre u et v  (parcours en largeur)
    file = []
    visités = []
    file.append(u)
    while file != []:
        sommet = file.pop(0)
        visités.append(sommet)
        for voisin in graphe[sommet]:
            if voisin == v:  # Si voisin égal v (destination), alors il existe un chemin de u à v
                return True
            if voisin not in visités:
                    file.append(voisin)
    # Pas de chemin entre u et v :
    return False


def ExistCycle(graphe):  # Recherche d’un cycle pour tous les sommets du graphe
    for sommet in graphe:
        if ExistCheminUV(graphe, sommet, sommet) == True:
            return True
    return False
