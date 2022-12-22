
#----------------------------------------------------------------------------------------------------------------------#
# Théo Tchilinguirian 103
# Projet final de NSI à rendre pour fin Mai 2020
# Jeu de Isola avec plateau dynamique, sauvegarde des scores et des parties en format .csv, chargement des parties non terminées, et options de jeu facultatives !
#----------------------------------------------------------------------------------------------------------------------#

# Un petit peu d'information: Le programme utilise des chemins absolus lors de la manipulation de fichiers. certaines fonctions et méthodes ne semblent pas fonctionner lorsqu'elles sont utilisées avec des chemins relatifs.

# Imports

import Mod_Package.module_FonctionsEntrées as mod_Ent

import os


def __main__():
    """
    """

    # printer les 2 regles du jeu ici
    # puis sauter environ 10 lignes
    
    mod_Ent.AffichMenuPrinc()

__main__()

os.system('pause')
