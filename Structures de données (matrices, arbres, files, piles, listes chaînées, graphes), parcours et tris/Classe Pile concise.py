
class Pile:
    def __init__(self):
        self.pile = []

    def est_vide(self):
        return self.pile == []  # Ou return len(self.pile) == 0

    def empiler(self, e):
        self.pile.append(e)

    def depiler(self):
        if self.pile:  # Est True si la pile n'est pas vide
            return self.pile.pop()  # pop le dernier élément

    def sommet(self):
        if self.pile:
            return self.pile[-1]

    def __str__(self):
        ch = ''
        for x in self.pile:
            ch = '|\t' + str(x) + "\t|" + '\n' + ch
        ch = "\nEtat de la pile:\n" + ch
        # return automatiquement
