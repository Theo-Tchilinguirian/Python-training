
"""
Ce module contient les définitions des fonctions de travail du programme.
"""

# Imports
import traceback
import Mod_Package.module_DATA as DATA
import Mod_Package.module_FonctionsAffichage as mod_Aff
import Mod_Package.module_FonctionsEntrées as mod_Ent

import os

from random import randint

def init_NvPartie():
    """
    Fonction principale qui initialise une nouvelle partie;
        - Obtention des options facultatives
        - Obtention des dimensions voulues du plateau
        - Création du plateau avec cadre (sans joueur)

        - Calcul des coordonnées des coins du plateau
        - Placement des joueurs sur le plateau

        - Initialisation du premier joueur.

    Entrées:
        - Pas d'entrées

    Sorties:
        - Plateau:  Le plateau construit (avec cadre et joueurs)
        - CoordsJoueurs:  Les coordonnées des joueurs
        - JoueurActif:  Le premier joueur actif (celui qui joue au premier tour)
        - Opt_Tupl:  Les options facultatives choisies
    """


    Opt_Tupl = mod_Ent.get_ChoixOpts()
    NbLignPlateau, NbColPlateau = mod_Ent.get_ChoixDimPlat()  # Obtention du choix des dimensions du plateau de jeu
    Plateau = init_DimPlat(NbLignPlateau, NbColPlateau)  # Création du plateau

    CoordsCoins_Tupl = get_CoordsCoins(NbLignPlateau, NbColPlateau)  # Obtention des coordonnées des coins du plateau
    CoordsMilieuJoueur1, CoordsMilieuJoueur2 = get_CoordsMilieu(CoordsCoins_Tupl)
    Plateau, CoordsJoueurs = init_PosJoueurs(Plateau, CoordsMilieuJoueur1, CoordsMilieuJoueur2, Opt_Tupl)  # Placement des joueurs

    JoueurActif = DATA.PremierJoueur  # Le joueur actif est le 'Premier Joueur' (voir module DATA)

    return Plateau, CoordsJoueurs, JoueurActif, Opt_Tupl

#----------------------------------------------------------------------------------------------------------------------#

def init_DimPlat(NbLignPlateau, NbColPlateau):
    """
    Fonction dynamique qui va construire un plateau selon les dimensions choisies par l'utilisateur;
        - Initialisation du plateau à vide

        - Construction du plateau et du cadre

    Entrées:
        - NbLignPlateau, NbColPlateau:  Les dimensions choisies par l'utilisateur pour le plateau

    Sorties:
        - Plateau:  Le plateau construit
    """


    # Initialisation du plateau
    Plateau = []

    for n in range(NbLignPlateau + 2):  # On ajoute des lignes et des colonnes qui correspondent aux limites (cachés), au cadre.
        Plateau.append([])  # Ajout des lignes

        for m in range(NbColPlateau + 2):
            if (m == 0 or n == 0) or (m == (NbColPlateau + 1) or n == (NbLignPlateau + 1)):
                Plateau[n].append(3)  # Ajout des limites, du "cadre"
            else:
                Plateau[n].append(0)  # Ajout des cases libres.

    return Plateau  # On renvoie le plateau construit.

#----------------------------------------------------------------------------------------------------------------------#

def get_CoordsCoins(NbLignPlateau, NbColPlateau):
    """
    Fonction qui calcule les coordonnées des coins du plateau;

    Entrées:
        - NbLignPlateau, NbColPlateau:  Les dimensions choisies par l'utilisateur pour le plateau
    Sorties:
        - CoordsCoins_Tupl: un tuple contenant les coordonnées des quatres coins du plateau (les coordonnées sont de la forme (y, x), ou (lignes, colonnes))
    """


    CoordsCoinHautGauche = (1, 1)  # Coin en haut à gauche
    CoordsCoinBasDroit = (NbLignPlateau, NbColPlateau)  # Coin en bas à droite
    CoordsCoinHautDroit = (1, NbColPlateau)  # Coin en haut à droite
    CoordsCoinBasGauche = (NbLignPlateau, 1)  # coin en bas à gauche

    CoordsCoins_Tupl = (CoordsCoinHautGauche, CoordsCoinBasDroit, CoordsCoinHautDroit, CoordsCoinBasGauche)
    # Tuple qui contient les coordonnées des quatres coins

    return CoordsCoins_Tupl

#----------------------------------------------------------------------------------------------------------------------#

def get_CoordsMilieu(CoordsCoins_Tupl):
    """
    Fonction qui calcule la position des joueur sur le plateau;

    Entrées:
        - CoordsCoins_Tupl: un tuple contenant les coordonnées des quatres coins du plateau (les coordonnées sont de la forme (y, x), ou (lignes, colonnes))

    Sorties:
        - CoordsMilieuJoueur1, CoordsMilieuJoueur2:  Les coordonnées des joueurs à peu près centrés sur le milieu du plateau
    """


    # int() retire la partie après la virgule tandis que round() arrondie à l'entier supérieur (round(3.4) = 3; round(3.5) = 4.

    CoordsMilieuJoueur1 = int((CoordsCoins_Tupl[0][0] + CoordsCoins_Tupl[3][0]) / 2), 1  # coordonnées (y coin haut gauche + y bas gauche; 1)
    CoordsMilieuJoueur2 = round((CoordsCoins_Tupl[2][0] + CoordsCoins_Tupl[1][0]) / 2 + 0.1), CoordsCoins_Tupl[2][1]  # coordonnées (y coin haut gauche + y bas gauche; nombre de colonnes)

    return CoordsMilieuJoueur1, CoordsMilieuJoueur2

#----------------------------------------------------------------------------------------------------------------------#

def init_PosJoueurs(Plateau, CoordsMilieuJoueur1, CoordsMilieuJoueur2, Opt_Tupl):
    """
    Fonction qui place les joueurs sur le plateau;
        - Obtention de la valeur de l'option de position aléatoire
        - Initialisation des dimensions du plateau
        - Initialisation des coordonnées des joueurs à vide

        - Les joueurs sont placés sur le plateau selon une position aléatoire ou au milieu de la première et dernière colonnes du plateau

        - Les coordonnées des joueurs sont contenus dans une liste

    Entrées:
        - Plateau:  le plateau de jeu avec le cadre; sans les joueurs

    Sorties:
        - Plateau:  Le plateau construit (avec cadre et joueurs)
        - CoordsJoueurs:  Liste de tuples contenant les coordonnées (y, x) (lignes, colonnes) des joueurs
    """


    # Initialisation des valeurs (nombres de colonnes, lignes du plateau; et coordonnées des joueurs; et une valeur aléatoire)
    Opt_RandPos = Opt_Tupl[0]  # initialisation de l'option de position aléatoire des joueurs sur le plateau
    NbLignPlateau, NbColPlateau = len(Plateau) - 1, len(Plateau[0]) - 1
    CoordsJoueur1, CoordsJoueur2 = (), ()



    if Opt_RandPos == True:  # Si l'option de position aléatoire est activée
        while CoordsJoueur1 == CoordsJoueur2:  # Si les coordonnées aléatoires sont les mêmes, ont recommence le tirage.
            CoordsJoueur1 = (randint(1, NbLignPlateau - 1), randint(1, NbColPlateau - 1))
            CoordsJoueur2 = (randint(1, NbLignPlateau - 1), randint(1, NbColPlateau - 1))  # Hors Bordures (on commence à 1, on finit à x-1)

    else:  # Positions basées sur les coins du plateau

         CoordsJoueur1 = CoordsMilieuJoueur1  # Coin haut gauche
         CoordsJoueur2 = CoordsMilieuJoueur2  # Coin bas droit

    Plateau[CoordsJoueur1[0]][CoordsJoueur1[1]] = 1  # On place les pions sur leurs cases
    Plateau[CoordsJoueur2[0]][CoordsJoueur2[1]] = 2

    CoordsJoueurs = [CoordsJoueur1, CoordsJoueur2]  # Liste (modifiable) de tuples (contenant les coordonnées (y, x) des joueurs)

    return Plateau, CoordsJoueurs

#----------------------------------------------------------------------------------------------------------------------#

def set_BouclJeu(MainPath, Plateau, CoordsJoueurs, JoueurActif, Opt_Tupl, NomJeu, NomJoueur1, NomJoueur2):
    """
    Fonction principale qui fait tourner l'algorithme du jeu;
        - On demande au joueur la case sur laquelle il souhaite se placer
        - On vérifie cette case

        - On lui demande la case à supprimer (si les regles du jeu de base ont été choisies)
        - On vérifie sa réponse

        - On vérifie si il y a un gagnant
        - Si oui, on désigne un gagnant et le jeu s'arrête
        - Si non, on change de joueur et on continue

    Entrées:
        - MainPath:  Le chemin absolu menant au programme principal ( " Programme_Principal_Main_Program " )
        - Plateau:  Le tableau de jeu (liste de listes)
        - CoordsJoueurs:  Liste de Tuples contenant chacun les coordonnées des joueurs 1 et 2 (coordonnées de la forme (y, x) )
        - JoueurActif:  Le joueur qui doit jouer
        - Opt_Tupl:  Tuple renseignant sur l'état des options facultatives (si elles sont activées ou non)
        - NomJeu:  Le nom de la partie (nom de la sauvegarde)
        - NomJoueur1:  Le nom du joueur 1 (permet de différencier les deux joueurs dans le fichier de sauvegarde)  (espérons seulement qu'ils n'aient pas le même nom)
        - NomJoueur2:  Le nom du joueur 2

    Sorties:
        - Pas de dessert
    """


    # elle contient les coordonnées du joueur dont c'est le tour.
    ModeDeJeuBase = Opt_Tupl[1]  # Le mode de jeu. Valeur True: le mode de jeu de base; Valeur False: mode de jeu généré par la non-relecture des règles du jeu par moi.
    Opt_SauterTour = Opt_Tupl[2]

    Perdant = 0  # Initialisation de la boucle
    Quitter = False

    # Boucle principale du jeu
    while Perdant == 0 and Quitter == False:  # Tant qu'il n'y a pas de gagnant, et tant que le joueur ne quitte pas.

        mod_Aff.AffichPlateau(Plateau)  # On affiche le plateau

        print("   Joueur {}, à vous de jouer !".format(JoueurActif))

        CasePosDispo = False  # Initialisation de la boucle
        # CasePosDispo contient si la case choisie pour poser le pion est disponible

        # Tout d'abord, le joueur choisi sur quelle case il veux se rendre
        # On entre dans la boucle qui vérifie si le choix de la case est correct
        while CasePosDispo != True and Quitter != True:  # Tant qu'il n'y a pas de case disponible, et tant que le joueur ne quitte pas, et tant que le joueur ne saute pas son tour (et que l'option pour sauter son tour est activée), alors on vérifie si la case choisie est disponible pour placer le pion du joueur

            # On demande son choix à l'utilisateur
            CoordsCase = mod_Ent.get_ChoixCasePos(Plateau, CoordsJoueurs, JoueurActif)

            if CoordsCase == 'q':  # Le joueur quitte la partie
                # On demande si le joueur veux sauvegarder ou non avant de quitter (boucle qui vérifie si la réponse est correcte)
                ChoixSauv = str()
                while ChoixSauv.lower() != 'oui' or 'non':  # Le joueur doit choisir entre oui et non

                    ChoixSauv = input("""Voulez vous sauvegarder avant de quitter? (oui/non)
                          >>> """)

                    if ChoixSauv.lower() == 'oui':  # Le joueur quitte, et le jeu est sauvegardé
                        Perdant, Gagnant = 0, int()  # La partie n'est pas terminée; on sauvegarde donc une partie chargeable
                        Save_Jeu(MainPath, NomJeu, NomJoueur1, NomJoueur2, Plateau, CoordsJoueurs, JoueurActif, Opt_Tupl, Perdant, Gagnant)
                        break  # renvoie CoordsCase = 'q'; donc on quitte le jeu (à partir de la fonction set_BouclJeu)

                    elif ChoixSauv.lower() == 'non':
                        break  # On quitte sans sauvegarder

                    else:
                        print(DATA.MsgError4)  # La boucle se relance (conditions d'arrêt non valides)
                Quitter = True  # On sort de la boucle

            # Si le joueur ne veux pas quitter; ->

            elif CoordsCase == '':  # Si le joueur a choisi la case sur laquelle il se trouve; il passe son tour (seulement si l'option a été choisie; sinon, la case est juste invalide)
                if Opt_SauterTour == True:  # L'option pour sauter son tour est activée; on passe notre tour
                    print("\n ----->  Vous passez votre tour  <----- ")  # On sort de la boucle
                    break

                elif Opt_SauterTour == False:  # Option désactivée; on renvoie une erreur
                    CasePosDispo = False  # Le joueur a tenté de sauter son tour alors que l'option n'était pas activée
                    mod_Aff.AffichPlateau(Plateau)  # On affiche le plateau
                    print(DATA.MsgError1)
                    print("\n   Joueur {}, à vous de jouer !".format(JoueurActif))
                    continue

            else:  # Le joueur ne saute pas son tour: on vérifie si la case choisie est disponible

                CasePosDispo = check_IfCasePosDispo(Plateau, JoueurActif, CoordsCase)  # On vérifie si la case est disponible

                if CasePosDispo == False:
                    mod_Aff.AffichPlateau(Plateau)  # On affiche le plateau avant d'afficher l'erreur et de redemander le choix
                    print(DATA.MsgError1)
                    print("\n   Joueur {}, à vous de jouer !".format(JoueurActif))
                    continue

                else:  # La case est disponible, on peut sortir de la boucle et passer aux prochaines étapes
                    break
            # Fin de boucle (boucle de choix de la case où placer le joueur)


        if CoordsCase == 'q':
            break  # Break est utilisé afin de ne pas passer dans les conditions ultérieurs, et sortir du jeu sans demander à l'utilisateur quelle case il veux supprimer; etc

        elif CoordsCase == '':  # Si On passe son tour
            JoueurActif = set_TourJoueur(JoueurActif)  # On change de joueur
            continue

        else:  # Si le joueur ne saute pas son tour
            if ModeDeJeuBase == True:

                CaseDelDispo = False  # Initialisation de la boucle

                while CaseDelDispo != True:  # Tant qu'il n'y a pas de case à retirer disponible

                    Plateau = set_NvCase(Plateau, CoordsCase, JoueurActif, CoordsJoueurs, ModeDeJeuBase)
                    CoordsJoueurs[JoueurActif - 1] = CoordsCase  # Les coordonnées de la case choisie deviennent ceux du joueur

                    mod_Aff.AffichPlateau(Plateau)

                    CoordsCaseDel = mod_Ent.get_ChoixCaseDel(Plateau, JoueurActif)  # Si on a choisi le mode de jeu de base, on choisi maintenant une case à supprimer
                    CaseDelDispo = check_IfCaseDelDispo(Plateau, CoordsCaseDel)  # On vérifie si cette case est disponible pour la suppression

                    if CaseDelDispo == True:  # Si oui, on supprime la case
                        Plateau = set_DelCase(Plateau, CoordsCaseDel)

                    elif CaseDelDispo == False:  # Si non, il faut choisir une case qui peut être supprimée
                        mod_Aff.AffichPlateau(Plateau)  # On affiche le plateau avant d'afficher l'erreur et de redemander le choix
                        print(DATA.MsgError1)
                        continue


            elif ModeDeJeuBase == False:  # Le second mode de jeu a été choisi,
                # Donc c'est la case sur laquelle on se trouvait qui est supprimée
                Plateau = set_NvCase(Plateau, CoordsCase, JoueurActif, CoordsJoueurs, ModeDeJeuBase)  # On change de case et on supprime l'ancienne
                CoordsJoueurs[JoueurActif - 1] = CoordsCase  # Les coordonnées de la case choisie deviennent ceux du joueur




            # On vérifie si il y a un gagnant

            Perdant = check_IfPerdu(Plateau, CoordsJoueurs)  # On regarde si il y a au moins une case libre restante autour des joueur
            # Perdant contient le joueur perdant (prend les valeurs 0, 1 et 2 si il y a 2 joueurs)

            if Perdant != 0:  # Si il n'y en a pas, on désigne un gagnant. (Au moins un perdant)
                mod_Aff.AffichPlateau(Plateau)
                JoueurGagnant = set_Gagnant(Perdant)

                Save_Jeu(MainPath, NomJeu, NomJoueur1, NomJoueur2, Plateau, CoordsJoueurs, JoueurActif, Opt_Tupl, Perdant, JoueurGagnant)  # On sauvegarde la partie gagnée
            elif Perdant == 0:
                JoueurActif = set_TourJoueur(JoueurActif)  # Pas de gagnant, on change de joueur

        # Fin de boucle

#----------------------------------------------------------------------------------------------------------------------#

def check_IfCasePosDispo(Plateau, JoueurActif, CoordsCase):
    """
    Fonction qui vérifie si la case où le joueur souhaite se placer est disponible;
        - Initialisation de la valeur de la disponibilité de la case à False
        - Obtention du joueur suivant

        - Tests:
            - Tests sur les huit cases autour de la case choisi: le joueur actif doit se trouver dans l'une d'entre elles
            - Tests sur la case choisie: si le joueur actif ou suivant se trouve dessus, la case est invalide

    Entrées:
        - Plateau:  Le tableau de jeu (liste de listes)
        - JoueurActif:  Le joueur qui doit jouer
        - CoordsCase:  Les coordonnées (y, x) de la case choisie par l'utilisateur

    Sorties:
        - CasePosDispo:  Variable booléenne contenant True ou False; False: la case choisie n'est pas disponible, True: la case est valide.
    """


    CasePosDispo = False  # On initialise la valeur à False si aucun test ne renvoie True
    JoueurSuivant = set_TourJoueur(JoueurActif)  # On récupère le joueur suivant pour tester si on essaie de placer notre pion dessus


    # On teste si le joueur se trouve dans une des 8 cases autour de la case choisie.
    if Plateau[CoordsCase[0] - 1][CoordsCase[1] - 1] == JoueurActif:
        CasePosDispo = True
    elif Plateau[CoordsCase[0] - 1][CoordsCase[1]] == JoueurActif:
        CasePosDispo = True
    elif Plateau[CoordsCase[0] - 1][CoordsCase[1] + 1] == JoueurActif:
        CasePosDispo = True
    elif Plateau[CoordsCase[0]][CoordsCase[1] - 1] == JoueurActif:
        CasePosDispo = True
    elif Plateau[CoordsCase[0] + 1][CoordsCase[1] - 1] == JoueurActif:
        CasePosDispo = True
    elif Plateau[CoordsCase[0] + 1][CoordsCase[1] + 1] == JoueurActif:
        CasePosDispo = True
    elif Plateau[CoordsCase[0] + 1][CoordsCase[1]] == JoueurActif:
        CasePosDispo = True
    elif Plateau[CoordsCase[0]][CoordsCase[1] + 1] == JoueurActif:
        CasePosDispo = True


    if Plateau[CoordsCase[0]][CoordsCase[1]] == JoueurActif:
        CasePosDispo = False  # Si la case sur laquelle on se trouve déja est choisie

    elif Plateau[CoordsCase[0]][CoordsCase[1]] == JoueurSuivant:
        CasePosDispo = False  # Le joueur actif ne peut se placer sur le pion de son adversaire

    if Plateau[CoordsCase[0]][CoordsCase[1]] == 3:
        CasePosDispo = False  # Le joueur actif ne peut se placer sur une case vide

    return CasePosDispo  # Renvoie si le joueur a le droit de se placer sur cette case (True) ou non (False)

#----------------------------------------------------------------------------------------------------------------------#

def check_IfCaseDelDispo(Plateau, CoordsCase):
    """
    Fonction simplifiée qui vérifie si la case que le joueur veux enlever est disponible;
        - Initialisation de la valeur de la disponibilité de la case à False

        - Test:
            - On vérifie si la case choisie est vide

    Entrées:
        - Plateau:  Le tableau de jeu (liste de listes)
        - CoordsCase:  Les coordonnées (y, x) de la case choisie par l'utilisateur

    Sorties:
        - CaseDelDispo:  Variable booléenne contenant True ou False; False: la case choisie n'est pas disponible, True: la case est valide.
    """


    CaseDelDispo = False  # On initialise la valeur à False (Si un joueur est présent sur la case ou si elle est déjà vide)

    if Plateau[CoordsCase[0]][CoordsCase[1]] == 0:
        CaseDelDispo = True  # La case est vide, donc peut être retirée

    return CaseDelDispo  # Renvoie si le joueur a le droit de retirer cette case (True) ou non (False)

#----------------------------------------------------------------------------------------------------------------------#

def set_TourJoueur(JoueurActif):
    """
    Fonction qui permet de passer au joueur suivant;
        - Si le joueur actif est 1, alors on passe au joueur 2
        - Si le joueur actif est 2, alors on passe au joueur 1

    Entrées:
        - JoueurActif:  Le joueur qui jouait (et qui a fini son tour)

    Sorties:
        - JoueurActif:  Le joueur qui doit jouer à présent
    """


    if JoueurActif == 1:  # Si le joueur actif est le n°1, on passe au n°2
        JoueurActif = 2
        return JoueurActif

    elif JoueurActif == 2:  # et inversement
        JoueurActif = 1
        return JoueurActif

#----------------------------------------------------------------------------------------------------------------------#

def set_DelCase(Plateau, CoordsCase):
    """
    Fonction qui enlève une case;
        - La valeur de la case du plateau de coordonnées CoordsCase est réaffectée à 3

    Entrées:
        - Plateau:  Tableau (liste de listes)
        - CoordsCase:  Tuple contenant les coordonnées (y, x) de la case choisie

    Sorties:
        - Plateau:  le plateau de jeu avec la case retirée.
    """


    Plateau[CoordsCase[0]][CoordsCase[1]] = 3  # On remplace la case choisie par une case vide

    return Plateau  # on renvoie le nouveau tableau

#----------------------------------------------------------------------------------------------------------------------#

def set_NvCase(Plateau, CoordsCase, JoueurActif, CoordsJoueurs, ModeDeJeuBase):
    """
    Fonction qui change le joueur de case en accord avec le mode de jeu (les règles du jeu) choisies;
        - Dans le mode de jeu de base:
            le joueur avance sur une des huit cases autour de lui, la dernière case sur laquelle il se trouvait est remplacée par une case libre.
        - Dans le second mode de jeu:
            Le joueur avance sur une des huit cases autour de lui, la dernière case sur laquelle il se trouvait est enlevée.

        - Le joueur est donc d'abord remplacé par 0 ou 3 selon le mode de jeu
        - Puis placé aux coordonnées qu'il a choisies

    Entrées:
        - Plateau:  Tableau (liste de listes)
        - CoordsCase:  Tuple de coordonées (y, x) (lignes, colonnes)
        - JoueurActif:  Le joueur qui joue ce tour
        - CoordsJoueurs:  Liste de tuples contenant les coordonnées (y, x) des joueurs
        - ModeDeJeuBase:  Option facultative booléenne qui prend pour valeur True ou False

    Sorties:
        - Plateau Tableau (liste de listes), avec la position du joueur actif modifiée
    """


    if ModeDeJeuBase == True:
        ValAncCase = 0  # La case sur laquelle se trouvait le joueur est remplacée par une case libre dans le jeu de base
    elif ModeDeJeuBase == False:
        ValAncCase = 3  # Et par une case vide dans le second mode de jeu  (case vide = 3)

    # ValAncCase prend la valeur 0 dans les règles du jeu de base; mais 3 dans les secondes règles du jeu; où la case supprimée est la dernière case occupée par le joueur.

    CoordsJoueurActif = CoordsJoueurs[JoueurActif - 1]  # On récupère les coordonnées du joueur

    Plateau[CoordsJoueurActif[0]][CoordsJoueurActif[1]] = ValAncCase  # On remplace le joueur par ValAncCase
    Plateau[CoordsCase[0]][CoordsCase[1]] = JoueurActif  # Le joueur est placé à la case qu'il a choisi

    return Plateau  # on renvoie le nouveau tableau

#----------------------------------------------------------------------------------------------------------------------#

def check_IfPerdu(Plateau, CoordsJoueurs):
    """
    Fonction qui vérifie si il y a un perdant;
        - Initialisation de 'Perdant' à 0: pas de perdant

        - On vérifie si les huits cases autour de tous les joueurs sont disponibles
            - Si au moins une case est disponible, alors il n'y a pas de perdant.
            - Sinon, Perdu prend la valeur du joueur (1 ou 2) perdant

    Entrées:
        - Plateau:  Tableau (liste de listes)
        - CoordsJoueurs:  Liste de tuples contenant les coordonnées (y, x) des joueurs

    Sorties:
        - Perdu:  0 si aucun joueur n'a perdu, 1 ou 2 si le joueur 1 ou 2 a perdu.
    """


    Perdu = 0  # On initialise la valeur à False si aucun test ne renvoie True
    Compteur = 0

    for CoordsJoueur in CoordsJoueurs:
        # On vérifie pour les joueurs tour à tour
        Compteur += 1

        # On teste si les 8 cases autour sont disponibles; si l'une d'entre elles l'est, on ne vérifie pas les autres, car on sait que le joueur peut encore jouer.
        if Plateau[CoordsJoueur[0] - 1][CoordsJoueur[1] - 1] != 0 and \
                Plateau[CoordsJoueur[0] - 1][CoordsJoueur[1]] != 0 and \
                Plateau[CoordsJoueur[0] - 1][CoordsJoueur[1] + 1] != 0 and \
                Plateau[CoordsJoueur[0]][CoordsJoueur[1] - 1] != 0 and \
                Plateau[CoordsJoueur[0] + 1][CoordsJoueur[1] - 1] != 0 and \
                Plateau[CoordsJoueur[0] + 1][CoordsJoueur[1] + 1] != 0 and \
                Plateau[CoordsJoueur[0] + 1][CoordsJoueur[1]] != 0 and \
                Plateau[CoordsJoueur[0]][CoordsJoueur[1] + 1] != 0:
            Perdu = Compteur  # Si aucune des 8 cases autours du joueur testé est libre, alors il a perdu (il ne peut y avoir qu'un perdant à la fois; pas de match nul)


    return Perdu  # Renvoie 0 si au personne n'a perdu; 1 si le joueur 1 a perdu, et 2 si le joueur 2 a perdu

#----------------------------------------------------------------------------------------------------------------------#

def set_Gagnant(JoueurPerdant):
    """
    Fonction qui vérifie si il y a un perdant;
        - Initialisation du gagnant: c'est le joueur qui suit le joueur perdant

    Entrées:
        - JoueurPerdant:  Le joueur qui n'a pas gagné !
    Sorties:
        - JoueurGagnant:  Le joueur dont le tour suit celui du joueur perdant
    """


    JoueurGagnant = set_TourJoueur(JoueurPerdant)

    print("Joueur {}, Vous avez perdu !".format(JoueurPerdant))
    print("Bravo, Joueur {}, Vous avez Gagné !".format(JoueurGagnant))

    return JoueurGagnant

#----------------------------------------------------------------------------------------------------------------------#

def Save_Jeu(MainPath, NomJeu, NomJoueur1, NomJoueur2, Plateau, CoordsJoueurs, JoueurActif, Opt_Tupl, Perdant, Gagnant):
    """
    Fonction qui écrit les résultats d'une partie (terminée oou non) dans un fichier .csv modifiable user-friendly;
        - Valeurs sauvegardées communes aux deux modes d'écriture:
            - Noms des joueurs
            - Plateau de jeu
            - Coordonnées des joueurs
            - Les options facultatives choisies


        - Si il y a un gagnant, donc si la partie est terminée:
            Partie sauvegardée dans le fichier des sauvegardes gagnées
            - Les dimensions du plateau ne sont pas sauvegardées
            - Le gagnant est sauvegardé à la place du joueur actif

        - Si il n'y a pas de gagnant, donc si la partie est en cours:
            Partie sauvegardée dans le fichier des sauvegardes en cours
            - Les dimensions du plateau sont sauvegardées
            - Le joueur actif est sauvegardé

    Entrées:
        - MainPath:  Le chemin absolu menant au programme principal ( " Programme_Principal_Main_Program " )
        - NomJeu:  Le nom de la partie; la sauvegarde portera ce nom
        - NomJoueur1:  Le nom du joueur qui a joué en premier
        - NomJoueur2:  Le nom du second joueur
        - Plateau:  Tableau (liste de listes)
        - CoordsJoueurs:  Liste de tuples contenant les coordonnées des joueurs
        - JoueurActif:  Le joueur qui était entrain de jouer (et qui a décidé de quitter, avec forcément l'accord du second joueur)
        - Opt_Tupl:  Tuple contenant les options facultatives choisies
        - Perdant:  Le joueur perdant (1 ou 2)
        - Gagnant:  Le joueur gagnant (1 ou 2)

    Sorties:
        - Pas de sorties
    """


    os.chdir(MainPath)  # On reset le Current Working Directory
    if Perdant == 0:  # Si il n'y a pas de perdant (donc la partie n'est pas finie)
        path = os.getcwd() + DATA.FileSavePath
    else:
        path = os.getcwd() + DATA.FileWonSavePath
    os.chdir(path)  # On travaille sur les sauvegardes non finies

    NbLignPlateau, NbColPlateau = len(Plateau) - 1, len(Plateau[0]) - 1

    with open(NomJeu + DATA.FileExtension, 'w') as SaveFile:  # 'with' permet de fermer le fichier automatiquement, même si le programme ne fonctionne pas.

        if Perdant == 0:
            # Sauvegarde du nombre de colonnes et de lignes du plateau (utilisés pour charger la partie)
            SaveFile.write("Nombre de lignes et de colonnes du plateau: (ne pas les modifier)" + '\n')
            SaveFile.write(str(NbLignPlateau) + DATA.FileWritingSeparator + str(NbColPlateau) + '\n')
        else:
            pass  # On ne sauvegarde pas les dimensions du plateau dans une partie terminée; car elle ne sera jamais chargée.


        # Sauvegarde des noms des joueurs
        SaveFile.write("Partie jouée par:" + '\n' + "Joueur 1:\n" + NomJoueur1 + '\n' + "Joueur 2:\n" + NomJoueur2 + '\n')


        # Sauvegarde du joueur actif/ du gagnant (si la partie est terminée)
        if Perdant == 0:  # Partie en cours, on sauvegarde le joueur actif.
            # Sauvegarde du joueur actif
            SaveFile.write("Joueur Actif:" + '\n')
            SaveFile.write(str(JoueurActif))
        else:  # Partie terminée, on sauvegarde le gagnant
            SaveFile.write("Joueur Gagnant:" + '\n')
            SaveFile.write(str(Gagnant))

        SaveFile.write('\n')


        # Sauvegarde du plateau de jeu
        for k in range(1, NbColPlateau):  # En-tête du plateau
            SaveFile.write(DATA.FileWritingSeparator + (chr(k + DATA.ValASCII)))

        SaveFile.write('\n')

        for i in range(1, NbLignPlateau):

            SaveFile.write(str(i) + DATA.FileWritingSeparator)  # Numérotation des lignes

            for j in range(1, NbColPlateau - 1):

                SaveFile.write(str(Plateau[i][j]) + DATA.FileWritingSeparator)  # Eléments du plateau

            SaveFile.write(str(Plateau[i][NbColPlateau - 1]))  # Eléments du plateau
            SaveFile.write('\n')


        # Sauvegarde des coordonnées des joueurs
        for i in range(len(CoordsJoueurs)):
            SaveFile.write("Joueur {}:".format(i + 1) + '\n')
            for j in CoordsJoueurs[i]:
                SaveFile.write(str(j) + DATA.FileWritingSeparator)

            SaveFile.write('\n')


        # Sauvegarde des options choisies
        SaveFile.write("Options choisies:" + '\n')
        for i in Opt_Tupl:
            SaveFile.write(str(i) + DATA.FileWritingSeparator)

#----------------------------------------------------------------------------------------------------------------------#

def Charge_Jeu(MainPath, NomJeu):
    """
    Fonction qui récupère les valeurs contenues dans une sauvegarde non terminée sous la forme d'un fichier .csv modifiable user-friendly;
        - Les parties gagnées ne peuvent donc pas être chargées (elles ne sont pas jouables et ne servent qu'a se vanter d'avoir gagné)

        - Valeurs lues:
            - Les dimensions du plateau
            - Noms des joueurs
            - Le joueur actif
            - Plateau de jeu  (reconstruit à vide à partir des dimensions sauvegardées puis rempli à partir du .csv)
            - Coordonnées des joueurs
            - Les options facultatives choisies

    Entrées:
        - Pas d'entrées

    Sorties:
        - NomJoueur1:  Le nom du joueur qui a joué en premier
        - NomJoueur2:  Le nom du second joueur
        - Plateau:  Tableau (liste de listes)
        - CoordsJoueurs:  Liste de tuples contenant les coordonnées des joueurs
        - JoueurActif:  Le joueur qui était entrain de jouer (et qui a décidé de quitter, avec forcément l'accord du second joueur)
        - Opt_Tupl:  Tuple contenant les options facultatives choisies
    """


    os.chdir(MainPath)  # On reset le Current Working Directory
    path = os.getcwd() + DATA.FileSavePath
    os.chdir(path)  # On travaille sur les sauvegardes non finies

    with open(NomJeu + DATA.FileExtension, 'r') as SaveFile:  # 'with' permet de fermer le fichier automatiquement, même si le programme ne fonctionne pas.

        # On récupère le nombre de lignes et de colonnes du plateau
        SaveFile.readline()
        DimPlateau = SaveFile.readline().split(';')
        NbLignPlateau, NbColPlateau = int(DimPlateau[0]) - 1, int(DimPlateau[1]) - 1


        # On récupère les noms des joueurs
        SaveFile.readline()
        SaveFile.readline()
        NomJoueur1 = SaveFile.readline().strip()  # .strip seul enlève le saut de ligne en fin de chaine
        SaveFile.readline()
        NomJoueur2 = SaveFile.readline().strip()


        # On récupère le joueur actif
        SaveFile.readline()
        JoueurActif = int(SaveFile.readline())


        # On récupère le plateau de jeu

        # On initialise le cadre du plateau et le plateau vide avec les dimensions récupérées
        Plateau = init_DimPlat(NbLignPlateau, NbColPlateau)
        SaveFile.readline()  # On passe l'en-tête du plateau

        for i in range(1, NbLignPlateau + 1):

            LignePlateau = SaveFile.readline().strip()  # On récupère la ligne du plateau (sans le saut de ligne)

            ColonnePlateau = LignePlateau.split(DATA.FileWritingSeparator)  # On découpe la ligne en colonnes

            for j in range(1, NbColPlateau + 1):  # On passe la première colonne, on commence à 1
                Plateau[i][j] = int(ColonnePlateau[j])  # On remplace le tableau vide par le tableau enregistré

        # On récupère les coordonnées des joueurs

        CoordsJoueurs = []

        for i in range(2):

            SaveFile.readline()

            CoordsJoueur = SaveFile.readline().strip().rstrip(';').split(';')  # On lit les coordonnées des joueurs tour à tour

            CoordsJoueur[0] = int(CoordsJoueur[0])  # On les transforment en entier
            CoordsJoueur[1] = int(CoordsJoueur[1])
            CoordsJoueurs += [tuple(CoordsJoueur)]  # Et on les ajoutent à un tuple de la forme (y, x) et dans la liste des coordonnées.


        # On récupère les options choisies
        SaveFile.readline()
        Opt_Tupl = list(SaveFile.readline().rstrip(';').split(';'))  # On en fait une liste pour modifier les valeurs à l'intérieur

        for k in range(len(Opt_Tupl)):
            if Opt_Tupl[k] == 'True':
                Opt_Tupl[k] = True  # On retransforme les éléments de Opt_Tupl en booléens

            elif Opt_Tupl[k] == 'False':
                Opt_Tupl[k] = False

        Opt_Tupl = tuple(Opt_Tupl)  # Puis on fait de Opt_Tupl un tuple.

    return NomJoueur1, NomJoueur2, Plateau, CoordsJoueurs, JoueurActif, Opt_Tupl
