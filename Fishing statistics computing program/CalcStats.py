
from functools import reduce


def time_convert(stri):
    liste = stri.split(":")
    return (int(liste[0]) * 60) + int(liste[1])

def time_deconvert(inte):
    inte = round(inte)
    return str(inte // 60) + ':' + str(inte % 60)

def recup_var_nom_esp(stri):
    l = stri.split(' ')
    return l[0], l[1]


with open("Temps Seconde Fish SoT.csv", "r") as fichier:
    champs = fichier.readline()
    tab = [ligne.rstrip(',,\n').split(',') for ligne in fichier]

for i in range(len(tab)):
    del tab[i][1]

print(tab)


dict_taille_temps = {'Taille': [], 'Temps': []}
liste_temps_regul_sans_pondie = []
liste_temps_troph_sans_pondie = []

for i in range(len(tab)):
    var, esp = recup_var_nom_esp(tab[i][0])
    if esp != 'Pondie':
        dict_taille_temps['Taille'].append(tab[i][1])
        dict_taille_temps['Temps'].append(tab[i][2])

        if tab[i][1] == 'Regular':
            liste_temps_regul_sans_pondie.append(time_convert(tab[i][2]))
        elif tab[i][1] == 'Trophy':
            liste_temps_troph_sans_pondie.append(time_convert(tab[i][2]))

liste_temps_regul = []
liste_temps_troph = []
for liste in tab:
    if liste[1] == 'Regular':
        liste_temps_regul.append(time_convert(liste[2]))
    elif liste[1] == 'Trophy':
        liste_temps_troph.append(time_convert(liste[2]))
nb_regul = len(liste_temps_regul)
nb_troph = len(liste_temps_troph)

print('---')
print(dict_taille_temps)
print(nb_regul, liste_temps_regul_sans_pondie)
print(nb_troph, liste_temps_troph_sans_pondie)

print('------------------------------------------------------------------------------------------------------------------------------------------')
print("@@@@@@@@@@@@@@@@@@@@@@@@moyennes de temps de pêche (SAUF PONDIE) et proba trophée")
moy_temps_regul = 0

for elt in liste_temps_regul_sans_pondie:
    moy_temps_regul += elt
moy_temps_regul /= nb_regul

print("moyenne temps pêcher poisson normal :", time_deconvert(moy_temps_regul))


moy_temps_troph = 0

for elt in liste_temps_troph_sans_pondie:
    moy_temps_troph += elt
moy_temps_troph /= nb_troph

print("moyenne temps pêcher poisson trophée :", time_deconvert(moy_temps_troph))


prob_troph = (nb_troph * 100) / (nb_regul + nb_troph)

print("probabilité d'obtenir un poisson trophée :", prob_troph, "pourcents")
print('------------------------------------------------------------------------------------------------------------------------------------------')

print(tab)
dict_Splashtails = {'Ruby': 0, 'Sunny': 0, 'Indigo': 0, 'Umber': 0, 'Seafoam': 0}
dict_Pondies = {'Charcoal': 0, 'Orchid': 0, 'Bronze': 0, 'Bright': 0, 'Moonsky': 0}
dict_Islehoppers = {'Stone': 0, 'Moss': 0, 'Honey': 0, 'Raven': 0, 'Amethyst': 0}
dict_Ancientscales = {'Almond': 0, 'Sapphire': 0, 'Smoke': 0, 'Bone': 0, 'Starshine': 0}
dict_Plentifins = {'Olive': 0, 'Amber': 0, 'Cloudy': 0, 'Bonedust': 0, 'Watery': 0}
dict_Wildsplashes = {'Russet': 0, 'Sandy': 0, 'Ocean': 0, 'Muddy': 0, 'Coral': 0}
dict_Devilfish = {'Ashen': 0, 'Seashell': 0, 'Lava': 0, 'Forsaken': 0, 'Firelight': 0}
dict_Battlegills = {'Jade': 0, 'Sky': 0, 'Rum': 0, 'Sand': 0, 'Bittersweet': 0}
dict_Wreckers = {'Rose': 0, 'Sun': 0, 'Blackloud': 0, 'Snow': 0, 'Moon': 0}
dict_Stormfish = {'Ancient': 0, 'Shores': 0, 'Wild': 0, 'Shadow': 0, 'Twilight': 0}

for liste in tab:
    var, esp = recup_var_nom_esp(liste[0])
    if esp == 'Splashtail':
        dict_Splashtails[var] += 1
    elif esp == 'Pondie':
        dict_Pondies[var] += 1
    elif esp == 'Islehopper':
        dict_Islehoppers[var] += 1
    elif esp == 'Ancientscale':
        dict_Ancientscales[var] += 1
    elif esp == 'Plentifin':
        dict_Plentifins[var] += 1
    elif esp == 'Wildsplash':
        dict_Wildsplashes[var] += 1
    elif esp == 'Devilfish':
        dict_Devilfish[var] += 1
    elif esp == 'Battlegill':
        dict_Battlegills[var] += 1
    elif esp == 'Wrecker':
        dict_Wreckers[var] += 1
    elif esp == 'Stormfish':
        dict_Stormfish[var] += 1

print(dict_Splashtails, '\n',
dict_Pondies, '\n',
dict_Islehoppers, '\n',
dict_Ancientscales, '\n',
dict_Plentifins, '\n',
dict_Wildsplashes, '\n',
dict_Devilfish, '\n',
dict_Battlegills, '\n',
dict_Wreckers, '\n',
dict_Stormfish, '\n')

f = lambda a, x: a + x

som_Splashtails = reduce(f, dict_Splashtails.values()) - dict_Splashtails['Seafoam']
print(som_Splashtails)
som_Pondies = reduce(f, dict_Pondies.values()) - dict_Pondies['Moonsky']
som_Islehoppers = reduce(f, dict_Islehoppers.values()) - dict_Islehoppers['Amethyst']
som_Ancientscales = reduce(f, dict_Ancientscales.values()) - dict_Ancientscales['Starshine']
som_Plentifins = reduce(f, dict_Plentifins.values()) - dict_Plentifins['Watery']
som_Wildsplashes = reduce(f, dict_Wildsplashes.values()) - dict_Wildsplashes['Coral']
som_Devilfish = reduce(f, dict_Devilfish.values()) - dict_Devilfish['Firelight']
som_Battlegills = reduce(f, dict_Battlegills.values()) - dict_Battlegills['Bittersweet']
som_Wreckers = reduce(f, dict_Wreckers.values()) - dict_Wreckers['Moon']
som_Stormfish = reduce(f, dict_Stormfish.values()) - dict_Stormfish['Twilight']

print(tab)
dict_prob_Splashtails = {'Ruby': 0, 'Sunny': 0, 'Indigo': 0, 'Umber': 0, 'Seafoam': 0}
dict_prob_Pondies = {'Charcoal': 0, 'Orchid': 0, 'Bronze': 0, 'Bright': 0, 'Moonsky': 0}
dict_prob_Islehoppers = {'Stone': 0, 'Moss': 0, 'Honey': 0, 'Raven': 0, 'Amethyst': 0}
dict_prob_Ancientscales = {'Almond': 0, 'Sapphire': 0, 'Smoke': 0, 'Bone': 0, 'Starshine': 0}
dict_prob_Plentifins = {'Olive': 0, 'Amber': 0, 'Cloudy': 0, 'Bonedust': 0, 'Watery': 0}
dict_prob_Wildsplashes = {'Russet': 0, 'Sandy': 0, 'Ocean': 0, 'Muddy': 0, 'Coral': 0}
dict_prob_Devilfish = {'Ashen': 0, 'Seashell': 0, 'Lava': 0, 'Forsaken': 0, 'Firelight': 0}
dict_prob_Battlegills = {'Jade': 0, 'Sky': 0, 'Rum': 0, 'Sand': 0, 'Bittersweet': 0}
dict_prob_Wreckers = {'Rose': 0, 'Sun': 0, 'Blackloud': 0, 'Snow': 0, 'Moon': 0}
dict_prob_Stormfish = {'Ancient': 0, 'Shores': 0, 'Wild': 0, 'Shadow': 0, 'Twilight': 0}

try :
    for var in dict_Splashtails.keys():
        dict_prob_Splashtails[var] += (dict_Splashtails[var] * 100) / som_Splashtails
except:
    pass
try :
    for var in dict_Pondies.keys():
        dict_prob_Pondies[var] += (dict_Pondies[var] * 100) / som_Pondies
except:
    pass
try :
    for var in dict_Islehoppers.keys():
        dict_prob_Islehoppers[var] += (dict_Islehoppers[var] * 100) / som_Islehoppers
except:
    pass
try :
    for var in dict_Ancientscales.keys():
        dict_prob_Ancientscales[var] += (dict_Ancientscales[var] * 100) / som_Ancientscales
except:
    pass
try :
    for var in dict_Plentifins.keys():
        dict_prob_Plentifins[var] += (dict_Plentifins[var] * 100) / som_Plentifins
except:
    pass
try :
    for var in dict_Wildsplashes.keys():
        dict_prob_Wildsplashes[var] += (dict_Wildsplashes[var] * 100) / som_Wildsplashes
except:
    pass
try :
    for var in dict_Devilfish.keys():
        dict_prob_Devilfish[var] += (dict_Devilfish[var] * 100) / som_Devilfish
except:
    pass
try :
    for var in dict_Battlegills.keys():
        dict_prob_Battlegills[var] += (dict_Battlegills[var] * 100) / som_Battlegills
except:
    pass
try :
    for var in dict_Wreckers.keys():
        dict_prob_Wreckers[var] += (dict_Wreckers[var] * 100) / som_Wreckers
except:
    pass
try :
    for var in dict_Stormfish.keys():
        dict_prob_Stormfish[var] += (dict_Stormfish[var] * 100) / som_Stormfish
except:
    pass

dict_prob_Splashtails['Seafoam'] = None
dict_prob_Pondies['Moonsky'] = None
dict_prob_Islehoppers['Amethyst'] = None
dict_prob_Ancientscales['Starshine'] = None
dict_prob_Plentifins['Watery'] = None
dict_prob_Wildsplashes['Coral'] = None
dict_prob_Devilfish['Firelight'] = None
dict_prob_Battlegills['Bittersweet'] = None
dict_prob_Wreckers['Moon'] = None
dict_prob_Stormfish['Twilight'] = None
print('------------------------------------------------------------------------------------------------------------------------------------------')
print("@@@@@@@@@@@@@@@@@@@@@@@@probas par espèce et variété SAUF NUIT")
print(dict_prob_Splashtails, "---", dict_prob_Splashtails['Ruby'] + dict_prob_Splashtails['Sunny'] + dict_prob_Splashtails['Indigo'] + dict_prob_Splashtails['Umber'], "---", som_Splashtails, '\n',
      dict_prob_Pondies, "---", dict_prob_Pondies['Charcoal'] + dict_prob_Pondies['Orchid'] + dict_prob_Pondies['Bronze'] + dict_prob_Pondies['Bright'], "---", som_Pondies, '\n',
      dict_prob_Islehoppers, "---", dict_prob_Islehoppers['Stone'] + dict_prob_Islehoppers['Moss'] + dict_prob_Islehoppers['Honey'] + dict_prob_Islehoppers['Raven'], "---", som_Islehoppers, '\n',
      dict_prob_Ancientscales, "---", dict_prob_Ancientscales['Almond'] + dict_prob_Ancientscales['Sapphire'] + dict_prob_Ancientscales['Smoke'] + dict_prob_Ancientscales['Bone'], "---", som_Ancientscales, '\n',
      dict_prob_Plentifins, "---", dict_prob_Plentifins['Olive'] + dict_prob_Plentifins['Amber'] + dict_prob_Plentifins['Cloudy'] + dict_prob_Plentifins['Bonedust'], "---", som_Plentifins, '\n',
      dict_prob_Wildsplashes, "---", dict_prob_Wildsplashes['Russet'] + dict_prob_Wildsplashes['Sandy'] + dict_prob_Wildsplashes['Ocean'] + dict_prob_Wildsplashes['Muddy'], "---", som_Wildsplashes, '\n',
      dict_prob_Devilfish, "---", dict_prob_Devilfish['Ashen'] + dict_prob_Devilfish['Seashell'] + dict_prob_Devilfish['Lava'] + dict_prob_Devilfish['Forsaken'], "---", som_Devilfish, '\n',
      dict_prob_Battlegills, "---", dict_prob_Battlegills['Jade'] + dict_prob_Battlegills['Sky'] + dict_prob_Battlegills['Rum'] + dict_prob_Battlegills['Sand'], "---", som_Battlegills, '\n',
      dict_prob_Wreckers, "---", dict_prob_Wreckers['Rose'] + dict_prob_Wreckers['Sun'] + dict_prob_Wreckers['Blackloud'] + dict_prob_Wreckers['Snow'], "---", som_Wreckers, '\n',
      dict_prob_Stormfish, "---", dict_prob_Stormfish['Ancient'] + dict_prob_Stormfish['Shores'] + dict_prob_Stormfish['Wild'] + dict_prob_Stormfish['Shadow'], "---", som_Stormfish, '\n')
print('------------------------------------------------------------------------------------------------------------------------------------------')
print("@@@@@@@@@@@@@@@@@@@@@@@@moyennes de temps selon technique ou non SAUF PONDIE")
print(tab)
nb_oui = nb_non = 0
for liste in tab:
    var, esp = recup_var_nom_esp(liste[0])
    if esp != 'Pondie':
        if liste[3] == 'Oui':
            nb_oui += 1
        elif liste[3] == 'Non':
            nb_non += 1
        else:
            print("@@@@@@@@@@@@un 'Non' ou un 'Oui' est mal écrit !!!@@@@@@@@@@@@")
if nb_oui == nb_non:
    print("nb_oui == nb_non, correct")
else:
    print("nb_oui != nb_non, INCORRECT")
print(nb_oui, nb_non)

liste_temps_tech = [[l[2], l[3]] for l in tab]
print(liste_temps_tech)
liste_temps_tech_oui = [[l[2], l[3]] for l in tab if l[3] == 'Oui']
liste_temps_tech_non = [[l[2], l[3]] for l in tab if l[3] == 'Non']
print(liste_temps_tech_oui)
print(liste_temps_tech_non)

moy_temps_oui = 0
for liste in liste_temps_tech_oui:
    moy_temps_oui += time_convert(liste[0])
moy_temps_oui /= nb_oui + nb_non
print("avec techniques :", time_deconvert(moy_temps_oui))
moy_temps_non = 0
for liste in liste_temps_tech_non:
    moy_temps_non += time_convert(liste[0])
moy_temps_non /= nb_oui + nb_non
print("sans techniques :", time_deconvert(moy_temps_non))
print('------------------------------------------------------------------------------------------------------------------------------------------')
# En pêcher bcp plus pour avoir valeur exacte de proba de poissons trophées, et de proba de variétés par espèces; et pour moy temps oui / non
# au moins 200 poissons !
# pour update le wiki
