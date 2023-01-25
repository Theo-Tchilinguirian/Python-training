
from random import randint


def CompteurMotsLettres(string):
    """
    string: une chaine de caractères
    Renvoie un tuple de valeurs: (nombre de mots, liste du nombre de lettres par mot)
    """
    liste = [0]
    i = 0
    for lettre in string:
        if lettre is not ' ':
            liste[i] += 1
        else:
            liste.append(0)
            i += 1
    return i+1, liste


def MélangeurLetterCase(string):  # Rend tout sarcastique
    """
    string: une chaine de caractères
    Renvoie: NvString: la chaine de caractères modifiée
    """
    nvString = str()
    for lettre in string:
        randomInteger = randint(0, 1)
        if randomInteger == 0:
            nvString += lettre.upper()
        else:
            nvString += lettre.lower()
    return nvString


def RechercherMot(string, mot):
    """
    string: une chaine de caractères
    mot: une chaine de caractères
    Renvoie: indiceMot: l'indice de la première lettre du mot recherché dans string
    """
    indiceMot = int()
    lettreVerif = len(mot) * [False]
    for indiceLettre in range(len(string)):
        if string[indiceLettre] == mot[0]:  # On est tombé sur le mot
            indiceMot = indiceLettre
            for indice in range(len(mot)):
                if string[indiceLettre + indice] == mot[indice]:
                    lettreVerif[indice] = True
                else:
                    lettreVerif = len(mot) * [False]
                    break
            if False not in lettreVerif:
                return indiceMot

# tests

string = "Une chaîne de caractères" \
         " >-|-< To be or not to be"
print(CompteurMotsLettres(string))
for k in range(10):
    string = MélangeurLetterCase(string)
    print(string)

string = "sandwich, serpent, fourbe, et métalexicographie ! haha."

print(RechercherMot(string, "métalexicographie"))
