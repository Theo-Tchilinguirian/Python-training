Chaine = input("Chaine: ")
NouvelleChaine = ""
for k in range(0, len(Chaine)):
    NouvelleChaine += Chaine[-(k+1)]
print(NouvelleChaine)
