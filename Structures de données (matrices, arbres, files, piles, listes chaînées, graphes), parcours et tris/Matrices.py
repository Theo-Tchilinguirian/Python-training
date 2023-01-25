


# Functions
def produit_matriciel(matrice_A, matrice_X):
    # Réalise le produit matriciel AX, renvoie la matrice AX. Ai,j; Xj,k non-vides.
    matrice_AX = []
    for i in range(len(matrice_A)):
        matrice_AX.append([])
        for k in range(len(matrice_X[0])):
            elt_ik = 0
            for j in range(len(matrice_X)):
                elt_ik += matrice_A[i][j] * matrice_X[j][k]
            matrice_AX[i].append(elt_ik)
    return matrice_AX

print(produit_matriciel([[1, 2], [4, 3], [3, 4]], [[1, 1],[3, 2]]))

def somme_matricielle(A, B):
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        C = []
        for i in range(len(A)):
            C.append([])
            for j in range(len(A[0])):
                C[i].append(A[i][j]+B[i][j])
        return C

print(somme_matricielle([[1, 2], [5, 4]], [[5, 6], [3, 2]]))

# Procedures