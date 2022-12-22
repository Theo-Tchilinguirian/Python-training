
class Noeud:

    def __init__(self, valeur=None, parent=None, filsGauche=None, filsDroit=None):

        self.valeur = valeur

        self.précédent = parent  # Noeud précédent; None si c'est la racine.
        self.gauche = filsGauche  # Sous-arbre gauche
        self.droite = filsDroit  # Sous-arbre droit

    def insérer(self, valeur):

        if not self.is_empty():  # Si l'arbre n'est pas vide (True si non vide)

            if self.valeur < valeur:
                if self.droite is not None:  # Pas une feuille
                    self.droite.insérer(valeur)  # On rappelle la fonction jusqu'a ce que l'on tombe sur une feuille
                else:  # On atteint une feuille
                    self.droite = Noeud(valeur, parent=self)

            elif self.valeur > valeur:
                if self.gauche is not None:
                    self.gauche.insérer(valeur)
                else:
                    self.gauche = Noeud(valeur, parent=self)

            # Si self.valeur == valeur, on ne fait rien et le programme se termine (le noeud existe déja).
        else:  # Si l'arbre est vide:
            self.valeur = valeur


    def is_empty(self):
        return self.valeur is None  # Si la valeur du noeud est None, alors c'est une feuille.
