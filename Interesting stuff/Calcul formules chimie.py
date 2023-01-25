#Calcul de formules
import os

def CalculFormules():
	NombreAvogadro = 6.02e+23
	TestFormuleChoisie = True
	while TestFormuleChoisie == True:
		try:
			FormuleChoisie = int(input("""Choisissez le numéro de la formule que vous voulez choisir
			1. Nombre de molécules
			2. Quantité de matière
			3. Concentration molaire
			4. Concentration massique
			Numéro de la formule: """))
			if FormuleChoisie > 4 or FormuleChoisie < 1:
				print("Le choix n'est pas valide")
				continue
			break
		except:
			print("Le choix n'est pas valide, recommencez")
			continue

	print("""Vous avez choisi la formule n°""", FormuleChoisie)
	while TestFormuleChoisie == True:
		if FormuleChoisie == 1:
			try:
				QuantitéMatière = float(input("""Quelle est la quantité de matière dont vous disposez?
					Quantité de matière en mole: """))
				print("Le nombre de molécules N dont vous disposez est N = ", QuantitéMatière * NombreAvogadro, "molécules")
				break
			except:
				print("La quantitée donnée n'est pas un nombre")
				continue

		if FormuleChoisie == 2:
			try:
				Masse = float(input("""Quelle est la masse dont vous disposez?
					Masse en grammes: """))
				MasseMolaire = float(input("""Quelle est la masse molaire dont vous disposez?
					Masse molaire en g/mol: """))
				print("La quantité de matière n dont vous disposez est n = ", Masse / MasseMolaire, "moles")
				break
			except:
				print("La quantitée donnée n'est pas un nombre")
				continue

		if FormuleChoisie == 3:
			try:
				QuantitéMatière = float(input("""Quelle est la quantité de matière dont vous disposez?
					Quantité de matière en mole: """))
				Volume = float(input("""Quelle est le volume dont vous disposez?
					Volume en litres: """))
				print("La concentration molaire C dont vous disposez est C = ", QuantitéMatière / Volume, "mol/L")
				break
			except:
				print("La quantitée donnée n'est pas un nombre")
				continue
		
		if FormuleChoisie == 4:
			try:
				Masse = float(input("""Quelle est la masse dont vous disposez?
					Masse en grammes: """))
				Volume = float(input("""Quelle est le volume dont vous disposez?
					Volume en litres: """))
				print("La concentration massique dont vous disposez est Cm = ", Masse / Volume, "g/L")
				break
			except:
				print("La quantitée donnée n'est pas un nombre")
				continue
	return

CalculFormules()
TestRecommencer = True
while TestRecommencer == True:
	Recommencer = input("voulez-vous recommencer? Oui/Non: ")
	if Recommencer == "Oui" or Recommencer == "oui":
		CalculFormules()
	else:
		if Recommencer == "Non" or Recommencer == "non":
			break
		else:
			print("Vous n'avez répondu ni par oui, ni par non.")
			continue

os.system("pause")