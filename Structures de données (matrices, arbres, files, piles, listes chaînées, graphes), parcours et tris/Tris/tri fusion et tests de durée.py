
import time

# Diviser pour régner ce n'est pas que les tris !
# Sauf ici.


def fusion(gauche, droite):
    résultat = []
    index_gauche = index_droite = 0
    while index_gauche < len(gauche) and index_droite < len(droite):
        if gauche[index_gauche] <= droite[index_droite]:
            résultat.append(gauche[index_gauche])
            index_gauche += 1
        else:
            résultat.append(droite[index_droite])
            index_droite += 1
    if len(gauche) > 0:
        résultat += gauche[index_gauche:]
    if len(droite) > 0:
        résultat += droite[index_droite:]
    return résultat


def tri_fusion(m):
    if len(m) <= 1:
        return(m)
    else:
        milieu = int(len(m)/2)
        gauche = m[:milieu]
        droite = m[milieu:]
        gauche = tri_fusion(gauche)
        droite = tri_fusion(droite)
    return fusion(gauche, droite)


deb = time.time()
res = tri_fusion([1, 2, 3, 5, 4])
print(res)
res = tri_fusion([7, 21, 2, 40, 1, 10])
print(res)
# Aucune idée comment aucun des 2 tris fusion marche; je connais mm pas la différence entre les deux
# le prof fait que lire le code; parfois. On code le pseudo-code puis la scéance est terminée
# Les variables ont aucun sens, ...
fin = time.time()
print('a', fin-deb)
print(time.thread_time())
d = time.time()
del fusion, tri_fusion
f = time.time()
print('a',f-d)

def tri_fusion(T):
    if len(T) <= 1:
        return T
    T1 = T[:int(len(T)/2)]
    T2 = T[int(len(T)/2):]
    return fusion(tri_fusion(T1), tri_fusion(T2))


def fusion(T1, T2):
    if T1 == []:
        return T2
    if T2 == []:
        return T1
    if T1[0] < T2[0]:
        return [T1[0]] + fusion(T1[1:], T2)
    else:
        return [T2[0]] + fusion(T1, T2[1:])

deb = time.time()
res = tri_fusion([3, 4, 6, 2, 5, 1, 8, 7])
print(res)
fin = time.time()
print('a',fin-deb)


print(time.thread_time())
print(time.time())
time.sleep(1)
print(time.time())
