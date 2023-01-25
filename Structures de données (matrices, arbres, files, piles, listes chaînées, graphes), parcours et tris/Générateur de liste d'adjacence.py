
def MatriceàListeAdj(matrice):
    listAdj = {}
    for sommet in range(len(matrice)):
        listAdj[sommet] = []
        for voisin in range(len(matrice[sommet])):
            listAdj[sommet].append(voisin)
    return listAdj


matrice = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]
print(MatriceàListeAdj(matrice))