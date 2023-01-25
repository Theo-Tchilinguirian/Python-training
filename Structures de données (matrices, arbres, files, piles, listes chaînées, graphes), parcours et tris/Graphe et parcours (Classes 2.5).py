
class graphe:
    def __init__(self):
        self.listadj = {}
        self.matriceadj = [[O for k in range(len(self.listadj))] for k in range(len(self.listadj))]


    def ListSommets(self):
        return list(self.listadj)


def ParcoursProfondeur(listadj, sommet, visités = []):
    visités.append(sommet)
    print(sommet)
    for voisin in listadj[sommet]:
        if voisin not in visités:
            ParcoursProfondeur(listadj, voisin, visités)


def ParcoursLargeur(listadj, sommet):
    file = [sommet]
    visités = [sommet]
    while not file == []:
        U = file.pop(0)
        print(U)
        for voisin in listadj[U]:
            if voisin not in visités:
                file.append(voisin)
                visités.append(U)


def ExistChemin(listadj, U, V):
    file = [U]
    visités = []
    while not file == []:
        sommet = file.pop(0)
        visités.append(sommet)
        for voisin in listadj[sommet]:
            if voisin == V:
                return True
            elif voisin not in visités:
                file.append(voisin)
    return False


def ExistCycle(listadj):
    for sommet in listadj:
        if ExistChemin(listadj, sommet, sommet) == True:
            return True
    return False


def ListArêtes(listadj):
    arêtes = []
    for sommet in listadj:
        for voisin in listadj[sommet]
            arêtes.append(sommet, voisin)
    return arêtes
