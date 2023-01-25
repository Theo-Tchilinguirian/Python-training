
from random import randint

def Générateur_MDP(n, typ):
    liste_mdp = []
    for k in range(n):
        if typ == -1:
            cond = randint(0, 6)
        else:
            cond = typ

        cond_adder(cond, liste_mdp)
    return "".join(liste_mdp)

def cond_adder(cond, liste_mdp):
    if cond == 0:
        liste_mdp.append(chr(randint(33, 47)))
    if cond == 1:
        liste_mdp.append(chr(randint(48, 57)))
    if cond == 2:
        liste_mdp.append(chr(randint(58, 64)))
    if cond == 3:
        liste_mdp.append(chr(randint(65, 90)))
    if cond == 4:
        liste_mdp.append(chr(randint(91, 96)))
    if cond == 5:
        liste_mdp.append(chr(randint(97, 122)))
    if cond == 6:
        liste_mdp.append(chr(randint(123, 126)))
    return liste_mdp


print(Générateur_MDP(1995, -1))