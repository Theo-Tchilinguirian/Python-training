# Imports:
from random import randint


# Fichier des fonctions métiers de "App2"
# i et n représentent les lignes et j et m les colonnes

def AffichTab1(tab):
    """
    """

    for i in range(len(tab)):
        print(tab[i])


def TabAlea(n, m, M):
    """
    """
    return [[randint(0, M) for j in range(m)] for i in range(n)]


def Damier(i, j):
    Damier = []
    for n in range(i):
        [[]]
        for m in range(j):
            if (n + m) % 2 == 0:
                Damier[i] += ["B"]
            else:
                Damier[i] += ["N"]
    # [[(n+m) % 2 == 0 for m in range(j)] for n in range(i)]
    return Damier


def Ligne(n, m):
    Tab = []
    for i in range(n):
        Tab += [[]]
        for j in range(m):
            Tab[i] += [i + 1]
    return Tab


def Colonne(n, m):
    Tab = []
    for i in range(n):
        Tab += [[]]
        for j in range(m):
            Tab[i] += [j + 1]
    return Tab


def Diag(Tableau):
    Tab = []
    for i in range(len(Tableau)):
        Tab += [[]]
        for j in range(len(Tableau[0])):
            if i == j:
                Tab[i] = [0]
            else:
                Tab[i] = [Tableau[i][j]]

    return Tab


def Cadre(Tableau):
    Tab = []
    for i in range(len(Tableau)):
        Tab += [[]]
        for j in range(len(Tableau[0])):
            if i == 0 or i == len(Tableau) - 1:
                Tab[i] += [1]
            else:
                Tab[i] += [0]
            if j == 0 or j == len(Tableau[0]) - 1:
                Tab[i][j] += 1
            else:
                Tab[i][j] += 0

    return Tab
print(Cadre([[2,4,3,3,5],[1,2,5,6,3]]))
