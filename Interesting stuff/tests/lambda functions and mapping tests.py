
f = lambda x, y, cond : x if cond else y  # Programmation procédurale

def ff(x, y, cond):  # Programmation fonctionelle
    if cond:
        return x
    else :
        return y

print(f(1, 2, 1<2))
print(f(1, 2, False))
print(ff(1, 2, 1<2))
print(ff(1, 2, False))


def ajout(X, Y):
    for e in Y:
        X.append(e)
    return X

print(ajout([1], [2]))


def foncAux(Cond, X, Y):
    if Cond:
        return ajout(X, Y)
    else :
        None


print(foncAux(True, [1], [2]))


def fonc(a, b):
    return list(filter(a, b))

print(fonc(lambda x: x%2==0, [2, 5, 6, 7, 22, 23]))

#  filter fait passer les elts de la liste en arguments de la lambda. Renvoie un objet filter que l'on listifise.


def funk(l):
    return [elt**3 for elt in l]
print(funk([4, 3, 5, 2]))

#   map == filter d'un coup (fait tt les elts de la liste d'un coup)

