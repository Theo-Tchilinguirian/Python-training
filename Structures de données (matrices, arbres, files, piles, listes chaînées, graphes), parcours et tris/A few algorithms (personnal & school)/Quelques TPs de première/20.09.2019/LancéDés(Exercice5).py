from random import *

while rep != 0:
    ValeurUne1 = randint(1, 6)
    ValeurDeux1 = randint(1, 6)
    ValeurUne2 = randint(1, 6)
    ValeurDeux2 = randint(1, 6)

    print("Le joueur 1 a obtenu", ValeurUne1, "et", ValeurDeux1)
    print("Le joueur 2 a obtenu", ValeurUne2, "et", ValeurDeux2)

    ValJoueur1 = ValeurUne1 + ValeurDeux1
    ValJoueur2 = ValeurUne2 + ValeurDeux2

    if ValJoueur1 > ValJoueur2:
        print("Le joueur 1 gagne", ValJoueur1, "Contre", ValJoueur2)
    elif ValJoueur1 < ValJoueur2:
        print("Le joueur 2 gagne", ValJoueur2, "Contre", ValJoueur1)
    elif ValJoueur1 == ValJoueur2:
        print("Egalité!")

    rep = int(input("rejouer? 0/1: "))