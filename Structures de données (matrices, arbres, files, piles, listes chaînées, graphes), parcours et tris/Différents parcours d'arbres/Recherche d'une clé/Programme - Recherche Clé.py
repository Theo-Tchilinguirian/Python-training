
# Imports:

from Programme_Classe_Arbre import *


# Programme:

def Recherche(arbre, valeur):
    """
    Renvoie True si la valeur recherchée est dans l'arbre, False sinon.
    """

    if not arbre.is_empty():  # Si l'arbre n'est pas vide (True si non vide)
        noeud = arbre
        while True:
            if noeud.valeur < valeur:
                if noeud.droite is not None:  # Pas une feuille
                    noeud = noeud.droite
                else:  # valeur n'est pas dans l'arbre
                    print("valeur non trouvée dans l'arbre")
                    return False

            elif noeud.valeur > valeur:
                if noeud.gauche is not None:
                    noeud = noeud.gauche
                else:  # valeur n'est pas dans l'arbre
                    print("valeur non trouvée dans l'arbre")
                    return False

            else:  # noeud.valeur == valeur:
                print("valeur trouvée dans l'arbre")
                return True

    else:  # Si l'arbre est vide:
        arbre.valeur = valeur


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
recherche(arbre, 9)  # valeur trouvée dans l'arbre
recherche(arbre, 12)  # valeur non trouvée dans l'arbre
