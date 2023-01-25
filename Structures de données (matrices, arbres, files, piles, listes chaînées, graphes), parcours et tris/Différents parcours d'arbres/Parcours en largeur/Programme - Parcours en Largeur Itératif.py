
# Imports:

from Programme_Classe_Arbre import *


# Programme:

def get_Hauteur(arbre):
    """
    arbre: Une instance de la classe Noeud
    renvoi: la hauteur de l'arbre
    """
    if arbre is not None:
        hauteurGauche = get_Hauteur(arbre.gauche)
        hauteurDroite = get_Hauteur(arbre.droite)
        if hauteurGauche > hauteurDroite:
            return hauteurGauche + 1
        else:
            return hauteurDroite + 1
    else:
        return 0


def ParcoursLargeurItératif(racine):  # 'racine' est un objet Noeud; il représente la racine d'un arbre ou d'un sous-arbre.
    if racine is not None and not racine.is_empty():  # Si l'arbre n'est pas vide:
        hauteur = get_Hauteur(racine)
        listeNiveau = list()  # On utilise une liste intermédiaire pour stocker les noeuds des niveaux
        listeNiveau.append(racine)
        while len(listeNiveau) != 0:  # Tant qu'il reste des noeuds à étudier
            noeud = listeNiveau.pop(0)  # Premier élément de la liste
            if noeud != None:  # On ajoute pas les feuilles (égales à None; ne peuvent pas être traitées)

                print(noeud.valeur)

                # On ajoute les noeuds fils à la fin de la liste, ce qui permet de traiter les noeuds par niveau et de gauche à droite dans l'arbre
                listeNiveau.append(noeud.gauche)
                listeNiveau.append(noeud.droite)


# Tests:
# On initialise l'arbre
arbre = Noeud()
arbre.insérer(10)
arbre.insérer(15)
arbre.insérer(10)
arbre.insérer(5)
arbre.insérer(9)
arbre.insérer(4)
arbre.insérer(6)
arbre.insérer(11)
# On lance le programme
ParcoursLargeurItératif(arbre)
# Résultat:
#10 5 15 4 9 11 6
