
# Utilisation d'une liste d'adjacence              
def parcours_en_largeur(g, sommet):
        visités = [False] * (len(g))
        aux = []
        # File d'attente
        F = []
        F.append(sommet)
  
        while F:
            # On défile et on afficher le sommet en tete de la file 
            sommet = F.pop(0)
            if visités[sommet-1] == False:
                print(sommet, end=" ")
                visités[sommet-1] = True
  
            # pour chaque voisin i de s faire
            for u in g[sommet]:
  
                if visités[u-1] == False:
                    print(u, end=" ")
                    F.append(u)
                    visités[u-1] = True
               
                  
def parcours_en_profondeur(g, sommet, visités):
  
        # On marque le noeud courant comme visité et on l'afficher
        visités[sommet-1] = True
        print(sommet, end=" ")
  
        # On recommence avec tous les noeuds voisins
        for u in g[sommet]:
            if visités[u-1] == False:
                parcours_en_profondeur(g,u, visités)
 
g =  {3: [1, 2], 1: [3, 4, 5, 6], 4: [1, 5], 5: [1, 4], 6: [1], 2: [3]}    

parcours_en_largeur (g,1)     #  => 1 3 4 5 6 2
print("----------------")
visités = [False] * (len(g))
parcours_en_profondeur (g,1,visités)   #  => 1 3 2 4 5 6
parcours_en_largeur (g,3) 
  
  
  


