# Imports
import traceback
import module_DATA as DATA
import os
import random

from random import randint


#----------------------------------------------------------------------------------------------------------------------#

def aff_FeuilleScore(FeuilleDeScores):
    """
        Entrée: FeuilleDeScores: La feuille de score avec les points des joueurs
    """

    NbLignes, NbColonnes = len(FeuilleDeScores), len(FeuilleDeScores[0])
    NbJoueurs = NbColonnes

    print("{}: |".format(DATA.tup_TitreLignes[0]), end = '')

    for k in range(1, NbJoueurs + 1):
        print("  {}  |".format(chr(k + DATA.ValASCII)), end = '')

    print('\n------------------------------------')

    for n in range(NbLignes):

        print("{}: |".format(DATA.tup_TitreLignes[n + 1]), end = '')

        for m in range(NbColonnes):
            if FeuilleDeScores[n][m] == 0:
                Score = "     |"
            else:
                Score = str(FeuilleDeScores[n][m]).center(5) + '|'

            print(Score, end = '')

        print()
#        print('               ---------------------')
    print()

#----------------------------------------------------------------------------------------------------------------------#

def init_FeuilleScore(NbJoueurs):
    """
        Entrée: NbJoueurs: Le nombre de joueurs
        Sortie: FeuilleDeScores: La feuille de score initialisée à vide
    """

    # Initialisation de la feuille de scores
    nbLigne = DATA.NombreDeLignes
    FeuilleDeScores = []

    for n in range(nbLigne):
        FeuilleDeScores.append([])  # Ajout des lignes de scores : nombre de lignes sans la ligne des joueurs
        for m in range(NbJoueurs):
            FeuilleDeScores[n].append(0)  # Ajout des cases non remplies, initialisées avec la valeur 0.

    return FeuilleDeScores

#----------------------------------------------------------------------------------------------------------------------#

def Save_FeuilleDeScores(FileName, FeuilleDeScores):
    """
        Entrée: ListDésLancés:  Contient les valeurs de chaque dés
        Sortie: Vrai ou Faux si il y a ou non un carré
    """

    NbLigne, NbCol = len(FeuilleDeScores), len(FeuilleDeScores[0])

    with open(FileName, 'w') as SaveFile:  # 'with' permet de fermer le fichier automatiquement, même si le programme ne fonctionne pas.

        # sauvegarde du nombre de Joueurs
        SaveFile.write(str(NbCol) + '\n')

        # Sauvegarde de la première ligne : noms des joueurs
        # D'abord, le titre de la ligne
        s_Ligne = DATA.tup_TitreLignes[0]
        # Ensuite, les noms des joueurs
        for k in range(NbCol):
            s_Ligne += DATA.SepCSV + 'Joueur' + str(k+1)
        SaveFile.write(s_Ligne)
        SaveFile.write('\n')

        # Sauvegarde des autres lignes de la feuille de score
        for i in range(NbLigne):
            s_Ligne = DATA.tup_TitreLignes[i+1]
            for j in range(NbCol):
                s_Ligne += DATA.SepCSV + str(FeuilleDeScores[i][j])

            SaveFile.write(s_Ligne)
            SaveFile.write('\n')

    return

#----------------------------------------------------------------------------------------------------------------------#

def set_NvJoueur(JoueurActif, NbJoueurs):
    """
        Entrée: JoueurActif: Le joueur qui joue ce tour (premier joueur: 1); NbJoueurs: nombre de joueurs (min 1 max 3)
        Sortie: Le joueur suivant
    """

    JoueurActif += 1

    if JoueurActif == NbJoueurs + 1:
        JoueurActif = 1

    return JoueurActif

#----------------------------------------------------------------------------------------------------------------------#

def Lancer_Dés(DicoDésLancés, DicoR):
    """
        Entrée: DicoDésLancés:  Contient les valeurs de chaque dés; DicoR:  Dictionnaire des dés que le joueur souhaite relancer  (True si souhaite relancer ce dé)
        Sortie: DicoDésLancés
    """

    for elt in DicoR.items():
        if elt[1]:  # Sous entendu if elt[1] == True:
            DicoDésLancés[elt[0]] = Random_Des()  # On relance le dé à relancer
    return DicoDésLancés

#----------------------------------------------------------------------------------------------------------------------#

def get_ChoixFeuilleScore(DicoJoué, DicoDésLancés):
    """
        Entrée: DicoDésLancés:  Contient les valeurs de chaque dés; DicoJoué: dictionnaire de tuples permettant d'analyser si le joueur actif a déja rempli ou non une case de sa fiche
        Sortie: La case à remplir
    """

    ChoixDispo = False

    while ChoixDispo == False:
        try:
            for clé, val in DicoJoué.items():
                if val[1] == True:
                    ValPrint = '----------'
                else:
                    ValPrint = 'Disponible'
                print("{}.".format(clé).ljust(4) + "{}: ".format(val[0]).ljust(20) + "{}".format(ValPrint))
            print("14. Ne rien écrire")


            ChoixScore = int(input("""Entrez le numéro de votre choix:
            >>> """))

            if ChoixScore == 14:
                break

            elif ChoixScore <= 0 or ChoixScore > len(DicoJoué):
                raise Exception
            elif DicoJoué[ChoixScore][1] == True:
                Affich_Dés(DicoDésLancés)
                print("{} déja marqué sur votre feuille de score".format(DicoJoué[ChoixScore][0]))
                print()
                ChoixDispo = False
            else:
                ChoixDispo = True

        except ValueError:
            print()
            Affich_Dés(DicoDésLancés)
            print("Entrez un nombre entier")
            print()
            ChoixDispo = False
        except Exception:
            print()
            Affich_Dés(DicoDésLancés)
            print("Entrez un nombre entre 1 et {}".format(len(DicoJoué) + 1))
            print()
            ChoixDispo = False

    return ChoixScore

#----------------------------------------------------------------------------------------------------------------------#

def get_NombreJoueurs():
    """
        Sortie: Le nombre de joueurs
    """

    ChoixCorrect = False

    while ChoixCorrect == False:
        try:
            NbJoueurs = int(input("Combien de joueurs (maximum de 3 joueurs, minimum de 1): "))

            if NbJoueurs <= 0 or NbJoueurs >= 4:
                raise Exception
            else:
                ChoixCorrect = True

        except ValueError:
            print("Entrez un nombre entier")
            ChoixCorrect = False
        except Exception:
            print("Entrez un nombre entre 1 et 3")
            ChoixCorrect = False

    return NbJoueurs

#----------------------------------------------------------------------------------------------------------------------#

def get_ChoixRelance(DicoDésLancés):
    """
        Entrée: DicoDésLancés:  Contient les valeurs de chaque dés
        Sortie: Renvoie quels dés l'utilisateur veux relancer
    """

    ChoixCorrect = False

    while ChoixCorrect == False:
        try:

            ChoixRelance = input("""
            Quels dés voulez-vous relancer ?  entrez les numéros des dés à relancer; laisser vide pour ne pas relancer
            exemple: 12345 ou 1 2 3 4 5 / 53 ou 5 3 / 146 ou 1 4 6
            >>> """)

            if ChoixRelance == '':
                ChoixCorrect = True

            else:

                for elt in ChoixRelance:
                    if elt == ' ':
                        pass
                    elif int(elt) <= 0 or int(elt) >= 6:
                        raise Exception

                ChoixCorrect = True

        except:
            Affich_Dés(DicoDésLancés)
            print("Erreur")
            ChoixCorrect = False

    return ChoixRelance

#----------------------------------------------------------------------------------------------------------------------#

def set_DicoR(ChoixRelance):
    """
    Entrée: ChoixRelance: les dés que l'utilisateur veut relancer (
    Sortie: Vrai ou Faux si il y a ou non un carré
    """

    DicoR = {1: False,
             2: False,
             3: False,
             4: False,
             5: False}


    if ChoixRelance == '':
        pass

    else:
        for k in range(len(ChoixRelance)):
            if ChoixRelance[k] != ' ':
                DicoR[int(ChoixRelance[k])] = True

    return DicoR

#----------------------------------------------------------------------------------------------------------------------#

def Random_Des():
    """
    Sortie: une valeur aléatoire
    """
    val = random.randint(1, 6)
    return val

#----------------------------------------------------------------------------------------------------------------------#

def is_UniqueVal(ListDésLancés):
    """
    Entrée: ListDésLancés:  Contient les valeurs de chaque dés
    Sortie: Vrai ou Faux si toutes les valeurs de ListDésLancés sont les mêmes ou non.
    """
    Valeur = ListDésLancés[0]
    for i in range(1, len(ListDésLancés)):
        if Valeur != ListDésLancés[i]:
            return False
    return True

#----------------------------------------------------------------------------------------------------------------------#

def is_Carré(DicoDésLancés):
    """
    Entrée: DicoDésLancés:  Contient les valeurs de chaque dés
    Sortie: Vrai ou Faux si il y a ou non un carré
    """
    # Il n'y a que 2 combinaisons possibles
    # Solution 1 : 1 1 1 1 2
    # Solution 2 : 2 3 3 3 3
    # On va commencer par trier les valeurs
    ValeursTriées = sorted(DicoDésLancés.values())

    # On extrait les 4 premières valeurs
    ListDésLancés = []
    for i in range(4):
        ListDésLancés.append(ValeursTriées[i])

    # On vérifie si les valeurs sont identiques
    if is_UniqueVal(ListDésLancés):
        return True, DATA.Carre_debut

    # On extrait les 4 dernières valeurs
    ListDésLancés = []
    for i in range(1, 5):
        ListDésLancés.append(ValeursTriées[i])

    # On vérifie si les valeurs sont identiques
    if is_UniqueVal(ListDésLancés):
        return True, DATA.Carre_fin

    return False, DATA.Carre_absent

#----------------------------------------------------------------------------------------------------------------------#

def is_Yams(DicoDésLancés):
    """
    Entrée: DicoDésLancés:  Contient les valeurs de chaque dés
    Sortie: Vrai ou Faux si il y a ou non un Yams
    """
    ListDésLancés = []
    for clé, val in DicoDésLancés.items():
        ListDésLancés.append(val)

    return is_UniqueVal(ListDésLancés)

#----------------------------------------------------------------------------------------------------------------------#

def is_Suite(ListValeursTriées):
    """
    Entrée: ListValeursTriées:  Contient les valeurs de chaque dés, triées
    Sortie: Vrai ou Faux si il y a ou non une suite
    """
    # On doit vérifier que les valeurs se suivent
    #  ex : 2 3 4 5 6
    # On vérifie que l'écart est toujours 1 entre 2 valeurs successives
    for i in range(len(ListValeursTriées)-1):
        if ListValeursTriées[i+1] - ListValeursTriées[i] != 1:
            return False
    return True

#----------------------------------------------------------------------------------------------------------------------#

def is_GrdSuite(DicoDésLancés):
    """
    Entrée: DicoDésLancés:  Contient les valeurs de chaque dés
    Sortie: Vrai ou Faux si il y a ou non un une grande suite
    """
    # Il n'y a que 2 combinaisons possibles
    # Solution 1 : 1 2 3 4 5
    # Solution 2 : 2 3 4 5 6
    # On va commencer par trier les valeurs
    ValeursTriées = sorted(DicoDésLancés.values())
    return is_Suite(ValeursTriées)

#----------------------------------------------------------------------------------------------------------------------#

def is_PetSuite(DicoDésLancés):
    """
    Entrée: DicoDésLancés:  Contient les valeurs de chaque dés
    Sortie: Vrai ou Faux si il y a ou non une petite suite
    """
    # Il n'y a que 5 combinaisons possibles ou plutôt des motifs possibles
    # Solution 1 : X 2 3 4 5 avec X = 1
    # Solution 2 : 1 X 2 3 4 avec X = 1 ou 2
    # Solution 3 : 1 2 X 3 4 avec X = 2 ou 3
    # Solution 4 : 1 2 3 X 4 avec X = 3 ou 4
    # Solution 5 : 1 2 3 4 X avec X = 4 ou 5

    # On commence par vérifier si c'est une grande suite
    if is_GrdSuite(DicoDésLancés):
        return True

    # On va commencer par trier les valeurs
    ValeursTriées = sorted(DicoDésLancés.values())

    # On teste les 4 premières valeurs
    SousValeursTriées = ValeursTriées[0:4]
    if is_Suite(SousValeursTriées):
        return True

    # On teste les 4 dernières valeurs
    SousValeursTriées = ValeursTriées[1:5]
    if is_Suite(SousValeursTriées):
        return True

    # On teste les 4 valeurs du milieu
    SousValeursTriées = ValeursTriées[0:1] + ValeursTriées[2:5]
    if is_Suite(SousValeursTriées):
        return True

    # On teste les 4 valeurs du milieu
    SousValeursTriées = ValeursTriées[0:2] + ValeursTriées[3:5]
    if is_Suite(SousValeursTriées):
        return True

    # On teste les 4 valeurs du milieu
    SousValeursTriées = ValeursTriées[0:3] + ValeursTriées[4:5]
    if is_Suite(SousValeursTriées):
        return True

    return False

#----------------------------------------------------------------------------------------------------------------------#

def is_Full_NM(ValeursTriées, N, M):
    """
    Entrée: ValeursTriées:  Contient les valeurs de chaque dés, triées; N et M:  Nombre de tours de boucle depuis le début de la liste (N) et depuis N (M)
    Sortie: Vrai ou Faux si il y a ou non une combinaison full
    """
    # On vérifie la combinaison
    # Solution 1 : 1 1 1 2 2

    # On extrait les N premières valeurs
    ListDésLancés_debut = []
    for i in range(N):
        ListDésLancés_debut.append(ValeursTriées[i])

    # On vérifie si les valeurs sont identiques
    if is_UniqueVal(ListDésLancés_debut):

        # On extrait les M dernières valeurs
        ListDésLancés_fin = []
        for i in range(M):
            ListDésLancés_fin.append(ValeursTriées[i+N])

        # On vérifie si les valeurs sont identiques
        if is_UniqueVal(ListDésLancés_fin):
            return True

    return False

#----------------------------------------------------------------------------------------------------------------------#

def is_Full(DicoDésLancés):
    """
    Entrée: DicoDésLancés:  Contient les valeurs de chaque dés
    Sortie: Vrai ou Faux si il y a ou non un full
    """
    # Il n'y a que 2 combinaisons possibles
    # Solution 1 : 1 1 1 2 2
    # Solution 2 : 1 1 2 2 2
    # On va commencer par trier les valeurs
    ValeursTriées = sorted(DicoDésLancés.values())

    # On teste la première combinaison
    if is_Full_NM(ValeursTriées, 3, 2):
        return True

    # On teste la seconde combinaison
    if is_Full_NM(ValeursTriées, 2, 3):
        return True

    return False

#----------------------------------------------------------------------------------------------------------------------#

def is_Brelan(DicoDésLancés):
    """
    Entrée: DicoDésLancés:  Contient les valeurs de chaque dés
    Sortie: Vrai ou Faux si il y a ou non un brelan
    """
    # Il n'y a que 3 combinaisons possibles
    # Solution 1 : 1 1 1 2 3
    # Solution 2 : 1 2 2 2 3
    # Solution 2 : 1 2 3 3 3
    # On va commencer par trier les valeurs
    ValeursTriées = sorted(DicoDésLancés.values())

    # On extrait les 3 premières valeurs
    ListDésLancés = []
    for i in range(3):
        ListDésLancés.append(ValeursTriées[i])

    # On vérifie si les valeurs sont identiques
    if is_UniqueVal(ListDésLancés):
        return True, DATA.Brelan_debut

    # On extrait les 3 valeurs suivantes
    ListDésLancés = []
    for i in range(3):
        ListDésLancés.append(ValeursTriées[i+1])

    # On vérifie si les valeurs sont identiques
    if is_UniqueVal(ListDésLancés):
        return True, DATA.Brelan_milieu

    # On extrait les 3 dernières valeurs
    ListDésLancés = []
    for i in range(3):
        ListDésLancés.append(ValeursTriées[i+2])

    # On vérifie si les valeurs sont identiques
    if is_UniqueVal(ListDésLancés):
        return True, DATA.Brelan_fin

    return False, DATA.Brelan_absent

#----------------------------------------------------------------------------------------------------------------------#

def Affich_Dés(DicoDésLancés):
    """
    Entrée: DicoDésLancés:  Contient les valeurs de chaque dés
    """
    # print("----------------------------")
    # print("Dé N°  : 1 | 2 | 3 | 4 | 5 |")
    # print("        --------------------")
    # print("Valeur : 1 | 2 | 3 | 4 | 5 |")
    # print("----------------------------")

    print("----------------------------")
    print("Dé N°  : 1 | 2 | 3 | 4 | 5 |")
    print("        --------------------")
    s_Ligne = "Valeur : "
    for i, elt in enumerate(DicoDésLancés.items()):
        s_Ligne = s_Ligne + str(elt[1]) + ' | '
    print(s_Ligne)
    print("----------------------------")

    return

#----------------------------------------------------------------------------------------------------------------------#

def get_ScoreBrelan(DicoDésLancés, type_Brelan):
    """
    Entrée: DicoDésLancés:  Contient les valeurs de chaque dés; type_Brelan:  contient - 1, 1, 2 ou 3 selon le type de brelan (début, milieu, fin)
    Sortie: score:  Le nombre de points obtenus avec le brelan
    """
    # Il y a 3 types de Brelan
    # Solution 1 : 1 1 1 2 3
    # Solution 2 : 1 2 2 2 3
    # Solution 2 : 1 2 3 3 3

    score = 0
    # On va commencer par trier les valeurs
    ValeursTriées = sorted(DicoDésLancés.values())

    if type_Brelan == DATA.Brelan_debut:
        for i in range(3):
            score += ValeursTriées[i]
    elif type_Brelan == DATA.Brelan_milieu:
        for i in range(3):
            score += ValeursTriées[i+1]
    elif type_Brelan == DATA.Brelan_fin:
        for i in range(3):
            score += ValeursTriées[i+2]

    return score

#----------------------------------------------------------------------------------------------------------------------#

def get_ScoreCarre(DicoDésLancés, type_Carre):
    """
    Entrée: DicoDésLancés:  Contient les valeurs de chaque dés; type_Carre:  contient - 1, 1 ou 2 selon le type de carré (début, fin)
    Sortie: score:  Le nombre de points obtenus avec le carré
    """
    # Il y a 2 types de Carrés
    # Solution 1 : 1 1 1 1 2
    # Solution 2 : 2 3 3 3 3

    score = 0
    # On va commencer par trier les valeurs
    ValeursTriées = sorted(DicoDésLancés.values())

    if type_Carre == DATA.Carre_debut:
        for i in range(4):
            score += ValeursTriées[i]
    elif type_Carre == DATA.Carre_fin:
        for i in range(4):
            score += ValeursTriées[i+1]

    return score

#----------------------------------------------------------------------------------------------------------------------#

def get_ScoreChance(DicoDésLancés):
    """
    Entrée: DicoDésLancés:  Contient les valeurs de chaque dés
    Sortie: score:  Le nombre de points obtenus avec les dés lancés
    """

    score = 0
    for clé, val in DicoDésLancés.items():
        score += val

    return score

#----------------------------------------------------------------------------------------------------------------------#

def is_X(DicoDésLancés, X):
    """
    Entrée: DicoDésLancés:  Contient les valeurs de chaque dés; X un nombre entier entier
    Sortie: Vrai ou Faux si X est présent ou non
    """

    for clé, val in DicoDésLancés.items():
        if val == X:
            return True

    return False

#----------------------------------------------------------------------------------------------------------------------#

def get_ScoreX(DicoDésLancés, X):
    """
    Entrée: DicoDésLancés:  Contient les valeurs de chaque dés; X un nombre entier
    Sortie: score:  Le nombre de points obtenus avec les dés lancés
    """

    score = 0
    for clé, val in DicoDésLancés.items():
        if val == X:
            score += X

    return score

#----------------------------------------------------------------------------------------------------------------------#

def get_SousTotal(FeuilleScore, JoueurActif):
    """
    Entrée: FeuilleScore:  La feuille de score avec les points des joueurs; JoueurActif:  Le joueur qui joue ce tour
    Sortie: score:  Le nombre de points obtenus pour le sous total
    """
    score = 0
    for i in range(6):
        score += FeuilleScore[i][JoueurActif-1]

    return score

#----------------------------------------------------------------------------------------------------------------------#

def get_SousTotal2(FeuilleScore, JoueurActif):
    """
    Entrée: FeuilleScore:  La feuille de score avec les points des joueurs; JoueurActif:  Le joueur qui joue ce tour
    Sortie: score:  Le nombre de points obtenus pour le total
    """
    score = 0
    for i in range(7):
        score += FeuilleScore[i+9][JoueurActif-1]

    return score

#----------------------------------------------------------------------------------------------------------------------#

def Affich_ErreurDés(DicoDésLancés, DicoJoué, ChoixScore):
    """
    Entrée: FeuilleScore:  La feuille de score avec les points des joueurs; DicoJoué dictionnaire de tuples permettant d'analyser si le joueur actif a déja rempli ou non une case de sa fiche; ChoixScore la case à remplir choisie
    """

    print()
    Affich_Dés(DicoDésLancés)
    print("{} n'est pas disponible avec vos dés".format(DicoJoué[ChoixScore][0]))
    print()


#----------------------------------------------------------------------------------------------------------------------#

def check_IfGagnant(ListFeuillesChoixJoueurs, JoueurActif):
    """
    Entrée: ListFeuillesChoixJoueurs:  dictionnaire de tuples permettant d'analyser si les joueurs ont déja rempli ou non une case de leurs fiches; JoueurActif:  Le joueur qui joue ce tour
    Sortie: 0: Pas de gagnant; JoueurActif: Le JoueurActif est gagnant
    """

    DicoJoué = ListFeuillesChoixJoueurs[JoueurActif - 1]

    for val in DicoJoué.values():
        if val[1] == False:
            return 0
        else:
            return JoueurActif  # Toutes les cases de la fiche sont pleines;
