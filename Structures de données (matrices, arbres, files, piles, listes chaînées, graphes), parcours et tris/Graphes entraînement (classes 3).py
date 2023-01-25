
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



class Graphe:
    def __init__(self, graphe={}):
        self.listadj = graphe

    def lister_Sommets(self):
        return list(self.listadj)

    def lister_Arêtes(self):
        arêtes = []
        for sommet in self.listadj:
            for voisin in self.listadj[sommet]:
                arêtes.append((sommet, voisin))
        return arêtes

    def ajouter_Sommet(self, sommet):
        if sommet not in self.listadj:
            self.listadj[sommet] = []

    def ajouter_Arête(self, arête):
        if arête[0] not in self.listadj:
            self.listadj[arête[0]] = [arête[1]]
        else:
            self.listadj[arête[0]].append(arête[1])


def parcours_Profondeur(listadj, sommet, visités=[]):
    visités.append(sommet)
    print(sommet)
    for voisin in listadj[sommet]:
        if voisin not in visités:
            parcours_Profondeur(listadj, voisin, visités)


def parcours_Largeur(listadj, sommet):
    file = [sommet]
    visités = [sommet]
    while not file == []:
        u = file.pop(0)
        print(u)
        for voisin in listadj[u]:
            if voisin not in visités:
                visités.append(voisin)
                file.append(voisin)


def exist_Chemin_uv(listadj, u, v):
    file = [u]
    visités = []
    while not file == []:
        sommet = file.pop(0)
        visités.append(sommet)
        for voisin in listadj[sommet]:
            if voisin == v:
                return True
            elif voisin not in visités:
                file.append(voisin)
    return False


def exist_Cycle(listadj):
    for sommet in listadj:
        if exist_Chemin_uv(listadj, sommet, sommet) == True:
            return True
    return False


def lister_Arêtes(listadj):
    arêtes = []
    for sommet in listadj:
        for voisin in listadj[sommet]:
            arêtes.append((sommet, voisin))
    return arêtes



""" Révisions inopinées de SQL
create database [nom];
Schéma relationel : [nom relation]([attributs] : [domaines])  # souligner clé primaire, # devant clés étrangères
create table [nom]([attributs] [domaines]);
create table [nom]([attributs] [domaines], primary key([clé primaire]));
create table [nom]([attributs] [domaines], primary key([clé prim]), foreign key([clé étr]) references [table]([clé prim de cette autre table]));
Une clé primaire est un attribut dont la valeur permet d identifier de manière unique un t-uplet de la relation.
Autrement dit, si un attribut est considéré comme clé primaire, on ne doit pas trouver dans toute la relation 2 fois la même valeur pour cet attribut.
insert into [table] values ([attributs]);
select * from [table]
select [attributs] from [table];
select [attributs] from [table] where [condition];
select distinct [attributs] from [table];
select [table].[attributs] from [table1 ou 2] inner join [table2 ou 1] on [table 1].[clé étrangère T1] = [table2].[clé prim T2];
Si on join from tab1 inner join tab2 on..., alors on greffe les tuples de la tab2 sur la tab1.
select [table].[attributs] from [table1 ou 2] inner join [table2 ou 1] on [table 1].[clé étrangère T1] = [table2].[clé prim T2] where [condition];
la condition permet de joindre que les tuples qui respectent cette condition
update [table] set [attributs] where [condition];
delete from [table] where [condition]
delete supprime les tuples qui respectent la condition
"""
