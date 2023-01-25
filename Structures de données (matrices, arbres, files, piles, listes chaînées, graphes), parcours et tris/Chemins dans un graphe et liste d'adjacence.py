
from Absolument_Tout import *
from Classe_Graphe import *

def chemin(g, sommet_de_depart):  #g est une liste d'adj     +  # pas un chemin: c'est un parcours en largeur
    Visités = list()
    pile = File()
    pile.enfiler(sommet_de_depart)
    while not pile.est_vide():
        u = pile.défiler()
        if u not in Visités:
            Visités.append(u)
            for voisin in g[u]:
                pile.enfiler(voisin)
    return Visités


g = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
     }

print(chemin(g, 'A'))


"""
on enfile sommet_départ
longueur du chemin = 0
tant que la file n'est pas vide:
on s'arrête sur ce chemin si le sommet est sommet_arrivée (on return la longueur et le chemin)
on ajoute ce chemin à la liste des chemins
on enfile chaque sommet fils
et on ajoute 1 à la longueur du chemin parcourue
et on appelle à nouveau la fonction pour que l'on enfile les fils de ces fils
"""

def trouvChemin(graphe, sommet_départ, sommet_arrivée, chemin = [], longueur=0):
    file = File()
    file.enfiler(sommet_départ)
    u = None
    while not file.est_vide() or u == sommet_arrivée:
        u = file.défiler()
        chemin.append(u)
        longueur += 1
        for voisin in graphe[u]:
            file.enfiler(voisin)
            longueur += 1
    return longueur, chemin

"""
Algorithme chemin_le_plus_court(g, sommet_de_départ, sommet_arrivée):
    chemin <- liste vide
    visités <- liste vide
    file <- [[sommet_de_départ]]
    Si sommet_de_départ = sommet_arrivée:
        renvoyer("sommet_de_départ = sommet_arrivée")
    FinSi
    TantQue file est vraie (non vide):
        mettre l'élément d'indice 0 dans chemin
        u <- chemin[-1]
        Si u est n'est pas dans visités
            Pour tout voisin de u dans g:
                chemin_aux <- liste de chemin
                ajouter voisin à chemin_aux
                ajouter chemin_aux à file
                Si voisin = sommet_arrivée:
                    renvoyer chemin_aux
                FinSi
            FinPour
            ajouter u à visités
        FinSi
    FinTantQue
    renvoyer("Pas de chemin de sommet_de_départ aux sommet_arrivée")
"""

def phraseListeur(chaine_de_caractères):
    listt = []
    for car in chaine_de_caractères:
        for i in range(len(chaine_de_caractères)):
            if car == ' ':
                listt.append([])
                while carac != ' ':
                    listt[i].append(carac)


def chemin_le_plus_court(g, sommet_de_départ, sommet_arrivée):
    visités = []
    file = [[sommet_de_départ]]
    if sommet_de_départ == sommet_arrivée:
        return "sommet_de_départ = sommet_arrivée"
    while file is True:  # non vide
        chemin = file.pop(0)
        u = chemin[-1]
        if u not in visités:
            for voisin in g[u]:
                chemin_aux = list(chemin)
                chemin_aux.append(voisin)
                file.append(chemin_aux)
                if voisin == sommet_arrivée:
                    return chemin_aux
            visités.append(u)
    return "Pas de chemin de sommet_de_départ au sommet_arrivée"


g = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
     }
sommet_de_départ = 'A'
sommet_arrivée = 'F'
print(chemin_le_plus_court(g, sommet_de_départ, sommet_arrivée))

"""
2e heure: mettre internet pour test de vitesse de frappe et reddit SoT reaper fleeing megalodon
"""