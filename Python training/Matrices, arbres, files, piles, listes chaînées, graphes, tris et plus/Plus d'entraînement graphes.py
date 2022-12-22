
class Graphe:
    def __init__(self, ListAdj):
        self.ListeAdjacence = ListAdj

    def ListSommets(self):
        return list(self.ListeAdjacence)

    def ListArêtes(self):
        arêtes = []
        for sommet in self.ListeAdjacence:
            for voisin in self.ListeAdjacence[sommet]:
                arêtes.append((sommet, voisin))
        return arêtes

    def Add_Sommet(self, sommet):
        if sommet not in self.ListeAdjacence:
            self.ListeAdjacence[sommet] = []

    def Add_Arête(self, tupleArête):
        if tupleArête[0] not in self.ListeAdjacence:
            self.ListeAdjacence[tupleArête[0]] = [tupleArête[1]]
        else:
            self.ListeAdjacence[tupleArête[0]].append(tupleArête[1])


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
                visités.append(voisin)


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
        for voisin in listadj[sommet]:
            arêtes.append((sommet, voisin))
    return arêtes


def GrapheNonOr_Est_Connexe(listadj):
    for sommet in listadj:
        if listadj[sommet] == []:
            return False
    return True


listadj = {'A': ['B', 'C'], 'B': ['C'],'C': ['A', 'B'], 'D': ['A', 'C']}

print(GrapheNonOr_Est_Connexe(listadj))
