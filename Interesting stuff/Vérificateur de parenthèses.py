class Maillon:
    def __init__(self, donnee = None, suivant = None):
        self.donnee = donnee
        self.suivant = suivant


class Pile:
    def __init__(self, pile = None):
        self.sommet = pile
        self.taille = 0

    def is_empty(self):
        return self.taille == 0

    def empiler(self, valeur):
        self.sommet = Maillon(valeur, self.sommet)
        self.taille += 1

    def depiler(self):
        if not self.is_empty():
            renvoi = self.sommet.donnee
            self.sommet = self.sommet.suivant
            self.taille -= 1
            return renvoi
        else:
            raise AttributeError("Pile Vide")

    def __str__(self):
        chaine = "En haut: Sommet de la pile\n"
        maillon = self.sommet
        while maillon is not None:  # Ne passe pas quand on atteint le None.
            chaine = chaine + "|\t" + str(maillon.donnee) + "\t|\n"
            maillon = maillon.suivant
        return chaine



def VerifieParenthèses(expr):
    p = Pile()
    for car in expr:
        if car == '(':
            p.empiler(car)
        elif car == ')':
            if p.is_empty():
                return False
            else:
                p.depiler()
    if p.is_empty():
        return True
    return False


# Tests

print(20*'-')
print(VerifieParenthèses("((a+b)*c-3("))
print(VerifieParenthèses("((a+b)*c-3)"))
print(20*'-')
