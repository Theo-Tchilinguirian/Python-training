# tests fonctions morpion


Tableau = [['[ ]', '[ ]', '[ ]'],
           ['[ ]', '[ ]', '[ ]'],
           ['[ ]', '[ ]', '[ ]']]

def AfficherTableau(Tableau):

    LenTab = len(Tableau)
    print('|-----|-----|-----|')
    for i in Tableau:
        for j in i:
            print('|', end=' ')
            print(j, end=' ')
        print('|')
    print('|-----|-----|-----|')


def Swapper(Tableau):

    Ligne = 0
    Colonne = 0
    Tableau[Ligne][Colonne] = '[+]'
    AfficherTableau(Tableau)

    rep = True
    while rep != 'q' or 'Q':
        print("q: Quitter, c: Choisir la case, enter: Changer de case")
        rep = input("rep: ")
        if rep == str():
            ALigne, AColonne = Ligne, Colonne
            FLigne, FColonne = Swap(Tableau, Ligne, Colonne)

            if Tableau[FLigne][FColonne] == '[X]':
                k = 0
                while Tableau[FLigne][FColonne] == '[X]':
                    FLigne, FColonne = Swap(Tableau, Ligne, Colonne)
                    k += 1
                    print(k)
                    for i in range(k):
                        Ligne, Colonne = Swap(Tableau, Ligne, Colonne)


                Ligne, Colonne = Swap(Tableau, Ligne, Colonne)
                Tableau[ALigne][AColonne] = '[ ]'
                Ligne, Colonne = Swap(Tableau, Ligne, Colonne)
                Tableau[Ligne][Colonne] = '[+]'

            else:
                Ligne, Colonne = Swap(Tableau, Ligne, Colonne)
                Tableau[Ligne][Colonne] = '[+]'
                Tableau[ALigne][AColonne] = '[ ]'

            AfficherTableau(Tableau)
        elif rep == 'c':
            ALigne, AColonne = Ligne, Colonne
            Ligne, Colonne = Swap(Tableau, Ligne, Colonne)
            Tableau[Ligne][Colonne] = '[+]'
            Tableau[ALigne][AColonne] = '[X]'
            AfficherTableau(Tableau)


def Swap(Tableau, Ligne, Colonne):

    if Colonne == Ligne == 2:
        Ligne = 0
        Colonne = 0
    elif Colonne == 2:
        Ligne += 1
        Colonne = 0
    else:
        Colonne += 1

    return Ligne, Colonne


Swapper(Tableau)