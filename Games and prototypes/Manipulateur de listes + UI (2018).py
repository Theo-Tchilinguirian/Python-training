#Ce programme permet à l'utilisateur de remplir, changer le contenu d'une liste, d'en afficher un élément
#particulier, demander "que voulez-vous faire?" avec 'help' pour une liste des commandes que l'utilisateur
#peut éxecuter, le programme peut être par exemple remplir une bibliothèque qui correspondrait à cette
#liste, etc... l'on peut RENOMMER la liste (Bibliothèque, par exemple. ou Cours, Liste de Livres à Lire, etc...).

ListeCommandes = ["help", "ajouter", "enlever", "montrer", "renommer"]
ListeUtilisateur = []
NomListe = input("Donnez un nom à votre liste: ")
TestChoix = True
while TestChoix == True:
	try:
		ChoixUtilisateur = input("""Quelle action voulez-vous executer?
			(tapez 'help' pour obtenir la liste des actions disponibles): """)
		if ChoixUtilisateur[0:4] != ListeCommandes[0] and ChoixUtilisateur[0:7] != ListeCommandes[1] and ChoixUtilisateur[0:7] != ListeCommandes[2] and ChoixUtilisateur[0:7] != ListeCommandes[3] and ChoixUtilisateur[0:8] != ListeCommandes[4]:
			print("Le choix est invalide")
			continue
		if ChoixUtilisateur == "help":
			print("""Les commandes éxécutables sont:
				1.'help'
				2.'ajouter [élément]'
				3.'enlever [élément]'(supprimme le premier élément correspondant dans la liste)
				4.'montrer [liste]'
				5.'renommer [liste]'
				[élément] est une chaîne ou un réel
				[liste] est le nom de la liste""")
			continue
		if ChoixUtilisateur[0:7] == "ajouter":
			try:
				ListeUtilisateur.append(float(ChoixUtilisateur[8:]))
				print("Commande éxécutée")
				continue
			except ValueError:
				ListeUtilisateur.append(ChoixUtilisateur[8:])
				print("Commande éxécutée")
		if ChoixUtilisateur[0:7] == "enlever":
			try:
				ListeUtilisateur.remove(ChoixUtilisateur[8:])
				print("Commande éxécutée")
				continue
			except:
				print("Le choix est invalide, recommencez")
				continue
		if ChoixUtilisateur == "montrer " + NomListe:
			print("Liste {1} contient {0}".format(ListeUtilisateur, NomListe))
			print("Commande éxécutée")
			continue
		if ChoixUtilisateur == "renommer " + NomListe:
			NomListe = input("renommez votre liste: ")
			print("Commande éxécutée")
			continue
	except:
		print("Le choix est invalide, recommencez")
		continue
