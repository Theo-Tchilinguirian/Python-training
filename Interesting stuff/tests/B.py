class gens:
    nb_de_gens = 0
    _val_a_mod = 'f'

    def __init__(self, Guernica):
        self.Guernica = Guernica
        gens.nb_de_gens += 1

    def _get_val_a_mod(cls):
        print("valamod =", cls._val_a_mod)


    val_a_mod = property(_get_val_a_mod)

    _get_val_a_mod = classmethod(_get_val_a_mod)
    
