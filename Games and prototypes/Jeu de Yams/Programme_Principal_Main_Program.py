
#----------------------------------------------------------------------------------------------------------------------#
# Projet final de NSI à rendre pour fin Mai 2020
# Jeu de Yams avec plateau dynamique, sauvegarde des scores et des parties en format .csv, chargement des parties non terminées, et options de jeu facultatives !
#----------------------------------------------------------------------------------------------------------------------#


# Imports

import module_FonctionsMétier as mod_Met
import module_DATA as DATA

import os


def __main__():

    DicoJoué = {1: ('Yams', False), 2: ('Chance', False), 3: ('Grande suite', False), 4: ('Petite suite', False),
                5: ('Full', False), 6: ('Carré', False),
                7: ('Brelan', False), 8: ('Total de 6', False), 9: ('Total de 5', False), 10: ('Total de 4', False),
                11: ('Total de 3', False),
                12: ('Total de 2', False), 13: ('Total de 1', False)}  # Représente ce qui a déja été marqué sur la feuille de score

    DicoR = {1: True, 2: True, 3: True, 4: True, 5: True}  # Représente quels dés le joueur souhaite relancer

    DicoDésLancés = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}  # Représente les valeurs de chaque dés (chaque dés contient 0à l'initialisation)

    NbJoueurs = mod_Met.get_NombreJoueurs()
    JoueurActif = 1

    ListFeuillesChoixJoueurs = []
    for n in range(NbJoueurs):
        ListFeuillesChoixJoueurs += [dict(DicoJoué)]

    FeuilleScore = mod_Met.init_FeuilleScore(NbJoueurs)

    FeuilleRemplie = False

    while FeuilleRemplie == False:

        DicoDésLancés = mod_Met.Lancer_Dés(DicoDésLancés, DicoR)  # Premier lancé
        mod_Met.Affich_Dés(DicoDésLancés)
        print("Joueur {}, à vous de jouer !".format(JoueurActif))

        for ToursJoués in range(2):  # Les deux autres tours
            ChoixRelance = mod_Met.get_ChoixRelance(DicoDésLancés)
            DicoR = mod_Met.set_DicoR(ChoixRelance)

            DicoDésLancés = mod_Met.Lancer_Dés(DicoDésLancés, DicoR)
            mod_Met.Affich_Dés(DicoDésLancés)

        ChoixCorrect = False

        while ChoixCorrect == False:

            ChoixScore = mod_Met.get_ChoixFeuilleScore(ListFeuillesChoixJoueurs[JoueurActif - 1], DicoDésLancés)

            # Choix de passer son tour
            if ChoixScore == 14:
                print("Vous n'écrivez rien, et passez votre tour.")
                ChoixCorrect = True

            # Choix de marquer un Yams
            elif ChoixScore == 1:
                if not mod_Met.is_Yams(DicoDésLancés):
                    mod_Met.Affich_ErreurDés(DicoDésLancés, ListFeuillesChoixJoueurs[JoueurActif - 1], ChoixScore)
                else:
                    ListFeuillesChoixJoueurs[JoueurActif - 1][1] = ('Yams', True)
                    FeuilleScore[14][JoueurActif - 1] = DATA.Score_Yams
                    ChoixCorrect = True


            # Choix de marquer une Chance
            elif ChoixScore == 2:
                ListFeuillesChoixJoueurs[JoueurActif - 1][2] = ('Chance', True)
                FeuilleScore[15][JoueurActif - 1] = mod_Met.get_ScoreChance(DicoDésLancés)
                ChoixCorrect = True


            # Choix de marquer une Grande Suite
            elif ChoixScore == 3:
                if not mod_Met.is_GrdSuite(DicoDésLancés):
                    mod_Met.Affich_ErreurDés(DicoDésLancés, ListFeuillesChoixJoueurs[JoueurActif - 1], ChoixScore)
                else:
                    ListFeuillesChoixJoueurs[JoueurActif - 1][3] = ('Grande Suite', True)
                    FeuilleScore[13][JoueurActif - 1] = DATA.Score_GrdSuite
                    ChoixCorrect = True


            # Choix de marquer une Petite Suite
            elif ChoixScore == 4:
                if not mod_Met.is_PetSuite(DicoDésLancés):
                    mod_Met.Affich_ErreurDés(DicoDésLancés, ListFeuillesChoixJoueurs[JoueurActif - 1], ChoixScore)
                else:
                    ListFeuillesChoixJoueurs[JoueurActif - 1][4] = ('Petite Suite', True)
                    FeuilleScore[12][JoueurActif - 1] = DATA.Score_PetSuite
                    ChoixCorrect = True


            # Choix de marquer un Full
            elif ChoixScore == 5:
                if not mod_Met.is_Full(DicoDésLancés):
                    mod_Met.Affich_ErreurDés(DicoDésLancés, ListFeuillesChoixJoueurs[JoueurActif - 1], ChoixScore)
                else:
                    ListFeuillesChoixJoueurs[JoueurActif - 1][5] = ('Full', True)
                    FeuilleScore[11][JoueurActif - 1] = DATA.Score_Full
                    ChoixCorrect = True


            # Choix de marquer un Carré
            elif ChoixScore == 6:
                Is_Carre, Type_Carre = mod_Met.is_Carré(DicoDésLancés)
                if not Is_Carre:
                    mod_Met.Affich_ErreurDés(DicoDésLancés, ListFeuillesChoixJoueurs[JoueurActif - 1], ChoixScore)
                else:
                    ListFeuillesChoixJoueurs[JoueurActif - 1][6] = ('Carré', True)
                    FeuilleScore[10][JoueurActif - 1] = mod_Met.get_ScoreCarre(DicoDésLancés, Type_Carre)
                    ChoixCorrect = True


            # Choix de marquer un Brelan
            elif ChoixScore == 7:
                Is_Brelan, Type_Brelan = mod_Met.is_Brelan(DicoDésLancés)
                if not Is_Brelan:
                    mod_Met.Affich_ErreurDés(DicoDésLancés, ListFeuillesChoixJoueurs[JoueurActif - 1], ChoixScore)
                else:
                    ListFeuillesChoixJoueurs[JoueurActif - 1][7] = ('Brelan', True)
                    FeuilleScore[9][JoueurActif - 1] = mod_Met.get_ScoreBrelan(DicoDésLancés, Type_Brelan)
                    ChoixCorrect = True


            # Choix de marquer la somme des 6
            elif ChoixScore == 8:
                if not mod_Met.is_X(DicoDésLancés, 6):
                    mod_Met.Affich_ErreurDés(DicoDésLancés, ListFeuillesChoixJoueurs[JoueurActif - 1], ChoixScore)
                else:
                    ListFeuillesChoixJoueurs[JoueurActif - 1][8] = ('Total de 6', True)
                    FeuilleScore[5][JoueurActif - 1] = mod_Met.get_ScoreX(DicoDésLancés, 6)
                    ChoixCorrect = True


            # Choix de marquer la somme des 5
            elif ChoixScore == 9:
                if not mod_Met.is_X(DicoDésLancés, 5):
                    mod_Met.Affich_ErreurDés(DicoDésLancés, ListFeuillesChoixJoueurs[JoueurActif - 1], ChoixScore)
                else:
                    ListFeuillesChoixJoueurs[JoueurActif - 1][9] = ('Total de 5', True)
                    FeuilleScore[4][JoueurActif - 1] = mod_Met.get_ScoreX(DicoDésLancés, 5)
                    ChoixCorrect = True


            # Choix de marquer la somme des 4
            elif ChoixScore == 10:
                if not mod_Met.is_X(DicoDésLancés, 4):
                    mod_Met.Affich_ErreurDés(DicoDésLancés, ListFeuillesChoixJoueurs[JoueurActif - 1], ChoixScore)
                else:
                    ListFeuillesChoixJoueurs[JoueurActif - 1][10] = ('Total de 4', True)
                    FeuilleScore[3][JoueurActif - 1] = mod_Met.get_ScoreX(DicoDésLancés, 4)
                    ChoixCorrect = True


            # Choix de marquer la somme des 3
            elif ChoixScore == 11:
                if not mod_Met.is_X(DicoDésLancés, 3):
                    mod_Met.Affich_ErreurDés(DicoDésLancés, ListFeuillesChoixJoueurs[JoueurActif - 1], ChoixScore)
                else:
                    ListFeuillesChoixJoueurs[JoueurActif - 1][11] = ('Total de 3', True)
                    FeuilleScore[2][JoueurActif - 1] = mod_Met.get_ScoreX(DicoDésLancés, 3)
                    ChoixCorrect = True


            # Choix de marquer la somme des 2
            elif ChoixScore == 12:
                if not mod_Met.is_X(DicoDésLancés, 2):
                    mod_Met.Affich_ErreurDés(DicoDésLancés, ListFeuillesChoixJoueurs[JoueurActif - 1], ChoixScore)
                else:
                    ListFeuillesChoixJoueurs[JoueurActif - 1][12] = ('Total de 2', True)
                    FeuilleScore[1][JoueurActif - 1] = mod_Met.get_ScoreX(DicoDésLancés, 2)
                    ChoixCorrect = True


            # Choix de marquer la somme des 1
            elif ChoixScore == 13:
                if not mod_Met.is_X(DicoDésLancés, 1):
                    mod_Met.Affich_ErreurDés(DicoDésLancés, ListFeuillesChoixJoueurs[JoueurActif - 1], ChoixScore)
                else:
                    ListFeuillesChoixJoueurs[JoueurActif - 1][13] = ('Total de 1', True)
                    FeuilleScore[0][JoueurActif - 1] = mod_Met.get_ScoreX(DicoDésLancés, 1)
                    ChoixCorrect = True

        # Ajout du total
        FeuilleScore[6][JoueurActif - 1] = mod_Met.get_SousTotal(FeuilleScore, JoueurActif)
        # Ajout de la prime
        if FeuilleScore[6][JoueurActif - 1] > 63:
            FeuilleScore[7][JoueurActif - 1] = DATA.Score_Prime
        # Ajout du total1
        FeuilleScore[8][JoueurActif - 1] = FeuilleScore[6][JoueurActif - 1] + FeuilleScore[7][JoueurActif - 1]

        # Ajout du total2
        FeuilleScore[16][JoueurActif - 1] = mod_Met.get_SousTotal2(FeuilleScore, JoueurActif)
        # Ajout du grand total
        FeuilleScore[17][JoueurActif - 1] = FeuilleScore[8][JoueurActif - 1] + FeuilleScore[16][JoueurActif - 1]
        # affiche les scores des joueurs et leur total de point
        mod_Met.aff_FeuilleScore(FeuilleScore)

        Gagnant = mod_Met.check_IfGagnant(ListFeuillesChoixJoueurs,
                                          JoueurActif)  # vérifie si une des feuilles de score est pleine et à qui elle appartient    renvoie Gagnant qui peut prendre les valeurs 0 (pas de gagnant) ou 1, 2, 3... (joueurs)
        #
        if Gagnant != 0:
            print("La partie est terminée, le joueur {} a rempli sa fiche.".format(Gagnant))
            FileName = 'testFeuille.csv'
            mod_Met.Save_FeuilleDeScores(FileName, FeuilleScore)
            FeuilleRemplie = True

        else:
            JoueurActif = mod_Met.set_NvJoueur(JoueurActif, NbJoueurs)
            DicoR = {1: True, 2: True, 3: True, 4: True, 5: True}
            FeuilleRemplie = False





__main__()

os.system('pause')

