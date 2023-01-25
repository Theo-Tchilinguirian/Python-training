
# D'abord les classes piles, files, noeuds, maillons, graphes ...

class Maillon:
    def __init__(self, donnée, suivant=None):
        self.donnée = donnée
        self.suivant = suivant


class Pile:
    def __init__(self, StalineEstMort=None, taille=0):
        self.sommet = StalineEstMort
        self.taille = taille

    def est_vide(self):
        return self.taille == 0

    def empiler(self, valeur):
        self.sommet = Maillon(valeur, self.sommet)
        self.taille += 1

    def dépiler(self):
        if not self.est_vide():
            renvoi = self.sommet.donnée
            self.sommet = self.sommet.suivant
            self.taille -= 1
            return renvoi


class File :
    def __init__(self, tête=None, taille=0):
        self.tête = tête
        self.taille = taille

    def est_vide(self):
        return self.taille == 0

    def enfiler(self, valeur):
        if self.est_vide():
            self.tête = Maillon(valeur, None)  # Valeur de base de suivant: None
        else:
            maillon = self.tête
            while maillon.suivant is not None:
                maillon = maillon.suivant
            maillon.suivant = Maillon(valeur, None)  # Valeur de base de suivant: None
        self.taille += 1

    def défiler(self):
        if not self.est_vide():
            renvoi = self.tête.donnée
            self.tête = self.tête.suivant
            self.taille -= 1
            return renvoi


class Noeud:  # Ou Arbre
    def __init__(self, valeur, parent=None, gauche=None, droit=None):
        self.parent = parent
        self.donnée = valeur
        self.gauche = gauche
        self.droit = droit

    def insérer(self, valeur):
        if valeur < self.donnée:
            if self.gauche is not None:
                self.gauche.insérer(valeur)
            else:
                self.gauche = Noeud(self, valeur)  # Valeur de base de fils gauche et fils droit: None
        elif valeur > self.donnée:
            if self.droit is not None:
                self.droit.insérer(valeur)
            else:
                self.droit = Noeud(self, valeur)  # Valeur de base de fils gauche et fils droit: None

    def taille(self):
        if self is not None:
            return 1 + self.gauche.taille() + self.droit.taille()
        else:
            return 0

    def hauteur(self):
        if self is not None:
            return 1 + max(self.gauche.hauteur(), self.droit.hauteur())
        else:
            return 0

    def parcoursPréfixe(self):
        if self is not None:
            print(self.donnée)
            self.gauche.parcoursPréfixe()
            self.droit.parcoursPréfixe()

    def parcoursInfixe(self):
        if self is not None:
            self.gauche.parcoursInfixe()
            print(self.donnée)
            self.droit.parcoursInfixe()

    def parcoursSuffixeOuPostfixe(self):
        if self is not None:
            self.gauche.parcoursSuffixeOuPostfixe()
            self.droit.parcoursSuffixeOuPostfixe()
            print(self.donnée)

    def parcoursLargeur(self):
        file = File()
        file.enfiler(self)
        while not file.est_vide():
            noeud = file.défiler()
            print(noeud)
            if noeud.gauche is not None:
                file.enfiler(noeud.gauche)
            if noeud.droit is not None:
                file.enfiler(noeud.droit)


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
                

# Le programme principal et les chemins


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
    while len(file) > 0:  # non vide
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
