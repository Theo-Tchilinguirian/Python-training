import random
import os
from builtins import abs
import tkinter as tk

"""
	Jeu de hasard
"""

print("Regles du jeu: un nombre sera choisi au hasard, et vous devrez deviner lequel c'est! Votre nombre d'essais est compté!")

k = True
while k == True:
	try:
		IntervalleCible = input("Choisissez un nombre positif dans lequel sera contenu la cible (par exemple 1000: la cible sera entre 0 et 1000): ")
		IntervalleCible = int(IntervalleCible)
	except:
		print("Ce n'est pas un nombre")
		continue


	if  IntervalleCible < 100:
		print("L'intervalle est trop petit (doit être plus grand ou égal à 100")
		continue
	else:
		break

NombreDéfini = random.randrange(0, IntervalleCible)
CompteurEssais = 0
def NombreChoisiParUtilisateurTRY():
	global CompteurEssais #ici on rend global à toutes les lignes (meme dans les def) la variable CompteurEssais , LE GLOBAL DOIT ETRE DANS UNE DEF OU UNE LAMBDA (mieux au début pour etre global sur toutes les lignes de la def)
	TRY = True
	while TRY == True:
		try:
			NombreChoisiParUtilisateur = input("Choisir un nombre à parier: ")
			NombreChoisiParUtilisateur = int(NombreChoisiParUtilisateur)
		except:
			print("Ce n'est pas un nombre")
			continue
		if NombreChoisiParUtilisateur > IntervalleCible:
			print("Le nombre choisi est trop grand")
			continue
		if NombreChoisiParUtilisateur < 0:
			print("Le nombre choisi est trop petit")
			continue
		if NombreChoisiParUtilisateur < IntervalleCible:
			break
		if NombreChoisiParUtilisateur > 0:
			break
	CompteurEssais += 1 #Le return doit être placé 1 indentation à droite le DEF (C'est mieux pour return toutes les données voulues sans soucis)
	return NombreChoisiParUtilisateur, CompteurEssais #ici return permet d'utiliser une ou plusieurs(list, tuple ou dictionnary) variable de la fonction définie hors de la définition de la fonction

Jouer = True
while Jouer == True:
	NombreChoisiParUtilisateur, NombreEssais = NombreChoisiParUtilisateurTRY()	#Un nom de variable quelquonque (marche avec le même que le nom dans la fonction) permet de récuperer la variable retournée précedement
	DistanceIntervalle = abs(NombreChoisiParUtilisateur - NombreDéfini)			#ici il y a plusieurs variables dans le return, donc on fait une affectation multiple!
	if DistanceIntervalle <= 10:
		print("Vous n'êtes pas très loin!")
		
	if DistanceIntervalle > 10 and DistanceIntervalle <= 50:
		print("Vous n'êtes pas loin, mais encore...")
		
	if DistanceIntervalle >= 50 and DistanceIntervalle < 100:
		print("Vous êtes à une certaine distance de la cible...")
		
	if DistanceIntervalle >= 100:
		print("Vous êtes distant de la cible...")
		#PEUT ETRE REMPLACE PAR CONTINUE
	if NombreChoisiParUtilisateur == NombreDéfini:
		print("Bravo! C'est gagné!")
		print("Votre nombre d'essais est:", NombreEssais)
		break
os.system("pause")