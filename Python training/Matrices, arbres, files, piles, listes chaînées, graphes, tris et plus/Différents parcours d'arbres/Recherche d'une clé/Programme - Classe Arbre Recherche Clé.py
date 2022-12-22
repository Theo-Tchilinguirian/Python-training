
class Noeud:

    def __init__(self, valeur = None, parent = None, filsGauche = None, filsDroit = None):

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


    def recherche(self, valeur):
        """
        Renvoie True si la valeur recherchée est dans l'arbre, False sinon.
        """
        if not self.is_empty():  # Si l'arbre n'est pas vide (True si non vide)
            if self.valeur < valeur:
                if self.droite is not None:  # Pas une feuille
                    self.droite.recherche(valeur)  # On rappelle la fonction jusqu'a ce que l'on tombe sur le noeud dont la valeur est celle que l'on recherche
                else:  # On atteint une feuille
                    print("valeur non trouvée dans l'arbre")
                    return False

            elif self.valeur > valeur:
                if self.gauche is not None:
                    self.gauche.recherche(valeur)
                else:
                    print("valeur non trouvée dans l'arbre")
                    return False

            else:  # self.valeur == valeur:
                print("valeur trouvée dans l'arbre")
                return True

        else:  # Arbre vide
            print("L'arbre est vide")
            return False

    def is_empty(self):
        return self.valeur is None  # Si la valeur du noeud est None, alors c'est une feuille.


# Tests:
# On initialise l'arbre
arbre = Noeud()
arbre.insérer(10)
arbre.insérer(15)
arbre.insérer(10)
arbre.insérer(5)
arbre.insérer(9)
arbre.insérer(4)
arbre.insérer(6)
arbre.insérer(11)
# On lance le programme
arbre.recherche(9)  # valeur trouvée dans l'arbre
arbre.recherche(12)  # valeur non trouvée dans l'arbre
