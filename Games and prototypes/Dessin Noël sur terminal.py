def ligne(l, n):
    NbEspace = int((l - n) / 2)
    l = NbEspace * " " + n * "*" + NbEspace * " " + "\n"
    return l


def trapèze(l, m, n):
    T = ""
    for k in range(m, n + 1, 2):
        T += ligne(l, k)

    return T


def sapin(LenSol, LenTronc, NbSegm):
    i = 9
    Sapin = trapèze(LenSol, 1, LenSol-((NbSegm - 1) * 4))
    for k in range(NbSegm - 1):
        Sapin += trapèze(LenSol, i-2, LenSol-2)
    Sapin += LenTronc * (round((LenSol / 2)) * " " + "***\n")
    Sapin += LenSol * "*"

    return Sapin


def trapèze2(l, m, n):
    T = ""
    for k in range(n, m - 2, -2):
        T += ligne(l, k)

    return T


def étoile():
    E = ""
    E += 16 * " " + trapèze(15, 1, 11) + trapèze2(35, 25, 33) + (23 * "*") + trapèze(35, 25, 33) + trapèze2(15, 1, 11)

    return E

print(étoile())

import os
os.system("pause")