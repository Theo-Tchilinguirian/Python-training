# Suite de conway. Faire boucle principale pr répéter. Faire changement de base (plus grande ou plus petite)
# Faire dessin courbe (nombres centrés premier en haut dernier en bas)

"""
Pb décomposé en listes (une liste est un élément de la suite de Conway)
Listes contiennent des sections de chiffres égaux qui sont parcourues et comptées
Le code suivant calcule l'élément suivant l, nommé l2.
"""

# nexta : deux boucles imbriquées, partiellement exécutées
# next : une boucle while avec une condition interne qui modifie l'état en cours
# de route, la boucle parcourant entièrement la liste.

def nexta(l):  # l supposée non vide.

        l2 = []  # Liste de l'élément suivant de la suite
        
        i = 0  # indice mobile qui va parcourir de l'indice du chiffre jusqu'à l'indice du prochain chiffre différent

        while i <= len(l)-1:  # Parcours sous-liste de chiffres
                chif_cur = l[i]  # Chiffre égal aux autres courant
                qte = 0  # Nombre de chiffres égaux.
                while i <= len(l)-1 and l[i] == chif_cur:
                        qte += 1
                        i+=1
                l2 += [qte, chif_cur]
        # l[i] est désormais le chiffre suivant

        return l2

def next(l):  # l supposée non vide.

        l2 = []  # Liste de l'élément suivant de la suite
        
        i = 0  # indice mobile qui va parcourir de l'indice du chiffre jusqu'à l'indice du prochain chiffre différent

        chif_cur = l[i]  # Chiffre égal aux autres courant
        qte = 0  # Nombre de chiffres égaux.
        while i <= len(l)-1:  # Parcours sous-liste de chiffres
                qte += 1
                i+=1
                if i <= len(l)-1 and l[i] != chif_cur:
                        l2 += [qte, chif_cur]
                        chif_cur = l[i]
                        qte = 0
        l2 += [qte, chif_cur]

        # l[i] est désormais le chiffre suivant

        return l2


# tests

l = [1]  # Liste de l'élément courant de la suite
for i in range(18):
        string = ""
        for x in l:
                string += str(x)
        print(str(i+1)+ (" " if i+1 > 9 else "  ") + string.center(200))
        l = next(l)

print()

l = [1]  # Liste de l'élément courant de la suite

for i in range(18):
        string = ""
        for x in l:
                string += str(x)
        print(str(i+1)+ (" " if i+1 > 9 else "  ") + string)
        l = next(l)


# TODO : analyse complexité temporelle (module time), recherche de la présence d'éléments précédents dans les suivants, recherche de constantes, de redondance... de propriétés.