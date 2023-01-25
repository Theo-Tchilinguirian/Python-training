print("test enumerate")
ListeLivres = ["Alice au Pays des Merveilles", "Tintin et Grominet", "Astérix et Grobélix", "Alice et Grominet"]
ListeLivres2 = ["Le Pays des Merveilles", "Mémoires d'un Âne", "Tintin au Tibet"]

Réponse = int(input("Choisissez la liste 1 ou la liste 2: "))
if Réponse == 1:
	for i, k in enumerate(ListeLivres):
		print("Le livre {0} se trouve à l'emplacement {1} ".format(k, i + 1))
if Réponse == 2:
	for i, k in enumerate(ListeLivres2):
		print("Le livre {0} se trouve à l'emplacement {1} ".format(k, i + 1))
for j in range(len(ListeLivres)):
	if ListeLivres[j].find("Alice") != -1:
		print(ListeLivres[j])

print("test listes/for")
Liste = [[1, "a"], [3, "d"], [5, "r"]]
for Val1, Val2 in Liste:
	print("la liste {0} contient '{1}'". format(Val1, Val2))
print("test double indice: ", Liste[0][1])
print("test chaines/for")
Chaine = "azerfd"
for ValSuccessive in Chaine:
	print(ValSuccessive)
print("test chaines/for/enumerate")
for IndiceVal, ValSuccessive in enumerate(Chaine):
	print(IndiceVal, ValSuccessive)
print("dernier position lettre =", IndiceVal + 1)
