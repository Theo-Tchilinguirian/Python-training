from random import randint

def SuppCar(Txt, i):
    """
    Données: Txt une chaine de caractères, i un entier inférieur à la longueur de Txt
    Résultat: NvTxt une chaine de caractères correspondant à Txt dont le caractère de rang i a été supprimmé
    """
    NvTxt = ""
    LenTxt = len(Txt)
    for k in range(LenTxt):
        if k != i:
            NvTxt += Txt[k]

    return NvTxt


def AleAlpha():
    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NvAlpha = ""
    for k in Alphabet:
        RangAlea = randint(0, 25)
        if Alphabet[RangAlea] not in NvAlpha:
            NvAlpha += Alphabet[RangAlea]
    return NvAlpha


print(AleAlpha())
