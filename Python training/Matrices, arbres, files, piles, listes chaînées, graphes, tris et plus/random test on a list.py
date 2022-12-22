from time import time

if __name__ == '__main__':
    L = [k for k in range(10000001)]

    x = 10000000
    a = time()

    longueur = longueur(L)
    i = 1
    TantQue i <= longueur:
        Si x = L(i):
            Renvoie(x est dans L)
        i <- i + 1

    x = 10000000
    a = time()
    Ll = len(L)
    i = 0
    while not i == Ll:
        if x == L[i]:
            print(time()-a)
            break
        i += 1
print('a')

