def ine():
    string = input("string : ")
    mot = input("mot : ")
    listr = list(string)
    for indice_elt in range(len(listr)):
        elt = listr[indice_elt]
        if elt == mot[0]:
            state = True
            for i in range(len(mot)):
                if listr[indice_elt + i] != mot[i]:
                    break
            return indice_elt

print(ine())