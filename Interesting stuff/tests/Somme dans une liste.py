#Somme
NombreTours = int(input("choisissez un nombre de tours: "))
NombreChoisi = int(input("Choisissez le min de la liste: "))
SommeTotale = 0
for k in range(NombreTours + 1):
	print("Nombre ", k	 + 1, "est: ", NombreChoisi)
	NombreChoisi += 1
	SommeTotale += NombreChoisi
print("Somme totale est:", SommeTotale)
