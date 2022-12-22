
class Graphe:

    def __init__(self, NbreSommets = None):
        # Créer un dictionnaire pour stocker la liste d'adjacence
        self.ListeAdjacence = {}

        # Matrice
        if NbreSommets is not None:
            self.V = NbreSommets
            self.graphe = [[0 for colonne in range(NbreSommets)] for ligne in range(NbreSommets)]

    # Ajouter une arête entre deux sommets
    def addArete(self, u, v):
        if v not in self.ListeAdjacence:
            self.ListeAdjacence[v] = []

        if u not in self.ListeAdjacence:
            self.ListeAdjacence[u] = []

        self.ListeAdjacence[u].append(v)

    # Ajouter une arête entre deux sommets

    def addArete_t(self, t):
        # t est de la forme (1, 2); 1 et 2 des arrêtes.
        # Cette méthode crée une liste d'adjence

        if t[0] not in self.ListeAdjacence:
            self.ListeAdjacence[t[0]] = [t[1]]
        else:
            self.ListeAdjacence[t[0]].append(t[1])

    def nombre_d_aretes(self):

        return len(self.ListeAdjacence)

    def sommets( self ):
        """
        Renvoie la liste des sommets du graphe.
        """
        ListeSommets = []
        for value in self.ListeAdjacence.values():
            ListeSommets += list(value)
        return list(set(ListeSommets))

    def est_un_sommet( self, s ):
        """
        Renvoie Vraie si 's' est un sommet du graphe
        """
        if s in self.sommets():
            return True
        else:
            return False

    def nombre_de_sommets(self):
        """
        Renvoie le nombre de sommets du graphe.
        """
        SomSommets = 0
        for value in self.ListeAdjacence.values():
            SomSommets += len(value)
        return SomSommets

    def aretes( self ):
        """
        Renvoie la liste des arêtes du graphe.
        """
        aret_ = []
        for debut in self.ListeAdjacence:
            for fin in self.ListeAdjacence[debut]:
                aret_.append((debut, fin))
        aret_.sort()
        return aret_


# aretes = [(1,2), (2,1), (1, 3), (2, 3)]
# gg = Graphe()
# for a in aretes:
#     gg.addArete_t(a)
# print(gg.ListeAdjacence)
# print(gg.nombre_d_aretes())
# print(gg.nombre_de_sommets())
# print(gg.sommets())
# print(gg.est_un_sommet(4))
# print(gg.est_un_sommet(3))
# print(gg.aretes())