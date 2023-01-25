print("Nombre négatif pour arreter le processus")

y = True
msg = ""

while y:
    n = int(input("nb: "))

    if n < 0:
        y = False
        break

    msg += ' '*n + '-'

print(msg)