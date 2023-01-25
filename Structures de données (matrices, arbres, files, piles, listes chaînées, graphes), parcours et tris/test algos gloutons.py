# algos gloutons nsi

P = [0.05, 0.1, 0.2, 0.5, 1, 2]

while True:
    prix = float(input("prix: "))
    val = float(input("vous donnez: "))
    if prix > val:
        continue
    else:
        break

diff_val = val - prix

k = -1

while diff_val != 0 or k != -len(P):
    x = diff_val - P[k]
    if x > 0:
        diff_val = x
    else:
        k = k - 1
    print(diff_val, k)

print(diff_val)