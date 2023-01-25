from math import *

print("coordonnés du premier point: ")
x1 = int(input("Abscisse: "))
y1 = int(input("Ordonnée: "))

print("coordonnés du deuxième point: ")
x2 = int(input("Abscisse: "))
y2 = int(input("Ordonnée: "))

Distance = sqrt((x2-x1)**2+(y2-y1)**2)
print("La distance entre les deux points vaut: ",Distance)
