
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


def ParcoursLargeurRécursif(racine):  # 'racine' est un objet Noeud; il représente la racine d'un arbre ou d'un sous-arbre.
     """
     Fonction qui intialise la récursivité
     """
     hauteur = get_Hauteur(racine)
     niveau = 0
     AjoutNiveau(racine, hauteur, niveau)


def AjoutNiveau(racine, hauteur, niveau):
    """
    Fonction permettant de changer de niveau récursivement dans l'arbre
    """
    if niveau != hauteur:
        RechercheNiveau(racine, hauteur, niveau)
        AjoutNiveau(racine, hauteur, niveau + 1)


def RechercheNiveau(racine, hauteur, niveau):
    """
    Fonction qui va afficher la valeur du noeud/racine du sous-arbre
    """
    if racine is not None:  # On n'affiche pas les feuilles (qui sont égales à None)
         if niveau == 0:
             print(racine.valeur)
         else:  # Si niveau > 0:
             RechercheNiveau(racine.gauche, hauteur, niveau - 1)  # On baisse le compteur de niveau jusqu'a ce qu'on puisse afficher la valeur
             RechercheNiveau(racine.droite, hauteur, niveau - 1)


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
ParcoursLargeurRécursif(arbre)
# Résultat:
#10 5 15 4 9 11 6
