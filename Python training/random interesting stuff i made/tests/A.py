
# Tests classes

class humain:

    nb_hum = 0
    nb_fun = 0

    def __init__(self, taille, nom):
        self.prenom = 'Humain'
        self.nom = nom
        self.taille = taille

        humain.nb_hum += 1

    def set_taille(self, nvtaille):
        self.taille = nvtaille

    def set_nb_fun(cls, nv_nb_fun):
        cls.nb_fun = nv_nb_fun
        
    set_nb_fun = classmethod(set_nb_fun)
    

class homme(humain):
    nb_hom = 0

    def __init__(self, taille, nom):
        self.prenom = 'Homme'
        self.taille = taille
        self.genre = 'Mâle'

        humain.nb_hum += 1
