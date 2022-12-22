
# Imports:

from Programme_Classe_Arbre import *


# Programme:

def Supprimer(Arbre, Elt):
    """
    Supprime l'élément Elt dans l'arbre Arbre
    """

    if Arbre is None:  # Si l'arbre est vide:
        print(Elt, "non trouvé dans l'arbre")
    else:
        if Elt < Arbre.valeur:
            Supprimer(Arbre.gauche, Elt)  # On cherche à gauche

        elif Elt > Arbre.valeur:
            Supprimer(Arbre.droite, Elt)  # On cherche à droite

        else:  # Elt == Arbre.valeur:
            père = Arbre.précédent
            if père.droite is Arbre:
                père.droite = Arbre.gauche
                père.droite.droite = Arbre.droite
            elif père.gauche is Arbre:
                père.gauche = Arbre.droite
                père.gauche.gauche = Arbre.gauche
            del Arbre


def afficher(arbre, niveau=0):  # Pour illustrer les tests
    if arbre.droite:  # Si arbre.droite != None:
        afficher(arbre.droite, niveau + 1)
    print(niveau*"\t", arbre.valeur)
    if arbre.gauche:
        afficher(arbre.gauche, niveau+1)


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
print(20*'-')
afficher(arbre, niveau=0)
print(20*'-')
Supprimer(arbre, 9)
print(20*'-')
afficher(arbre, niveau=0)
print(20*'-')
Supprimer(arbre, 12)
print(20*'-')
afficher(arbre, niveau=0)
print(20*'-')
