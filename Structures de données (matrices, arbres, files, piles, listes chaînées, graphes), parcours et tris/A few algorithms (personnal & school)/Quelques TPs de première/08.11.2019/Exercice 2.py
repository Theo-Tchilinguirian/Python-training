def Max1(a, b):
    """
    Données: a et b des nombres entiers
    Résultat:  plus grand nombre entre a et b, si a == b, renvoie b.
    """
    if a > b:
        return a
    else:
        return b


def Max2(a, b, c):
    """
    Données: a, b et c des nombres entiers
    Résultat:  plus grand nombre entre a, b et c.
    """
    if Max1(a, b) > c:
        return Max1(a, b)
    else:
        return c


Aff = Max2(1, 3, 2)
print(Aff)

# rep = 1
# while rep != 0:
#   rep = int(input(...))