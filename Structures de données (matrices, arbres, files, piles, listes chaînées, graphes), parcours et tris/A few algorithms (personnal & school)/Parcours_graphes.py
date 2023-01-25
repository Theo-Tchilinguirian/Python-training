
from Classe_Graphe import *
from Module_Maillon_Pile_File import *


# Parcours en largeur:

def ParcLargGraph(graphe, sommet):
    F = File()
    visité = {}
    for u in graphe.sommets():
        visité[u] = False
    visité[sommet] = True
    F.enfiler(sommet)
    while not F.is_empty():
        u = F.defiler()
        for v in graphe.ListeAdjacence[u]:
            if visité[v] == False:
                visité[v] = True
                F.enfiler(v)
        print(u)


# Parcours en profondeur:

def ParcProfGraph(graphe, sommet, visité):
    visité[sommet] = True
    print(sommet)
    for v in graphe.ListeAdjacence[sommet]:
        if visité[v] == False:
            ParcProfGraph(graphe, v, visité)



aretes = [(3, 1), (3, 2), (1, 3), (1, 4), (1, 5), (1, 6), (4, 1), (4, 5), (5, 1), (5, 4), (6, 1), (2, 3)]
graph = Graphe()
for a in aretes:
    graph.addArete_t(a)

print(ParcLargGraph(graph, 1))


graphe = Graphe()
for a in aretes:
    graphe.addArete_t(a)
visité = {}
for u in graphe.sommets():
    visité[u] = False

print(ParcProfGraph(graphe, 1, visité))
