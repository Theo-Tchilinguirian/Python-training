
MsgError1 = "Valeur saisie invalide"
ValASCII = 64
JoueurActif = 1
SepCSV = ';'

NombreDeLignes = 18
tup_TitreLignes = ['joueurs        ', 'Total de 1     ', 'Total de 2     ', 'Total de 3     ', 'Total de 4     ', 'Total de 5     ', 'Total de 6     ',
                   'Total          ', 'Prime          ', 'Total1         ', 'Brelan         ', 'Carré          ', 'Full           ', 'Petite Suite   ', 'Grande Suite   ', 'Yams           ',
                   'Chance         ', 'Total2         ', 'Total          ']

dico_Scores = {'Prime':35, 'Full':25, 'Petite Suite':30, 'Grande Suite':40, 'Yams':50}
dico_Des_Valeurs = {1:-1, 2:-1, 3:-1, 4:-1, 5:-1}
dico_Des_Relance = {1:False, 2:False, 3:False, 4:False, 5:False}

# Points
Score_Yams = 50
Score_GrdSuite = 40
Score_PetSuite = 30
Score_Full = 25
Score_Prime = 35

# Types de Brelans différents possibles
Brelan_absent = -1  # Pas de brelan
Brelan_debut = 1  # Les 3 valeurs du brelan (triées) sont au début
Brelan_milieu = 2  # Au milieu
Brelan_fin = 3  # Ou à la fin

# Types de Carrés différents possibles
Carre_absent = -1  # Pas de carré
Carre_debut = 1  # Les 4 valeurs (triées) du carré sont au début
Carre_fin = 2  # Ou à la fin
