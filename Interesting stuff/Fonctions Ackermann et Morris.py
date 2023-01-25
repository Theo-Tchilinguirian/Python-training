def puissance_ou_exponentiation_rapide(x, n):
    if n == 1:
        return x
    elif n%2 == 0:
        return puissance_ou_exponentiation_rapide(x**2, n/2)
    elif n%2 == 1:  # Ou else
        return x*puissance_ou_exponentiation_rapide(x**2, n//2)


def A(m, n):
    if m == 0 and n >= 1:
        return n + 1
    elif n == 0 and m >= 1:
        return A(m-1, 1)
    elif n >= 1 and m >= 1:
        return A(m-1, A(m, n-1))


def M(m, n):
    if m == 0:
        return 1
    elif n >=1 and m >= 1:
        return M(m-1, M(m, n))
