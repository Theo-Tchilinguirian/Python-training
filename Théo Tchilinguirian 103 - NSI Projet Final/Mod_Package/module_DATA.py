
"""
Les valeurs enregistrées dans ce module agissent comme des variables globales dans le code où leur module est appelé
cependant, elles ne sont pas modifiées dans le programme, ou permettent seulement d'initialiser le code.

Elles sont modifiables et permettent au programme d'être dynamique.
Ces variables sont donc modifiables afin de faire fonctionner le code différement.
"""

MsgError1 = "Valeur saisie invalide"

MsgError2 = "Pas de parties enregistrées. Lancez une nouvelle partie"

MsgError3 = "Le fichier est introuvable"

MsgError4 = "Vous devez répondre par oui ou non"

MsgError5 = "Choisissez une option parmi les options proposées"

MsgError6 = "Vous devez entrer vos choix, séparés par un espace ou non (exemple: 1 3; ou 21)"

ValASCII = 64  # Voir Mod_Package.module_FonctionsEntrées (get_ChoixCase()) et Voir Mod_Package.module_FonctionsAffichage (AffichTPlateau())

PremierJoueur = 1  # Voir Mod_Package.module_FonctionsMétier (init_NvPartie()); initialise le premier joueur actif.

FileSavePath = '/SAVES/UNFINISHED_SAVES'  # Depuis la fonction __main__

FileWonSavePath = '/SAVES/WON_SAVES'  # Depuis la fonction __main__

FileExtension = '.csv'  # Extension du fichier de sauvegarde et de charge

FileWritingSeparator = ';'  # Séparateur utilisé pour sauvegarder les données dans un fichier.
