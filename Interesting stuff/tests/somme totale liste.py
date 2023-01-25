#SOMME TOTALE
n = int(input("nb tours"))
a = int(input("nb de départ"))
s = 0
for k in range(n):
	a += 1
	s += a
print("somme totale =", s)