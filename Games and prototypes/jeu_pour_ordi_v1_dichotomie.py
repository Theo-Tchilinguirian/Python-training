# Dans ce jeu, l'utilisateur choisi un nombre pour l'ordinateur.
# L'ordinateur doit trouver le nombre avec les indications de "plus petit" ou "plus grand".


cpt = 1
d = 0
print("Dans ce jeu, vous devez choisir un nombre que l'ordinateur doit deviner en fonction de vos indications.")
f = int(input('Limite max ?: '))
x = int(input("Le nombre, compris dans l'intervalle: "))

tr = False  # 'Trouvé'
while not tr and d <= f:

    print("Ordi: Je vais donc chercher le nombre entre", d, "et", f)
    nb = (d + f)//2  # Nombre choisi par l'ordinateur (votre opposanta, il doit trouver votre nombre)
    # L'ordinateur procède ici par dichotomie pour retrouver x.

    print("- - - Tour numéro", cpt, "- - -")
    cpt += 1

    if nb == x:
        print("Ordi:", nb, "?")
        print("Ordi: J'ai trouvé! Le nombre est", x, "!!")
        tr = True

    elif nb < x:
        print("Ordi:", nb, "?")
        print("Vous: Trop petit!    [--> {}]".format(x))
        d = nb + 1

    else:
        print("Ordi:", nb, "?")
        print("Vous: Trop grand!    [--> {}]".format(x))
        f = nb - 1


# Cet algo a une complexité théorique d'environ log2(n) --> Si on a un intervalle entre 0 et 1024 (2^10) on a 10 tours environs pour finir l'algo.
# C'est la meilleure complexité possible réalisable à ce jour.
