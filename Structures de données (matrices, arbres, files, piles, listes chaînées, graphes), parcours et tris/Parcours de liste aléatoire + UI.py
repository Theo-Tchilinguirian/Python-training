# Tchilinguirian Théo Maxim Costa 103
# 29/11/2019 - 12/12/2019

# Les algorithmes de première / Exercices
#----------------------------------------

# Imports
#-------------------

from random import *


# Fonctions d'entrées et de sortie
#---------------------------------



# Fonctions Métiers
#-------------------

def ListAlea(n, M):

    return [randint(1, M) for k in range(0, n)]


def MinMaxMoy(Liste):  # 1
    """
    Données:
    Liste un tableau unidimensionnel constitué de nombres entiers relatifs
    Résultat:
    Le minimum, le maximum, et la moyenne des valeurs de la liste
    """
    Min = Liste[0]
    Max = Liste[0]
    Som = Liste[0]
    for k in range(1, len(Liste)-1):
        Som += Liste[k]
        if Liste[k] < Min:
            Min = Liste[k]
        elif Liste[k] > Max:
            Max = Liste[k]
    Moy = Som / len(Liste)

    return Min, Max, Moy


def CompteCar(txt, Car):  # 2
    """
    Données:
    txt une chaine de caractère
    Car un caractère
    Résultat:
    Cpt le nombre d'occurences de Car dans txt
    """
    Cpt = 0
    for i in txt:
        if Car == i:
           Cpt += 1

    return Cpt


def CompteMax(Liste):  # 3
    """
    Données:
    Liste une liste constitué de nombres entiers relatifs
    Résultat:
    Le maximum final et le nombre de fois qu'on a rencontré un maximum
    """
    Max = Liste[0]
    Cpt = 1
    for i in range(1, len(Liste)-1):
        if Liste[i] >= Max:
            Max = Liste[i]
            Cpt += 1
    return Max, Cpt


def LocaliseMax(Liste):  # 4
    """
    Données:
    Liste un tableau unidimensionnel(liste) constitué de nombres entiers relatifs
    Résultat:
    Le maximum final et les indices des maximums
    """
    Max = Liste[0]
    Indices = []
    for i in range(1, len(Liste)-1):
        if Liste[i] > Max:
            Max = Liste[i]
    for k in range(len(Liste)):
        if Liste[k] == Max:
            Indices += [k]

    return Max, Indices


#----------------------------------
# Programme Principal
#----------------------------------

rep = 1
while rep != 0:
    Choix = int(input("""Que voulez vous faire?
    1. Calcul minimum, maximum et moyenne d'une liste
    2. Compter le nombre d'occurences d'un caractère dans un texte
    3. Nombre de fois qu'on atteint le maximum
    4. Indices du maximum
    Votre choix (1, 2, 3 ou 4...): """))
    if Choix == 1:
        LongListe = int(input("Longueur de la liste?: "))
        MaxRand = int(input("Maximum du random?: "))
        Liste = ListAlea(LongListe, MaxRand)
        print("La liste est", Liste)

        ResMin, ResMax, ResMoy = MinMaxMoy(Liste)
        print("Le minimum de la liste est {}, le maximum est {} et la moyenne des valeurs est {} dans la liste {}".format(ResMin, ResMax, ResMoy, Liste))
    if Choix == 2:
        Txt = input("Texte: ")
        Car = input("Caractère: ")
        NombreDocc = CompteCar(Txt, Car)
        print("Le nombre de {} dans le texte est {}".format(Car, NombreDocc))
    if Choix == 3:
        LongListe = int(input("Longueur de la liste?: "))
        MaxRand = int(input("Maximum du random?: "))
        Liste = ListAlea(LongListe, MaxRand)
        print("La liste est", Liste)

        Max, Cpt = CompteMax(Liste)
        print("Le maximum de la liste est {}, le nombre d'occurences du maximum dans la liste est {}".format(Max, Cpt))
    if Choix == 4:
        LongListe = int(input("Longueur de la liste?: "))
        MaxRand = int(input("Maximum du random?: "))
        Liste = ListAlea(LongListe, MaxRand)
        print("La liste est", Liste)

        Max, Indices = LocaliseMax(Liste)
        print("Le maximum de la liste est {}, les indices des maximums rencontrés dans la liste parcourue est {}".format(Max, Indices))

    rep = int(input("Réessayer? (oui: 1 / non: 0): "))