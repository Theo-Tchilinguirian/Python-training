
class File:
    def __init__(self):
        self.file = []

    def est_vide(self):
        return self.file == []  # Ou return len(self.file) == 0 ou return not self.file
        # Inverse: if self.file: ...  --> True si la file n'est pas vide

    def enfiler(self, e):
        self.file.append(e)

    def defiler(self):
        if self.file:  # Est True si la file n'est pas vide
            return self.file.pop(0)  # pop le premier élément

    def get_Longueur(self):
        return len(self.file)

    def __str__(self):
        ch = ''
        for x in self.file:
            ch = '|\t' + str(x) + "\t|" + '\n' + ch
        ch = "\nEtat de la file:\n" + ch
        return ch


# Tests

q = File()
q.enfiler(9)
q.enfiler(2)
q.enfiler(5)

print(q)

q.defiler()
q.defiler()

print("La file est-elle vide: {}".format(q.est_vide()))
print(q)
print("Longueur de la file: {}".format(q.get_Longueur()))