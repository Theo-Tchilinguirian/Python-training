
from Classe_Graphe import *
from Module_Maillon_Pile_File import *

def chemin(g, sommet_de_depart):  # Ne fonctionne pas avec une pile
    Visités = list()
    file = File()
    file.enfiler(sommet_de_depart)
    while not file.is_empty():
        u = file.defiler()
        if u not in Visités:
            Visités.append(u)
            for voisin in g.ListeAdjacence[u]:
                file.enfiler(voisin)
    return Visités


aretes = [('A','B'), ('A','C'), ('A', 'E'), ('B', 'A'), ('B', 'D'), ('B', 'E'), ('C', 'A'), ('C', 'F'), ('C', 'G'), ('D', 'B'), ('E', 'A'), ('E', 'B'), ('E', 'D'), ('F', 'C'), ('G', 'C')]
g = Graphe()
for a in aretes:
    g.addArete_t(a)
print(chemin(g, 'A'))

# Résultat obtenu avec une pile: ['A', 'E', 'D', 'B', 'C', 'G', 'F']
# Résultat obtenu avec une file: ['A', 'B', 'C', 'E', 'D', 'F', 'G']  (correct)