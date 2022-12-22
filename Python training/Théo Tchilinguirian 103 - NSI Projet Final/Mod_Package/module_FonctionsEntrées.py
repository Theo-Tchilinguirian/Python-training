
"""
Ce module contient les définitions des fonctions d'entrées du programme.
"""

# Imports
import traceback
import Mod_Package.module_DATA as DATA
import Mod_Package.module_FonctionsAffichage as mod_Aff
import Mod_Package.module_FonctionsMétier as mod_Met

import os


def AffichMenuPrinc():
    """
    Fonction principale qui demande au joueur l'action à effectuer et vérifie sa réponse;
        - Le path vers le répertoire de travail principal est créé (là où se trouve Programme_Principal_Main_Program)
        - On initialise le choix de l'utilisateur

        - Des choix sont proposés à l'utilisateur:
            - Choisir 1, 2, ou 3 lancera des fonctions
            - Choisir 4 eteindra le jeu

    Entrées:
        - Pas d'entrées

    Sorties:
        - Pas de sorties
    """


    MainPath = os.getcwd()  # Répertoire de travail principal
    Choix = str()

    while Choix != 4:
        try:

            Choix = int(input("""
            1. Nouvelle Partie
            2. Charger une Partie
            3. Parties Enregistrées
            4. Quitter
            >>> """))

            if Choix == 1:
                # On initialise une nouvelle partie

                # On affiche les parties prééxistantes
                print("Choisir le nom d'une partie déja existante la remplacera par cette nouvelle sauvegarde")
                print("Parties non finies:")
                mod_Aff.AffichFilesDir(MainPath + DATA.FileSavePath)
                print("Parties finies:")
                mod_Aff.AffichFilesDir(MainPath + DATA.FileWonSavePath)

                # Choix du nom de la partie et des joueurs
                NomJeu = get_NomJeu()
                NomJoueur1, NomJoueur2 = get_NomJoueurs()

                # Création du plateau de jeu
                Plateau, CoordsJoueurs, JoueurActif, Opt_Tupl = mod_Met.init_NvPartie()
                mod_Met.set_BouclJeu(MainPath, Plateau, CoordsJoueurs, JoueurActif, Opt_Tupl, NomJeu, NomJoueur1, NomJoueur2)


            elif Choix == 2:

                Path = MainPath + DATA.FileSavePath  # On travaille sur les sauvegardes non terminées

                NomValide = False

                while NomValide == False:  # Boucle de test
                    try:
                        # On vérifie si il y a au moins une partie disponible
                        ListDir = os.listdir(Path)

                        if ListDir == []:  # Si il n'y a pas de parties enregistrées
                            print(DATA.MsgError2)
                            NomValide = True  # On sort de la boucle

                        else:

                            # On charge une partie enregistrée non finie

                            # On affiche les parties disponibles à charger
                            print("Conseil: Si vous choisissez une partie non finie dont le nom est le même que celui d'une partie finie, lorsque vous terminerez la partie non finie, elle écrasera la partie déja finie qui porte le même nom.")
                            print("Parties non finies:")
                            mod_Aff.AffichFilesDir(Path)
                            # On récupère le nom d'une partie  (Si le nom n'est pas disponible: on rentre dans le except avec une 'FileNotFoundError' error
                            NomJeu = get_NomJeuFromNumero(MainPath + DATA.FileSavePath)

                            NomJoueur1, NomJoueur2, Plateau, CoordsJoueurs, JoueurActif, Opt_Tupl = mod_Met.Charge_Jeu(MainPath, NomJeu)

                            mod_Met.set_BouclJeu(MainPath, Plateau, CoordsJoueurs, JoueurActif, Opt_Tupl, NomJeu, NomJoueur1, NomJoueur2)

                            NomValide = True  # Si aucune erreur n'a lieu, alors on sort de la boucle.

                    except FileNotFoundError:
                        print(DATA.MsgError3)
                        NomValide = False


            elif Choix == 3:

                # Affiche les parties enregistrées
                print("Conseil: Si vous choisissez le nom d'une partie prééxistante lors de la création d'une nouvelle partie, la partie prééxistante sera écrasée.")
                print("Parties non finies:")
                mod_Aff.AffichFilesDir(MainPath + DATA.FileSavePath)
                print("Les parties non finies peuvent être chargées pour les continuer; vous pouvez aussi modifier la partie dans le dossier des sauvegardes\n")
                print("Parties finies:")
                mod_Aff.AffichFilesDir(MainPath + DATA.FileWonSavePath)


            elif Choix == 4:
                pass  # On sort de la boucle et quitte le jeu

            else:
                print(DATA.MsgError5)

        except ValueError:
            print(DATA.MsgError1)

#----------------------------------------------------------------------------------------------------------------------#

def get_ChoixOpts():
    """
    Fonction qui demande au joueur les options facultatives à activer et vérifie sa réponse;
        - On initialise les valeurs par défaut des options facultatives

        - Le choix de l'utilisateur est vérifié
            - La boucle vérifie si les nombres 1, 2 ou 3 sont présents dans la réponse

        -  Les options sont contenues dans un tuple et renvoyées.

    Entrées:
        - Pas d'entrées

    Sorties:
        - Tupl_Opts:  Tuple contenant des booléens
    """


    #mettre valeur par défaut(non) et checks etc ... et mettre un tableau d'options, 1, 2, 3, le input contenant le tuple avec les virgules etc
    # Ajouter option passer tour oui non

    Opt_RandPos = False  # Les options facultatives sont initialisées à leurs valeurs de base
    Opt_GameMode = True
    Opt_SauterTour = False

    Tupl_Opts = (Opt_RandPos, Opt_GameMode, Opt_SauterTour)  # Tuple qui contient les options (initialisé aux valeurs par défaut)

    ChoixValide = False

    while ChoixValide == False:
        try:
            Choix = tuple(input("""\nChoisissez les options facultatives de la partie:
            1. Position aléatoire des joueurs (par défaut: désactivé)
            2. Jouer avec les règles de base (par défaut: activé)
            3. Permission de sauter son tour (par défaut: désactivé)
            entrez les numéros des options pour inverser leurs valeurs par défaut; séparez vos choix par un espace ou non. (ex: 1 32)
            laisser vide pour conserver les valeurs par défaut
            >>> """))

            if Choix == tuple():  # Si aucune option n'est choisie,
                pass  # Les options gardent leurs valeurs par défaut

            else:  # Si au moins une option est choisie,

                for Elt in Choix:
                    if Elt == ' ':
                        pass
                    elif int(Elt) == 1:
                        Opt_RandPos = True  # Si le joueur a choisi cette option, on inverse sa valeur de base.
                    elif int(Elt) == 2:
                        Opt_GameMode = False
                    elif int(Elt) == 3:
                        Opt_SauterTour = True

                    else:
                        raise ValueError  # Si on marque autre chose que 1, 2, 3 ou espace.

                Tupl_Opts = (Opt_RandPos, Opt_GameMode, Opt_SauterTour)  # On modifie la valeur de Tupl_Opts si au moins une option est choisie

            ChoixValide = True
        except ValueError:
            print(DATA.MsgError6)
            ChoixValide = False

    print()  # Saut de ligne

    return Tupl_Opts

#----------------------------------------------------------------------------------------------------------------------#

def get_ChoixDimPlat():
    """
    Fonction qui demande au joueur les dimensions du plateau de jeu;
        - Initialisation des dimensions du plateau

        - On rentre dans une première boucle; les conditions de sortie sont atteintes lorsque les deux choix de l'utilisateurs sont corrects
        - La deuxième couche de boucles sont des boucle qui vérifient si les valeurs des dimensions du plateau sont correctes

    Entrées:
        - Pas d'entrées

    Sorties:
        - NbLignPlateauInt:  Dimensions y (lignes) du plateau
        - NbColPlateauInt:  Dimensions x (colonnes) du plateau
    """


    # Initialisation des valeurs de base.
    NbLignPlateauStr, NbColPlateauStr = str(), str()
    NbLignPlateauInt, NbColPlateauInt = -1, -1

    while NbLignPlateauInt == -1 or NbColPlateauInt == -1:

        DimCorrect = False

        while DimCorrect == False:  # Boucle de try/except; vérification des inputs de l'utilisateur
            try:

                NbLignPlateauStr = input("Veuillez indiquer le nombre de lignes (min:3, max:26, défaut:6): ")
                NbLignPlateauInt = int(NbLignPlateauStr)

                if NbLignPlateauInt < 3 or NbLignPlateauInt > 26:
                    print(DATA.MsgError5)
                    DimCorrect = False  # == continue

                else:
                    DimCorrect = True  # On sort de la boucle

            except ValueError:  # Si le code essaie de transformer une lettre en entier (si l'utilisateur a tapé une lettre)

                if NbLignPlateauStr == '':
                    NbLignPlateauInt = 6  # Valeur par défaut
                    DimCorrect = True  # On sort de la boucle
                else:  # Si la valeur contenue n'est pas un string vide
                    print(DATA.MsgError1)
                    DimCorrect = False


        DimCorrect = False

        while DimCorrect == False:
            try:

                NbColPlateauStr = input("Veuillez indiquer le nombre de colonnes (min:4, max:26, défaut:8): ")
                NbColPlateauInt = int(NbColPlateauStr)

                if NbColPlateauInt < 4 or NbColPlateauInt > 26:
                    print(DATA.MsgError1)
                    DimCorrect = False

                else:
                    DimCorrect = True  # On sort de la boucle

            except ValueError:  # Si l'utilisateur choisi une chaine de caractère qui ne peut être transformée en entier

                if NbColPlateauStr == '':
                    NbColPlateauInt = 8  # Valeur par défaut
                    DimCorrect = True  # On sort de la boucle
                else:  # Si la valeur contenue n'est pas un string vide
                    print(DATA.MsgError1)
                    DimCorrect = False

        return NbLignPlateauInt, NbColPlateauInt

#----------------------------------------------------------------------------------------------------------------------#

def get_ChoixCasePos(Plateau, CoordsJoueurs, JoueurActif):
    """
    Fonction qui demande à l'utilisateur la case sur laquelle il souhaite se placer;
        - Les coordonnées du joueur actif sont calculés à partir du joueur actif et de la liste des coordonnées
        - On initialise les valeurs de Case et CoordsCase

        Case contient l'input de l'utilisateur et permet de créer CoordsCase:
            CoordsCase = (int(Case[1]), ord(Case[0]) - DATA.ValASCII) -> Si Case (l'input) = 'A1', CoordsCase sera les coordonnées de la case A1.

    Entrées:
        - Plateau:  Le plateau de jeu est utilisé dans le test de validité de la réponse utilisateur
        - CoordsJoueurs:  Liste de tuples contenant les coordonnées des joueurs
        - JoueurActif:  Le joueur qui joue ce tour

    Sorties:
        - CoordsCase:  Les coordonnées (validés) de la case choisie   (prend les valeurs 'q', '', ou un tuple de coordonnées (y, x))
    """


    CoordsJoueurActif = CoordsJoueurs[JoueurActif - 1]
    Case = str()
    CoordsCase = 'q'  # Si égal à 'q', alors on quitte le jeu

    while Case != 'q':
        try:

            Case = input("""
        Choisissez une case (exemples: A1; 'q' pour sauvegarder et quitter; ou laissez vide pour passer votre tour (si activé))
            >>> """.format(CoordsJoueurActif))

            if Case.lower() == 'q':  # Réponse prioritaire; Le joueur ne choisi pas de case et souhaite quitter
                break  # On renvoie 'q': le joueur quitte (à partir de set_BouclJeu)

            elif Case == '':
                CoordsCase = ''  # renvoie CoordsCase = ''; donc le joueur saute son tour (à partir de la fonction set_BouclJeu)
                break  # Le joueur a laissé son choix vide: il saute son tour


            else:

                CoordsCase = (int(Case[1]), ord(Case[0]) - DATA.ValASCII)

                # On lance la fonction suivante afin de tester la validité de la case choisie (test le plus sûr)
                mod_Met.check_IfCasePosDispo(Plateau, JoueurActif, CoordsCase)  # Test de validité du choix de l'utilisateur
                # Si ce test rate, il renvoie une erreur, on passe dans le except, le choix de la case étant invalide.
                # Choisir "AA", "AAA", "11", "1A", ou "X30", ne fonctionnera donc pas.

                break

        except:
            mod_Aff.AffichPlateau(Plateau)  # On affiche le plateau avant d'afficher l'erreur et de redemander le choix
            print(DATA.MsgError1)
            print("\n   Joueur {}, à vous de jouer !".format(JoueurActif))
            continue

    return CoordsCase

#----------------------------------------------------------------------------------------------------------------------#

def get_ChoixCaseDel(Plateau, JoueurActif):
    """
    Fonction qui demande à l'utilisateur la case qu'il souhaite supprimer;

        - On demande à l'utilisateur la case à supprimer

        - On vérifie si la case choisie est correcte
        Case contient l'input de l'utilisateur et permet de créer CoordsCase:
            CoordsCase = (int(Case[1]), ord(Case[0]) - DATA.ValASCII) -> Si Case (l'input) = 'A1', CoordsCase sera les coordonnées de la case A1.

    Entrées:
        - Plateau:  Le plateau de jeu est utilisé dans le test de validité de la réponse utilisateur
        - JoueurActif:  Le joueur qui joue ce tour

    Sorties:
        - CoordsCase:  Les coordonnées (validés) de la case choisie
    """


    print("   Joueur {}, essayez de piéger votre adversaire !".format(JoueurActif))

    CaseDispo = False

    while CaseDispo == False:
        try:

            Case = input("""
        Choisissez une case à enlever
            >>> """)


            CoordsCase = (int(Case[1]), ord(Case[0]) - DATA.ValASCII)

            # On lance la fonction suivante afin de tester la validité de la case choisie (test le plus sûr)
            mod_Met.check_IfCaseDelDispo(Plateau, CoordsCase)  # Test
            # Si ce test rate, on passe dans le except, le choix de la case étant invalide.
            # Choisir "AA", "AAA", "11", "1A", ou "X30", ne fonctionnera donc pas.
            CaseDispo = True  # On sort de la boucle

        except:
            mod_Aff.AffichPlateau(Plateau)  # On affiche le plateau avant d'afficher l'erreur et de redemander le choix
            print("\n   Joueur {}, essayez de piéger votre adversaire !".format(JoueurActif))
            print(DATA.MsgError1)
            continue

    return CoordsCase

#----------------------------------------------------------------------------------------------------------------------#

def get_NomJeu():
    """
    Fonction qui demande à l'utilisateur le nom d'un fichier pour le renvoyer;

        - On demande à l'utilisateur le numéro du fichier choisi

        - On vérifie si le numéro du fichier choisi n'est pas vide

        - On renvoie le nom du fichier

    Entrées:
        - Pas d'entrées

    Sorties:
        - NomJeu:  Le nom du fichier choisi par l'utilisateur (chaine de caractère)
    """


    NomDispo = False  # On initialise la boucle

    while NomDispo == False:  # Boucle qui vérifie si le nom de la sauvegarde est correct

        NomJeu = input("Choisissez le nom de votre partie: ")

        if NomJeu == '':
            print(DATA.MsgError1)
            continue

        else:
            NomDispo = True  # Le nom de la sauvegarde est correct; on sort de la boucle

    return NomJeu  # On renvoie le nom de la partie si il est correct

#----------------------------------------------------------------------------------------------------------------------#

def get_NomJeuFromNumero(Path):
    """
    Fonction qui demande à l'utilisateur le numéro d'un fichier et récupère le nom de ce fichier pour le renvoyer;

        - On initialise la liste des fichiers présent dans le path donné

        - On demande à l'utilisateur le numéro du fichier choisi

        - On vérifie si le numéro du fichier choisi est correct

        - On renvoie le nom du fichier correspondant (sans extension)

    Entrées:
        - Path:  Un chemin menant vers un dossier

    Sorties:
        - NomJeu:  Le nom du fichier correspondant au numéro choisi par l'utilisateur (sans l'extension) (chaine de caractère)
    """


    ListDir = os.listdir(Path)  # Liste des fichiers du dossier auquel path mène

    NomDispo = False  # On initialise la boucle

    while NomDispo != True:  # Boucle qui vérifie si le nom de la sauvegarde est correct

        try:

            NumeroPartie = int(input("Choisissez le numéro de la partie à charger: "))

            if NumeroPartie <= 0 or NumeroPartie > len(ListDir):
                print(DATA.MsgError5)  # Le numéro choisi est invalide et ne correspond à celui d'aucune partie
                continue

            else:
                NomJeu = ListDir[NumeroPartie - 1]  # On récupère le nom du fichier correspondant
                NomJeu = NomJeu.split('.')[0]  # On retire l'extension
                NomDispo = True  # Le numéro de la sauvegarde est correct; on sort de la boucle

        except ValueError:  # Si on entre une lettre, ...
            print(DATA.MsgError1)
            continue

        return NomJeu  # On renvoie le nom de la partie si il est correct

#----------------------------------------------------------------------------------------------------------------------#

def get_NomJoueurs():
    """
    Fonction qui demande aux utilisateurs leurs noms/leurs pseudonymes;

        Dans des boucles séparées:

            - On demande aux utilisateurs leur nom tour à tour

            - On vérifie si les noms sont corrects

        - On renvoie les noms des joueurs

        Le fait que les boucles soient séparées permet de ne pas revenir sur le premier choix si le second est incorrect

    Entrées:
        - Pas d'entrées

    Sorties:
        - NomJoueur1, NomJoueur2:  Les noms des joueurs (chaines de caractères)
    """


    NomJoueur1 = '1'
    NomJoueur2 = '2'  # On initialise le nom des joueurs

    NomDispo = False

    while NomDispo == False:

        NomJoueur1 = input("Choisissez le nom du joueur 1: ")

        if NomJoueur1 == '':
            print(DATA.MsgError1)
            continue

        else:
            NomDispo = True


    NomDispo = False

    while NomDispo == False:


        NomJoueur2 = input("Choisissez le nom du joueur 2: ")

        if NomJoueur2 == '':
            print(DATA.MsgError1)
            continue

        else:
            NomDispo = True

    return NomJoueur1, NomJoueur2  # On renvoie le nom des joueurs
