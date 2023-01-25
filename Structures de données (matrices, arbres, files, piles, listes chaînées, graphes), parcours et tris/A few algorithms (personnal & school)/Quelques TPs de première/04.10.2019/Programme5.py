Texte = input("Texte: ")
NvTexte = ""
for k in range(0, len(Texte)):
    if Texte[k] != " ":
        NvTexte = NvTexte + Texte[k]
    if Texte [k] == " ":
        NvTexte = NvTexte + "-"
        
print(NvTexte)
