class Maillon:
    def __init__(self, donnée, suivant=None):
        self.donnée = donnée
        self.suivant = suivant


class Pile:
    def __init__(self, StalineEstMort=None, taille=0):
        self.sommet = StalineEstMort
        self.taille = taille

    def est_vide(self):
        return self.taille == 0

    def empiler(self, valeur):
        self.sommet = Maillon(valeur, self.sommet)
        self.taille += 1

    def dépiler(self):
        if not self.est_vide():
            renvoi = self.sommet.donnée
            self.sommet = self.sommet.suivant
            self.taille -= 1
            return renvoi


class File :
    def __init__(self, tête=None, taille=0):
        self.tête = tête
        self.taille = taille

    def est_vide(self):
        return self.taille == 0

    def enfiler(self, valeur):
        if self.est_vide():
            self.tête = Maillon(valeur, None)  # Valeur de base de suivant: None
        else:
            maillon = self.tête
            while maillon.suivant is not None:
                maillon = maillon.suivant
            maillon.suivant = Maillon(valeur, None)  # Valeur de base de suivant: None
        self.taille += 1

    def défiler(self):
        if not self.est_vide():
            renvoi = self.tête.donnée
            self.tête = self.tête.suivant
            self.taille -= 1
            return renvoi


class Noeud:  # Ou Arbre
    def __init__(self, valeur, parent=None, gauche=None, droit=None):
        self.parent = parent
        self.donnée = valeur
        self.gauche = gauche
        self.droit = droit

    def insérer(self, valeur):
        if valeur < self.donnée:
            if self.gauche is not None:
                self.gauche.insérer(valeur)
            else:
                self.gauche = Noeud(self, valeur)  # Valeur de base de fils gauche et fils droit: None
        elif valeur > self.donnée:
            if self.droit is not None:
                self.droit.insérer(valeur)
            else:
                self.droit = Noeud(self, valeur)  # Valeur de base de fils gauche et fils droit: None

    def taille(self):
        if self is not None:
            return 1 + self.gauche.taille() + self.droit.taille()
        else:
            return 0

    def hauteur(self):
        if self is not None:
            return 1 + max(self.gauche.hauteur(), self.droit.hauteur())
        else:
            return 0

    def parcoursPréfixe(self):
        if self is not None:
            print(self.donnée)
            self.gauche.parcoursPréfixe()
            self.droit.parcoursPréfixe()

    def parcoursInfixe(self):
        if self is not None:
            self.gauche.parcoursInfixe()
            print(self.donnée)
            self.droit.parcoursInfixe()

    def parcoursSuffixeOuPostfixe(self):
        if self is not None:
            self.gauche.parcoursSuffixeOuPostfixe()
            self.droit.parcoursSuffixeOuPostfixe()
            print(self.donnée)

    def parcoursLargeur(self):
        file = File()
        file.enfiler(self)
        while not file.est_vide():
            noeud = file.défiler()
            print(noeud)
            if noeud.gauche is not None:
                file.enfiler(noeud.gauche)
            if noeud.droit is not None:
                file.enfiler(noeud.droit)