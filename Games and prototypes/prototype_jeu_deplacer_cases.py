"""
Docstring janvier 2023
Code non commenté, qui date un peu. Le niveau de compréhensibilité du code est si faible que
c'est sûrement un chapitre entier du cahier des charges. En tout cas c'est un bon entraînement
technique sur les listes, et sur la manipulation de valeurs (voire d'objets) dans une matrice.
C'est en essayant de comprendre du vieux code qu'on apprend par la manière forte qu'il faut
bien le commenter.
"""

from random import randint

n = 4
plt = [[(j*n+i)+1 for i in range(n)] for j in range(n)]  # python list comprehension
case_vide_pos = [0,0]
print(plt)
for i in range(n):
    for j in range(n):
        if plt[i][j] ==  16:
            case_vide_pos = [i,j]
i = 0
for i in range(n*n):
    direction = randint(1,4)
    if direction == 1 and case_vide_pos[0]>0:
        tmp = plt[case_vide_pos[0]-1][case_vide_pos[1]]
        plt[case_vide_pos[0]-1][case_vide_pos[1]] = plt[case_vide_pos[0]][case_vide_pos[1]]
        plt[case_vide_pos[0]][case_vide_pos[1]] = tmp
        case_vide_pos[0] -= 1

    elif direction == 2 and case_vide_pos[0]<n-1:
        tmp = plt[case_vide_pos[0]+1][case_vide_pos[1]]
        plt[case_vide_pos[0]+1][case_vide_pos[1]] = plt[case_vide_pos[0]][case_vide_pos[1]]
        plt[case_vide_pos[0]][case_vide_pos[1]] = tmp
        case_vide_pos[0] += 1

    elif direction == 3 and case_vide_pos[1]>0:
        tmp = plt[case_vide_pos[0]][case_vide_pos[1]-1]
        plt[case_vide_pos[0]][case_vide_pos[1]-1] = plt[case_vide_pos[0]][case_vide_pos[1]]
        plt[case_vide_pos[0]][case_vide_pos[1]] = tmp
        case_vide_pos[1] -= 1

    elif direction == 4 and case_vide_pos[1]<n-1:
        tmp = plt[case_vide_pos[0]][case_vide_pos[1]+1]
        plt[case_vide_pos[0]][case_vide_pos[1]+1] = plt[case_vide_pos[0]][case_vide_pos[1]]
        plt[case_vide_pos[0]][case_vide_pos[1]] = tmp
        case_vide_pos[1] += 1


for i in range(n*n):
    if i%n == 0:
        print()
        for j in range(n):
            print("---",end="")
        print()
        print("|",end="")
    if plt[i//n][i%n] != 16:
        print(str(plt[i//n][i%n]).rjust(2),end="|")
    else:
        print("  ",end="|")
print()
for j in range(n):
    print("---",end="")
print()
end = False
while not end:
    direction = input("direction(H(HAUT),B(BAS),G(GAUCHE),D(DROITE)): ")
    if direction == "H" and case_vide_pos[0]>0:
        tmp = plt[case_vide_pos[0]-1][case_vide_pos[1]]
        plt[case_vide_pos[0]-1][case_vide_pos[1]] = plt[case_vide_pos[0]][case_vide_pos[1]]
        plt[case_vide_pos[0]][case_vide_pos[1]] = tmp
        case_vide_pos[0] -= 1

    elif direction == "B" and case_vide_pos[0]<n-1:
        tmp = plt[case_vide_pos[0]+1][case_vide_pos[1]]
        plt[case_vide_pos[0]+1][case_vide_pos[1]] = plt[case_vide_pos[0]][case_vide_pos[1]]
        plt[case_vide_pos[0]][case_vide_pos[1]] = tmp
        case_vide_pos[0] += 1

    elif direction == "G" and case_vide_pos[1]>0:
        tmp = plt[case_vide_pos[0]][case_vide_pos[1]-1]
        plt[case_vide_pos[0]][case_vide_pos[1]-1] = plt[case_vide_pos[0]][case_vide_pos[1]]
        plt[case_vide_pos[0]][case_vide_pos[1]] = tmp
        case_vide_pos[1] -= 1

    elif direction == "D" and case_vide_pos[1]<n-1:
        tmp = plt[case_vide_pos[0]][case_vide_pos[1]+1]
        plt[case_vide_pos[0]][case_vide_pos[1]+1] = plt[case_vide_pos[0]][case_vide_pos[1]]
        plt[case_vide_pos[0]][case_vide_pos[1]] = tmp
        case_vide_pos[1] += 1
    else:
        print("vous ne pouvez pas aller dans cette direction......")

    cpt = 0  # compteur
    while cpt < n*n-1 and plt[cpt//n][cpt%n] < plt[(cpt+1)//n][(cpt+1)%n]:
        cpt += 1
    print(cpt)
    if cpt == n*n-1:
        print("vous avez gagné")
        end = True

    for i in range(n*n):
        if i%n == 0:
            print()
            for j in range(n):
                print("---",end="")
            print()
            print("|",end="")
        if plt[i//n][i%n] != 16:
            print(str(plt[i//n][i%n]).rjust(2),end="|")
        else:
            print("  ",end="|")
    print()
    for j in range(n):
        print("---",end="")
    print()

