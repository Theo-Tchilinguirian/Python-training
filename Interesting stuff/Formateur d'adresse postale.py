#demande une adresse et la print
import os

Numéro = str(input("Numéro: "))
Rue = str(input("Nom de la rue: "))
Ville = str(input("Ville: "))

Adresse = """{}, rue {}
	{}""".format(Numéro, Rue, Ville)

print(Adresse)

os.system("pause")