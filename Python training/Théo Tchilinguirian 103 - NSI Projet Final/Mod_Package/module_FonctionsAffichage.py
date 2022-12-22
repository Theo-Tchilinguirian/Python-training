
"""
Ce module contient les définitions des fonctions d'affichage' du programme.
"""

# Imports
import Mod_Package.module_DATA as DATA

import os


def AffichPlateau(Plateau):
    """
    Fonction qui affiche le plateau de jeu;
        - Calcul des dimensions du plateau

        - Création de l'en-tête du plateau

        - Affichage des éléments du plateau ligne par ligne (lignes numérotées)

    Entrées:
        - Plateau:  Le plateau de jeu

    Sorties:
        - Pas de sorties
    """

    NbLignPlateau, NbColPlateau = len(Plateau) - 1, len(Plateau[0]) - 1  # Initialisation des dimensions du plateau (hors cadre)

    # Entête (lettres de A à Z)
    ###
    print(8 * '\n')
    print("   |", end='')
    for k in range(1, NbColPlateau):
        print(" {} |".format(chr(k + DATA.ValASCII)), end='')
    ###

    print("\n" + (NbColPlateau) * "----", end='')
    for i in range(1, NbLignPlateau):
        print()
        if len(str(i)) == 2:
            print("{} | ".format(i), end='')  # Numérotation des lignes (de 10 à 26)
            # On enleve un espace pour ne pas décaler tout le tableau à cause de la taille du nombre
        else:
            print(" {} | ".format(i), end='')  # Numérotation des lignes (de 1 à 9)

        for j in range(1, NbColPlateau):
            ValActiv = Plateau[i][j]
            if ValActiv == 0:  # Si l'élément est un 0, la case est libre
                print("  | ", end='')
            elif ValActiv == 3:  # Si l'élément est un 3, la case est vide
                print("X | ", end='')
            else:  # Si l'élément est un 1 ou un 2, la case est un joueur
                print("{} | ".format(ValActiv), end='')

        print()
        print((NbColPlateau) * "----", end='')  # Fin du tableau
    print('\n')  # Double saut de ligne

#----------------------------------------------------------------------------------------------------------------------#

def AffichFilesDir(Path):
    """
    Fonction qui affiche les fichiers contenus dans un dossier;
        - Initialisation de la liste des fichiers contenus dans le dossier

        - Affichage des éléments numérotés

    Entrées:
        - Path:  Le chemin menant au dossier

    Sorties:
        - Pas de sorties
    """

    ListDir = os.listdir(Path)

    if ListDir == []:  # Si il n'y a pas de parties sauvegardées
        print("Aucune partie sauvegardée")

    else:  # Sinon, on affiche les noms des parties sauvegardées

        for i in range(len(ListDir)):

            print("{}. {}".format(i + 1, ListDir[i]))

    print()  # Saut de ligne
