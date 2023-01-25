# Travail à faire

personnes = [
    {'nom':"Bernard", "age": 10},
    {'nom':"Marc", "age": 5},
    {'nom':"Nadia", "age": 7},
    {'nom':"Jean", "age": 12}
]

def rechercheI(liste, nom):
    for i in range(len(liste)):
        for cle, val in liste[i].items():  # liste[i] -> dicos
            if val == nom:
                return "Indice du dictionnaire: {}. {}: {}".format(i, cle, val)


print(rechercheI(personnes, "Nadia"))  # => {nom: "Nadia", age: 7}

def rechercheII(liste, nom):
    for i in range(len(liste)):
        for cle in liste[i]:  # liste[i] -> dicos          # Ou: if liste[i]['nom'] == "Nadia"
            if liste[i][cle] == nom:
                return "Indice du dictionnaire: {}. {}: {}".format(i, cle, liste[i][cle])


print(rechercheII(personnes, "Nadia"))  # => {nom: "Nadia", age: 7}

def rechercheIII(dico, nom):
    return [elt for elt in dico if elt['nom'] == nom]


print(rechercheIII(personnes, "Nadia")[0])
