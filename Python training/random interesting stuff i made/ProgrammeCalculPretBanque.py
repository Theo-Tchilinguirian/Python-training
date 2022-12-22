
# Affiche le TAM: tableau d'amortissement mensuel

import os


Capital0 = float(input("Montant à emprunter à la banque: "))
DureeAnnees = int(input("Nombre d'années pour rembourser: "))
TauxIntrsAnnuels = float(input("Taux d'intérêts annuels (en pourcents): "))
print("\nLa mensualité ne doit pas dépasser 33% de vos revenus net mensuels, ou le prêt sera refusé.\n")

# Calcul des intérêts:  (le taux d'intérêts mensuels change tous les mois; car le capital restant à rembourser diminue chaque mois)

TauxIntrsMensuels = TauxIntrsAnnuels/12
IntrsMensuels = TauxIntrsMensuels/100  # On divise par 12 à la fin afin d'obtenir le coefficient d'intérêts sur le capital restant 'mensuel'

# Calcul de la mensualité:  (valeur constante; part du capital à rembourser à la banque avec intérêts)

DureeMois = DureeAnnees * 12

M = (Capital0 * IntrsMensuels) / (1-((1 + IntrsMensuels)**-DureeMois))  # (Capital0 * IntrsMensuels)  -> Les intérêts que l'on doit à la banque pour le premier mois

CapitalHorsIntrs = M - (Capital0 * IntrsMensuels)
IntrsHorsCapital = (Capital0*IntrsMensuels)


CapitalRestant = Capital0
SommeIntrsCrdt = IntrsHorsCapital

for Année in range(1, DureeAnnees + 1):

    print("Année:     Mois:     Capital restant à rembourser au début du mois:               Capital à rembourser à la fin du mois (mensualité):               Capital à rembourser sans intérêts:               Intérêts du capital (en pourcents et euros):     ")

    for Mois in range(1, 13):
        print("{}".format(Année).format(5), end='')
        print("{}".format(Mois).center(30), end='')
        print("{}".format(round(CapitalRestant, 5)).center(45), end='')
        print("{}".format(round(M, 5)).center(50), end='')
        print("{}".format(round(CapitalHorsIntrs, 5)).center(70), end='')
        print("{}     {}".format(round(TauxIntrsMensuels, 5), round(IntrsHorsCapital, 5)).center(35))

        CapitalRestant = CapitalRestant - CapitalHorsIntrs
        CapitalHorsIntrs = M - (CapitalRestant * IntrsMensuels)
        IntrsHorsCapital = (CapitalRestant*IntrsMensuels)

        SommeIntrsCrdt += IntrsHorsCapital

    print()

    Année += 1

print("Somme des intérêts du crédit:", round(SommeIntrsCrdt, 5), '\n')

os.system('pause')
