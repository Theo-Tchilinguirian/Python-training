   # --------------------------------------------------------- #
   #                                                           #
   #   Jeu Hoop - Octobre 2020                                 #
   #                                                           #
   #               Srtuctures de données                       #
   #                        Programmation orientée objet       #
   #                                                           #
   #   Moinet Dominique                                        #
   #                                                           #
   # --------------------------------------------------------- #

#                     xxxxxxxxxxxxxxxxxxxx
#                     x    Les imports   x
#                     xxxxxxxxxxxxxxxxxxxx

import random



#                     xxxxxxxxxxxxxxxxxxxx
#                     x    Les classes   x
#                     xxxxxxxxxxxxxxxxxxxx

# **************************************************************
# La classe pile qui détermine les attributs et fonctionnalités
# **************************************************************
class pile:

    def __init__(self,n):
       self.contenu=[]
       self.taille=n     


    def EstVide(self):
      return len(self.contenu)==0

    def EstPlein(self):
      return len(self.contenu)==self.taille

    def sommet(self):
        if self.EstVide():
           print("pas de sommet, la pile est vide") 
        else:
           return self.contenu[-1]
        
    def NbElt(self):
        return len(self.contenu)
        
    def empiler(self,a):
        if self.EstPlein():
           print("pas possible, la pile est pleine") 
        else:
           return self.contenu.append(a)

    def depiler(self,a):
        if self.EstVide():
           print("pas possible, la pile est vide") 
        else:
           return self.contenu.pop()

    def deplace(self,P):
        a=self.sommet()
        self.depiler(a)
        P.empiler(a)
        return P
                    # ********************************** #
                    #      Fin de la classe pile         #
                    # ********************************** #        

# ******************************************************************
# La classe JeuHoop qui détermine les attributs et fonctionnalités
# ******************************************************************

class JeuHoop:

    def __init__(self,n):
  
       # Construction du jeu
       L=[]                    # Création des éléments
       for i in range(n):      # du jeu :
          for j in range(n):  # n 0, n 1, ... n n-1
             L.append(i)       # n = 3 : L = [0,0,0,1,1,1,2,2,2]
       random.shuffle(L)       # mélange des éléments
       J=[]                    # Liste (de listes) contenant le jeu final
       for i in range(0,len(L),n):
          P=pile(n)                # Constitution d'un pieu
          for j in range(n):  # On prend n éléments successifs de L
             P.empiler(L[i+j])
          J.append(P)
       J.append(pile(n))            # pieu vide
       if n>=4:
          J.append(pile(n))        # besoin d'un autre pieu vide si beucoup d'éléments
       if n==7:
          J.append(pile(n))
          
       # L'attribut LesPieux, une liste de piles
       self.LesPieux=J

       # Attribut NbPieu, le nombre de pieux (piles) du jeu
       self.NbPieu=len(J)

       # Attribut hauteur, le nombre maximal de pions par de pieu (nbr max d'éléments d'une pile)
       self.hauteur=n
      



    def __repr__(self):   
     # Représentation graphique du jeu
       n=self.NbPieu
       h=self.hauteur
       ligne="   "+n*"---    "
       txt=""  # La chaine de caractères finale à afficher, représentant le jeu
       for i in range(h):
           lc="" # ligne courante
           for j in range(n):
             if self.LesPieux[j].NbElt() <= i:
                 car=" "
             else:
                 car=chr(self.LesPieux[j].contenu[i]+65)  # Couleurs remplacées par des lettres
             lc=lc+"  | "+car+" |"    # matérialise les colonnes
           txt=lc+"\n"+ligne+"\n"+txt
       txt=ligne+"\n"+txt
       txt=txt+"    "
       for k in range(n):
           txt=txt+str(k+1)+"      "  # numérotation des pieux
       return txt


    def gagnant(self):
       # Renvoie un booléen valant vrai si la partie est finie
       # Le jeu est fini si les pieux contiennent "toutes les listes de même valeur"
       P=[]
       for k in range(self.NbPieu):
          P.append(self.LesPieux[k].contenu)
       G=True
       h=self.hauteur
       for i in range(0,h):
         L=[]
         for j in range(h):
             L.append(i)
         G=G and (L in P)
       return G

                    # ************************************* #
                    #      Fin de la classe JeuHoop         #
                    # ************************************* #        


#                     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#                     x    Les fonctions d'entrrée/sortie    x
#                     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def menu():
    print("0 : Pour quitter")
    print("1 : Pour commencer une partie")
    rep=int(input("Votre réponse : "))
    ok=rep==1
    nb=0
    if ok:
      print("Vous voulez jouer avec combien de couleurs (entre 3 et 7)")
      nb=int(input("Votre réponse : "))
    return nb         
             
def LireMvt(J):
    n=J.NbPieu
    ok=False
    while not ok:
      print("n° du pieu du pion à déplacer (entre 1 et",n,")",end="")
      i=int(input(" : "))
      if i<1 or i>n:
         print("valeur non valide")
      elif J.LesPieux[i-1].EstVide():
         print("Impossible,pas de pion sur ce pieu") 
      else:
        ok =True
    ok=False
    while not ok:
      print("n° du pieu du pion à revevoir (entre 1 et",n,")",end="")
      j=int(input(" : "))
      if j==i:
        print("Pas de déplacement, vous pouvez continuer à jouer")
        ok =True
      else:
        if j<1 or j>n:
          print("valeur non valide")
        elif J.LesPieux[j-1].EstPlein():
          print("Impossible,le pieu est plein") 
        elif (not J.LesPieux[j-1].EstVide()) and J.LesPieux[j-1].sommet()!=J.LesPieux[i-1].sommet():
          print("Impossible,le pion n'est pas compatible avec le récepteur")
        else:
          ok =True        
    return i-1,j-1

#                     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#                     x         Le programme principal       x
#                     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

h=menu()
while h!=0: 
  G = False
  Jeu=JeuHoop(h)
  while (not G):  
    print(Jeu)
    i,j = LireMvt(Jeu)
    Jeu.LesPieux[i].deplace(Jeu.LesPieux[j])
    G=Jeu.gagnant()
  print()
  print("   ====> Yeah! <====")
  print(Jeu)
  print("   ***** c'est gagné ****")
  print()
  h=menu()


