##########################################################
# TP  Programmer avec des Fonctions                      #
##########################################################

#------------------------
# Date
# Nom et prenom et classe
# -----------------------



#********************************************
#   Les fonctions d'entrée et de sortie
#********************************************
def menu():
   print (30*"-")
   print ("  0. Quitter")
   print ("  1. Compter les espaces dans un texte")
   print ("  2. Compter un caractère dans un texte")
   print ("  3. Supprimer les espaces dans un texte")
   print ("  4. Supprimer un caractère dans un texte")
   print ("  5. Modifier un caractère dans un texte")
   print ("  6. Convertir un texte en majuscules sans espace en minuscules")
   print ("  7. Convertir un texte en majuscules avec espace en minuscules")
   print ("  8. Rechercher le caractère le plus présent dans un texte")
   print ("  9. Rechercher une chaine de caractères dans un texte")
   print (30*"-")
   rep=int(input("         Votre reponse : "))
   print (30*"-")
   print()
   return rep

def attente(n):
# Entrée : n un entier
# Sortie : affichage
  print("   ------>   Réponse",n,"en attente   <------")

  
#********************************************
#   Les fonctions métiers
#********************************************

# Compter les espaces
#.....................

def CompteEspace(Txt):
# Donnée : txt une chaine de caractères
# Résultat : cpt entier prenant pour valeur le nombre d'espace de txt.
  cpt=0 # On initialise le compteur à 0
  for i in range(0,len(Txt)): # on parcourt la chaine de caracteres
    if Txt[i]==" ":
      cpt=cpt+1  # on augmente de 1 le compteur pour chaque espace rencontre
  return cpt



# Compter un caractère donné
#............................

def CompteCar(Txt,car):
# Donnée : txt une chaine de caractères, car un caractère
# Résultat : cpt entier prenant pour valeur le nombre de caractère car de txt.
  cpt=0 # On initialise le compteur à 0
  for k in range(0, len(Txt)):
    if Txt[k] == car:
      cpt = cpt + 1
  return cpt


# Supprimer les espaces
#.......................

def SupprEspace(Txt):
# Donnée : txt une chaine de caractères
# Résultat : cpt entier prenant pour valeur le nombre d'espace de txt.
  NvTxt="" # On initialise un nouveau texte à vide
  for k in range(0,len(Txt)): # on parcourt la chaine de caracteres
    if Txt[k]!=" ":
      NvTxt=NvTxt+Txt[k]  #Si le caractère n'est pas un espace, on écrit le caractère correspondant au texte 
  return NvTxt


# Supprimer un caractère donné
#..............................

def SupprCar(Txt,car):
# Donnée : txt une chaine de caractères
# Résultat : cpt entier prenant pour valeur le nombrede caractère car de txt.
  NvTxt="" # On initialise un nouveau texte à vide
  for k in range(len(Txt)):
     if Txt[k] != car:
        NvTxt  = NvTxt + Txt[k]

  return NvTxt

# Remplacer un caractère donné par un autre caractère
#....................................................

def ModifCar(txt,c1,c2):
# Donnée : txt une chaine de caractères
#          c1 et c2 deux caractères 
# Résultat : NvTxt, chaine de caractère correspondant à txt dont le caractère
#            c1 a été changé en c2
  NvTxt="" # On initialise un nouveau texte à vide
  for k in range(len(Txt)):
     if Txt[k] == c1:
        NvTxt = NvTxt + c2
     else:
         NvTxt  = NvTxt + Txt[k]

  return NvTxt




# Convertir un texte en majuscules sans espace en minuscules
#............................................................
def MajMin1(TxtMaj):  # arguments à définir
# Donnée : TxtMaj un texte en maj sans espaces
# Résultat : TxtMin: TxtMaj converti en minuscules
   TxtMin = "" # On initialise le texte à vide
   for k in range(len(TxtMaj)):
      TxtMin = TxtMin + chr(ord(TxtMaj)+32)
   return TxtMin



# Convertir un texte en majuscules avec espace en minuscules
#............................................................
def MajMin2(TxtMaj):  # arguments à définir
# Donnée : TxtMaj un texte en maj
# Résultat : TxtMin: TxtMaj converti en minuscules   
   TxtMin = "" # On initialise le texte à vide
   for k in range(len(TxtMaj)):
      if TxtMaj[k] == " ":
         TxtMin = TxtMin + TxtMaj[k]
      else:
         TxtMin = TxtMin + chr(ord(TxtMaj)+32)
   return TxtMin


# Recherche le caractère le plus présent dans un texte
#......................................................
def MaxCar(ChaineCar, Car):  # arguments à définir
# Donnée : Car le caractere que l'on cherche
# Résultat : gCar le caractere le plus présent dans le texte
   Fréq = {}
   for Car in ChaineCar.lower():
      Fréq[Car] = ChaineCar.count(Car)
      for Key, Value in Fréq.items():
         if Value == max(Fréq.values()):
            gCar = {Key: Value}
          
   return gCar

# Recherche un mot dant un chaine de caractères
#...............................................
def ChercheMot(Chaine, Mot):  # arguments à définir
# Donnée : Chaine la chaine avec le mot a chercher
#          Mot le mot à chercher
# Résultat : pos la position
  return Chaine.find(Mot)


#********************************************
#   Le programme principal
#********************************************

rep=1
while rep!=0:
  rep=menu()
  if rep==1:
    Txt=input("texte dont on compte les espaces (non vide) : ")
    NbEspace=CompteEspace(Txt)
    print("Le texte saisi contient",NbEspace,"espace(s)")
  elif rep==2:          
    Txt=input("texte dont on compte un caractère (non vide) : ")
    Car=input("Caractère à compter : ")
    NbCar=CompteCar(Txt,Car)
    print("Le texte saisi contient",NbCar,"caractère(s)",Car)
  elif rep==3:
    attente(rep)
    Txt = input("texte dont on veux supprimer les espaces: ")
    NvTxt = SupprEspace(Txt)
    print("bah sa donne", NvTxt)
    
  elif rep==4:
    attente(rep)
    Txt = input("texte dont on veux supprimer le car: ")
    Car = input("le car: ")
    NvTxt = SupprCar(Txt,Car)
    print(NvTxt)
  elif rep==5:
    attente(rep)
    txt = input("txt dont on veux modif un car par un autre")
    c1 = input("car à changer")
    c2 = input("car pour changer")
    NvTxt = ModifCar(txt,c1,c2)
    print(NvTxt)
  elif rep==6:
    attente(rep)
    TxtMaj = input("txt en maj sans espace à convertir en min")
    NvTxt = MajMin1(TxtMaj)
    print(NvTxt)
  elif rep==7:
    attente(rep)
    TxtMaj = input("txt en maj à convertir en min")
    NvTxt = MajMin2(TxtMaj)
    print(NvTxt)
  elif rep==8:
    attente(rep)
    ChaineCar = input("Chaine")
    Car = input("Car à trouver")
    NvTxt = MaxCar(ChaineCar, Car)
    print(NvTxt)
  elif rep==9:
    attente(rep)
    Chaine = input("Chaine")
    Mot = input("mot à trouver")
    NvTxt = ChercheMot(Chaine, Mot)
    print(NvTxt)
  else:
    if rep!=0:
      print("Réponse non valide")
  print()  
            
            
