"""
Le module 'UTIL' rassemble des fonctions utiles.
"""

# Imports:
from random import randint

def Get_RandChar(CharMin = 'A', CharMax = 'Z'):
    """
    Entrées:
        CharMin: Lettre majuscule de l'alphabet, doit se trouver avant, ou être la même que CharMax
        CharMax: Lettre majuscule de l'alphabet, doit se trouver après, ou être la même que CharMin
    Sorties:
        RandChar: Lettre majuscule aléatoire entre CharMin et CharMax
    """

    RandMin, RandMax = ord(CharMin), ord(CharMax)

    RandChar = chr(randint(RandMin, RandMax))

    return RandChar


def Get_IndicesMaxMin(ListeNb):
    """
    Entrées:
        ListeNb: Liste de nombres
    Sorties:
        Max: Maximum de la liste; le nombre le plus grand
        IndicesMax: Les indices (positions) du maximum dans la liste
        Min: Minimum de la liste; le nombre le plus petit
        IndicesMin: Les indices (positions) du minimum dans la liste
    """

    Max = ListeNb[0]
    Min = ListeNb[0]
    IndicesMax = [0]
    IndicesMin = [0]

    for i in range(1, len(ListeNb)):
        if ListeNb[i] > Max:
            Max = ListeNb[i]
            IndicesMax = []
        if ListeNb[i] == Max:
            IndicesMax.append(i)

        if ListeNb[i] < Min:
            Min = ListeNb[i]
            IndicesMin = []
        if ListeNb[i] == Min:
            IndicesMin.append(i)

    return Max, IndicesMax, Min, IndicesMin


def MélangeurList(Liste):
    """
    """

    NvListe = []

    for i in range(len(Liste)):
        IndiceHasard = randint(0, len(Liste)-1)
        Elt = Liste.pop(IndiceHasard)
        NvListe.append(Elt)

    return NvListe


def PerlinNoiseAlgorithm(Min=0, Max=10, TailleListe=10):
    """
    """

    RandListe = []
    NbAlea = randint(Min, Max)

    for k in range(TailleListe):

        NvNbAlea = randint(Min + NbAlea, Max + NbAlea)
        RandListe.append(NvNbAlea)
        NbAlea = NvNbAlea
    print(RandListe)

PerlinNoiseAlgorithm(Min=0, Max=10, TailleListe=10)





class Temperature:
    "Classe qui représente une température"

    def __init__(self, temp = 0, deg = 'C'):
        object.__setattr__(self, 'temp', temp)  # On utilise la méthode de la classe objet et non pas "self.temp = temp" car cela appelerait la méthode setattr de notre objet
        object.__setattr__(self, 'deg_type', deg)
        object.__setattr__(self, '_prev_temp', [])

    def __str__(self):
        return 'Température: {}°{}'.format(self.temp, self.deg_type)

    def __getattr__(self, nom_attr):
        """Méthode appelée si l'attribut cherché n'est pas trouvé"""

        print("""L'attribut "{}" n'existe pas.""".format(nom_attr))

    def __setattr__(self, nom_attr, val_attr):
        """Méthode appelée lors de la modification d'un attribut"""

        if type(object.__getattribute__(self, nom_attr)) != list:  # On passe par object pour obtenir le type correct
            print("Vous ne pouvez pas réaffecter cet attribut")
        else:
            print("Modification de la valeur de l'attribut {}. La valeur précédente sera enregistrée.".format(nom_attr))
            object.__setattr__(self, '_prev_temp', {nom_attr:val_attr})
            object.__setattr__(self, nom_attr, val_attr)

    def __delattr__(self, nom_attr):
        """Méthode appelée lorsqu'on essaie de supprimer un attribut"""

        if nom_attr == 'temp' or 'deg_type':
            raise AttributeError("Vous ne pouvez supprimer l'attribut {}.".format(nom_attr))
        else:
            object.__delattr__(self, nom_attr)

    def __getitem__(self, index):
        """Appelée lorsqu'on fait nom_objet[index]"""

        if type(index) == int:
            return self._prev_temp[index]
        else:
            print("type d'index non pris en charge. Utilisez des entier.")

    def __setitem__(self, index, value):
        """Appelée lorsqu'on fait nom_objet[index] = valeur"""

        if type(index) == int:
            self._prev_temp[index] = value  # Pas besoin de return car list est un objet mutable
            # De plus, cette méthode n'appelle pas __setattr__ de la classe
        else:
            print("type d'index non pris en charge. Utilisez des entier.")


a = Temperature()
a._prev_temp = [1]
a._prev_temp[0] = 2
print(a._prev_temp)
