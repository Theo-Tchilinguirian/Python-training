def factorielle(n):
    u = 1
    for i in range(2, n + 1):  # 2, 2 = Ne passe pas, 2, 1 = non plus, ...
        u = i * u
    return u


def factorielle_recursive(n):
    if n == 0:  # Si pas mis ça: ne s'arrête pas et n descends vers -inf
        u = 1
    else:
        u = n * factorielle_recursive(n - 1)
    return u


def factorielle_mathematique(n):
    if n == 0:
        return 1
    else:
        return n*factorielle_mathematique(n - 1)


print(factorielle(0))
print(factorielle_recursive(3))
print(factorielle_mathematique(2))