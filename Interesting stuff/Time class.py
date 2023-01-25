
class Temps:

    def __init__(self, secondes=0, minutes=0, heures=0, jours=0, semaines=0):

        self.s = secondes
        self.m = minutes
        self.h = heures
        self.j = jours
        self.se = semaines

        self._actualiser_temps()


    def _actualiser_temps(self):

        if self.s >= 60 :
            (quotient, reste) = (self.s // 60, self.s % 60)
            self.m += quotient
            self.s = reste

        if self.m >= 60 :
            (quotient, reste) = (self.m // 60, self.m % 60)
            self.h += quotient
            self.m = reste

        if self.h >= 24 :
            (quotient, reste) = (self.h // 24, self.h % 24)
            self.j += quotient
            self.h = reste

        if self.j >= 7 :
            (quotient, reste) = (self.j // 7, self.j % 7)
            self.se += quotient
            self.j = reste


    def ajouter_temps(self, unité, qte):

        if unité == 's' :
            self.s += qte

        if unité == 'm' :
            self.m += qte

        if unité == 'h' :
            self.h += qte

        if unité == 'j' :
            self.j += qte

        if unité == 'se' :
            self.se += qte

        self._actualiser_temps()


    def __str__(self):

        repr_temps = "{} semaine et {} jours,\n\t{} heures, {} minutes et {} secondes".format(self.se, self.j, self.h, self.m, self.s)
        return repr_temps

#    def si on ajoute deux objets temps:




# Temps(secondes, minutes, heures, jours, semaines)
t = Temps()  # durées initialisées à 0
t.ajouter_temps('m', 100)  # ajouter 100 minutes

t.h += 56  # ajout manuel de 56 heures :  non recommandé car nécessite une actualisation
t._actualiser_temps()  # ne pas ajouter manuellement le temps.

print(t)
