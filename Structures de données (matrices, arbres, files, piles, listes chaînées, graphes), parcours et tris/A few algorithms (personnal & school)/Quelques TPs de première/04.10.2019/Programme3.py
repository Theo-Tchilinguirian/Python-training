Txt = input("Texte en majuscules: ")
NvTxt = ""

for k in range(0, len(Txt)):
    NvTxt = NvTxt + chr(ord(Txt[k]) + 32)
print(NvTxt)
