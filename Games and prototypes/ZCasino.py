# TP cours OpenClassrooms

import os
from math import ceil
from random import randrange     #on importe les modules nécéssaires

continuer = True
nb_misé = -1
argent_misé = -1
argent = 1000
print("vous êtes assis à la table du casino avec", argent,"$")
while continuer == True:              #on créer une boucle qui arrete le jeu quand elle est sur "False" -> voir fin du programme
	nb_misé = -1
	argent_misé = -1
	while nb_misé < 0 or nb_misé > argent:
		nb_misé = input("Choisissez une somme à miser: ")
		try:                                                         #cette boucle permet de tester si le nb choisi est un nombre ou si il est trop grand 
			nb_misé = int(nb_misé)
		except ValueError:
			print("Ce n'est pas un nombre")
			nb_misé = -1
			continue
		if nb_misé < 0:
			print("Le nombre est négatif")
		if nb_misé > argent:
			print("Vous n'avez pas assez d'argent, il vous reste", argent, "$")
			break

	while argent_misé <= 0 or argent_misé > 49:
		argent_misé = input("Choisissez un nombre entre 0 et 49: ")
		try:                                                              #cette boucle permet de tester si le nb choisi est un nombre ou si il est entre 0 et 49 
			argent_misé = int(argent_misé)
		except ValueError:
			print("Ce n'est pas un nombre")
			argent_misé = -1
			continue
		if argent_misé < 0:
			print("Le nombre est négatif")
		if argent_misé > 49:
			print("Le nombre est trop grand")
			break

	num_aléatoire = randrange(50)
	print("La roue tourne, la boule tombe sur le numéro:", num_aléatoire)

	if num_aléatoire == nb_misé:
		argent += nb_misé * 3
		print("Vous gagnez 3 fois le nombre misé! Vous avez maintenant:", argent, "$")
	elif num_aléatoire % 2 == nb_misé % 2:
		nb_misé = ceil(nb_misé * 0.5)                                                                #permet de déduire l'argent du compte du joueur
		argent += nb_misé / 2
		print("Vous gagnez la moitié du nombre misé")
	else:
		argent -= nb_misé
		print("Vous perdez votre mise!")

	if argent <= 0:
		print("Vous êtes ruiné! Fin de la partie.")
		continuer = False
	else:
		print("Il vous reste", argent)

	quitter = input("Voulez-vous quitter le casino? (o/n): ")
	if quitter == "o" or quitter == "O":
		print("Vous quittez le casino avec votre argent")
		continuer = False

os.system("pause")                        #met en pause le programme
