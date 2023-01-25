# Tchilinguirian Théo Maxim Costa 103
# 29/11/2019 - 12/12/2019

# Les algorithmes de première / Exercices
#----------------------------------------

# Imports
#-------------------

from random import randint


# Fonctions d'entrées et de sortie
#---------------------------------

def zero(v):
    """
    Fonction appelée par AffichTab4()
    renvoie un certain nombre d'espaces selon la taille du nombre
    """
    if 100 <= v < 1000:
        return ' '
    elif 10 <= v < 100:
        return '  '
    elif v < 10:
        return '  '
    else:
        return ''


def InitListeAlea():
    """
    Fonction d'input
    Cette fonction est appelée dans la fonction menu()
    elle permet  d'éviter de répéter plusieurs lignes de code
    """
    LongListe = int(input("Longueur de la liste?: "))
    Min = int(input("Minimum du random?: "))
    Max = int(input("Maximum du random?: "))

    return LongListe, Min, Max


def InitTabAlea():
    """
    Fonction d'input
    Cette fonction est appelée dans la fonction menu()
    elle permet  d'éviter de répéter plusieurs lignes de code
    """
    n = int(input("nombre de lignes: "))
    m = int(input("nombre de colonnes: "))
    Min = int(input("Minimum du random?: "))
    Max = int(input("Maximum du random?: "))

    return n, m, Min, Max


def AffichTab1(tab):
    """
    Fonction d'affichage
    Affiche un tableau sur plusieurs lignes
    """
    return [print(tab[i]) for i in range(len(tab))]


def AffichTab2(tab):
    """
    Fonction d'affichage
    Affiche un tableau sur plusieurs lignes, en plus d'un ruban de tirets encadrant les premières et dernières lignes
    """
    print('-'*(2*len(tab[0])-1))  # ruban de tirets variant selon la taille du tableau (de nombres à un chiffre)
    for i in tab:
        for j in i:
            print(j, end=' ')  # paramètre "end" de la fonction print qui prend pour valeur par défaut "\n" (saut de ligne)
        print()  # saut de ligne
    print('-'*(2*len(tab[0])-1))

def AffichTab3(tab):
    """
    Fonction d'affichage
    Affiche un tableau sur plusieurs lignes, chaque nombre est encadré dans une case du tableau
    """
    print('-'*(4*len(tab[0])+1))
    for i in tab:
        print('|', end=' ')
        for j in i:
            print(j, end=' | ')
        print()
        print('-'*(4*len(tab[0])+1))


def AffichTab4(tab):
    """
    Fonction d'affichage
    Affiche un tableau sur plusieurs lignes, chaque nombre est encadré dans une case du tableau,
    la taille des cases est rendue constante selon la taille des nombres qui constituent le tableau
    """
    print('-'*(7*len(tab[0])+1))
    for i in tab:
        print('|', end=' ')
        for j in i:
            print(zero(j)+str(j), end=' | ')
        print()
        print('-'*(7*len(tab[0])+1))


def menu():
    """
    Fonction menu qui appelle les fonctions définies
    constitue le programme principal
    """
    rep = 1
    while rep != 0:
        input("tapez 'enter' pour continuer")

        Choix = int(input("""Que voulez vous faire?
        
        LISTES:
        1. Recherche minimum et maximum d'une liste
        2. Le maximum et le nombre de fois qu'il est atteint
        3. Indices d'une valeur
        4. Permuter deux valeurs
        
        TABLEAUX:
        5. Tableau de n lignes et m colonnes n'ayant que des 1 sur la 1ere ligne, 2 sur la 2eme...
        6. Tableau de n lignes et m colonnes n'ayant que des 1 sur la 1ere colonne, 2 sur la 2eme...
        7. renvoie un tableau dont les valeurs du cadre ont été remplacées par 0
        8. renvoie un tableau dont les valeurs des diagonales ont été remplacées par 0
        
        POUR ALLER PLUS LOIN:
        9. test- AffichTab1(TabAlea)
        10. test- AffichTab2(TabAlea) (pour un tableau de nombres à un chiffre)
        11. test- AffichTab3(TabAlea) (pour un tableau de nombres à un chiffre)
        12. test- AffichTab4(TabAlea)
        13. Champ miné de façon aléatoire
        
        13. Quitter
        
        Votre choix (1, 2, 3, 4...): """))

        if Choix == 1:  # 1. Recherche minimum et maximum d'une liste
            LongListe, Min, Max = InitListeAlea()
            Liste = ListAlea(LongListe, Min, Max)
            print("La liste est", Liste)

            ResMin, ResMax = MinMax(Liste)
            print("Le minimum de la liste est {} et le maximum est {} dans la liste {}".format(ResMin, ResMax, Liste))

        elif Choix == 2:  # 2. Le maximum et le nombre de fois qu'il est atteint
            LongListe, Min, Max = InitListeAlea()
            Liste = ListAlea(LongListe, Min, Max)
            print("La liste est", Liste)

            Max, Cpt = ComptMax(Liste)
            print("Le maximum de la liste est {}, le nombre d'occurences du maximum dans la liste est {}".format(Max, Cpt))

        elif Choix == 3:  # 3. Indices d'une valeur
            LongListe, Min, Max = InitListeAlea()
            Liste = ListAlea(LongListe, Min, Max)
            print("La liste est", Liste)
            elt = int(input("Valeur numérique à rechercher dans la liste: "))

            Indices = Localise(Liste, elt)
            print("Les indices de la valeur recherchée dans la liste sont {}".format(Indices))

        elif Choix == 4:  # 4. Permuter deux valeurs
            LongListe, Min, Max = InitListeAlea()
            Liste = ListAlea(LongListe, Min, Max)
            print("La liste est", Liste)
            i = int(input("indice de la première valeur à permuter (inclu dans la liste): " ))
            j = int(input("indice de la seconde valeur à permuter (inclu dans la liste): " ))

            ResListe = Permute(Liste, i, j)
            print("La liste avec les valeurs permutées est {}".format(ResListe))

        elif Choix == 5:  # 5. Tableau de n lignes et m colonnes n'ayant que des 1 sur la 1ere ligne, 2 sur la 2eme...
            n = int(input("nombre de lignes: "))
            m = int(input("nombre de colonnes: "))

            AffichTab3(Ligne(n, m))

        elif Choix == 6:  # 6. Tableau de n lignes et m colonnes n'ayant que des 1 sur la 1ere colonne, 2 sur la 2eme...
            n = int(input("nombre de lignes: "))
            m = int(input("nombre de colonnes: "))

            AffichTab3(Colonne(n, m))

        elif Choix == 7:  # 7. renvoie un tableau dont les valeurs du cadre ont été remplacées par 0
            n, m, Min, Max = InitTabAlea()
            Tableau = TabAlea(n, m, Min, Max)
            print("Le tableau est", Tableau)

            AffichTab3(Cadre(Tableau))

        elif Choix == 8:  # 8. renvoie un tableau dont les valeurs des diagonales ont été remplacées par 0
            n, m, Min, Max = InitTabAlea()
            Tableau = TabAlea(n, m, Min, Max)
            print("Le tableau est", Tableau)

            AffichTab3(Diag(Tableau))

        elif Choix == 9:  # 9. test- AffichTab1(TabAlea)
            n, m, Min, Max = InitTabAlea()
            Tableau = TabAlea(n, m, Min, Max)
            print("Le tableau est", Tableau)

            AffichTab1(Tableau)

        elif Choix == 10:  # 10. test- AffichTab2(TabAlea)
            n, m, Min, Max = InitTabAlea()
            Tableau = TabAlea(n, m, Min, Max)
            print("Le tableau est", Tableau)

            AffichTab2(Tableau)

        elif Choix == 11:  # 11. test- AffichTab3(TabAlea)
            n, m, Min, Max = InitTabAlea()
            Tableau = TabAlea(n, m, Min, Max)
            print("Le tableau est", Tableau)

            AffichTab3(Tableau)

        elif Choix == 12:  # 12. test- AffichTab4(TabAlea)
            n, m, Min, Max = InitTabAlea()
            Tableau = TabAlea(n, m, Min, Max)
            print("Le tableau est", Tableau)

            AffichTab4(Tableau)

        elif Choix == 13:  # 13. Champ miné de façon aléatoire
            n = int(input("nombre de lignes et de colonnes: "))

            AffichTab3(mine(n))

        else:  # 13. Quitter
            rep = 0


# Fonctions Métiers (LISTES)
#---------------------------

def ListAlea(n, a, b):
    """
    Données:
            a < b
            a le nombre le plus grand à pouvoir être créé dans la liste
            b le nombre le plus petit à pouvoir être créé dans la liste
    Résultat:
            renvoie une liste de n entiers constituée de nombres aléatoires compris entre a et b
    """
    return [randint(a, b) for k in range(0, n)]


def MinMax(Liste):  # 1
    """
    Données:
            Liste: un tableau unidimensionnel constitué de nombres entiers relatifs
    Résultat:
            Min, Max: Le minimum et le maximum des valeurs de la liste
    """
    Min = Liste[0]
    Max = Liste[0]
    for k in range(1, len(Liste)):
        if Liste[k] < Min:
            Min = Liste[k]
        elif Liste[k] > Max:
            Max = Liste[k]

    return Min, Max


def ComptMax(Liste):  # 2
    """
    Données:
            Liste: une liste constitué de nombres entiers relatifs
    Résultat:
            Le maximum final et le nombre de fois qu'on l'a rencontré
    """
    Max = Liste[0]
    Cpt = 1
    for i in range(1, len(Liste)):
        if Liste[i] > Max:
            Max = Liste[i]
            Cpt = 1  # Lorsque qu'un nouveau maximum est trouvé, le compteur se réinitialise à 1
        elif Liste[i] == Max:
            Cpt += 1

    return Max, Cpt


def Localise(Liste, elt):  # 3
    """
    Données:
            Liste: un tableau unidimensionnel(liste) constitué de nombres entiers relatifs
            elt: l'élement recherché
    Résultat:
            Indices: liste des indices de l'élément recherché
    """
    Indices = []
    for k in range(len(Liste)):
        if Liste[k] == elt:
            Indices += [k]

    return Indices


def Permute(Liste, i, j):  # 4
    """
    Données:
            Liste: la liste sur laquelle le programme va travailler
            i et j les éléments à permuter
    Résultat:
            Liste: la liste d'origine, i et j permutés
    """
    Vali = Liste[i]  # Vali: la valeur de i sauvegardée
    Liste[i] = Liste[j]  # Echange des valeurs de i et j
    Liste[j] = Vali  # Récupération de la valeur de i retenue plus tôt

    return Liste


# Fonctions Métiers (TABLEAUX)
#---------------------------

def TabAlea(n, m, a, b):
    """
    Données:
            n et m: le nombre de lignes (n) et de colonnes (m) du tableau
            a et b des nombres aléatoires pour a < b
    Résultat:
             un tableau constitué de nombres aléatoires compris entre a et b
    """
    return [[randint(a, b) for j in range(m)] for i in range(n)]


def Ligne(n, m):
    """
    Données:
            n et m: le nombre de lignes (n) et de colonnes (m) du tableau
    Résultat:
            un tableau n'ayant que des 1 sur la première ligne, des 2 sur la deuxième, ...
    """
    return [[i for j in range(m)] for i in range(1, n + 1)]


def Colonne(n, m):
    """
    Données:
            n et m: le nombre de lignes (n) et de colonnes (m) du tableau
    Résultat:
            un tableau n'ayant que des 1 sur la première colonne            n et m: le nombre de lignes (n) et de colonnes (m) du tableau, des 2 sur la deuxième, ...
    """
    return [[j for j in range(1, m + 1)] for i in range(n)]


def Cadre(T):
    """
    Données:
            T: le tableau à modifier
    Résultat:
            un tableau dont les valeurs des éxtrémitées (le cadre) ont été remplacées par 0
    """
    T = [[0] + T[i] + [0] for i in range(len(T))]
    T = [[0] * len(T[0])] + T + [[0] * len(T[0])]
    return T


def Diag(T):
    """
    Données:
            T: le tableau à modifier
    Résultat:
            T: le tableau d'origine dont les valeurs en diagonales ont été remplacées par 0
    """
    for i in range(len(T)):
        T[i][i] = 0
        T[i][-i - 1] = 0
    return T


def mine(n):
    """
    Données:
            n: le nombre de lignes et de colonnes du champ de mines
    Résultat:
            L un tableau représentant un champ miné de façon aléatoire
    """
    L = []
    sp = [-1]
    for i in range(n):
        L.append([])
        V0 = -1
        while V0 in sp:
            V0 = randint(0, n)
        sp.append(V0)
        for j in range(n):
            if j == V0:
                L[i].append(1)
            else:
                L[i].append(0)
    return L


#----------------------------------
# Programme Principal
#----------------------------------

menu()
