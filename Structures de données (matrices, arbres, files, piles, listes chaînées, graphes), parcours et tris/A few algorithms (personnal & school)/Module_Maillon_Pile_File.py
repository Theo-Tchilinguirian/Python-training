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


class File:
    def __init__(self, file = None):
        self.tete = file
        self.taille = 0

    def is_empty(self):
        return self.taille == 0

    def enfiler(self, valeur):
        if self.is_empty():  # Si vide
            self.tete = Maillon(valeur, None)  # Pas besoin de parcourir jusqu'à la fin de la file.
        else:  # Si non vide
            maillon = self.tete
            while maillon.suivant is not None:  # On s'arrette au maillon qui a pour suivant None (donc à l'avant dernier elt de la file)
                maillon = maillon.suivant  # A la sortie de la boucle, maillon.suivant is None
            maillon.suivant = Maillon(valeur, None)  # maillon contient la référence, pointe vers un des objets maillons dans self.tete, ainsi, modifier un attribut de maillon, c'est modifier un attribut d'un maillon de self.tete.
        self.taille += 1

    def defiler(self):
        if not self.is_empty():  # Si non vide
            renvoi = self.tete.donnee
            self.tete = self.tete.suivant
            self.taille -= 1
            return renvoi
        else:  # Si vide alors erreur
            raise AttributeError("File Vide")

    def __str__(self):
        chaine = "En haut: Tête de la file\n"
        maillon = self.tete
        while maillon is not None:  # Ne passe pas quand on atteint le None.
            chaine = chaine + "|\t" + str(maillon.donnee) + "\t|\n"
            maillon = maillon.suivant
        return chaine
