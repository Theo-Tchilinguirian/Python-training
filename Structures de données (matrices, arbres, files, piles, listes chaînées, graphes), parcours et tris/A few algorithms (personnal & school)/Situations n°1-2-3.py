from turtle import *

print("On souhaite dessiner un carré de 50 unité de coté")
for i in range(4):
	forward(50)
	right(90)

print("On souhaite parcourir tous les éléments d'une chaine de caracteres et les afficher les uns apres les autres")
Chaine = input("Chaine: ")
for i, k in enumerate(Chaine):
	print(i + 1, k)


print("On souhaite calculer la moyenne de plusieurs notes d'élèves saisies les unes après les autres")
note = 0
somme = 0
NombreNotes = int(input("Nombre de notes: "))
for i in range(NombreNotes):
	note = int(input("Ajouter une note: "))
	somme += note
print("moyenne des notes:", somme / NombreNotes)