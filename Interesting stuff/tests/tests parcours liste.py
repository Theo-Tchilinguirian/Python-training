# tableau lignes

def lg(n, m):
    Tab = []
    for i in range(n):
        Tab += [[]]
        for j in range(m):
            Tab[i] += [i+1]
    return Tab

# tableau colonnes

def cl(n, m):
    Tab = []
    for i in range(n):
        Tab += [[]]
        for j in range(m):
            Tab[i] += [j+1]
    return Tab
print(cl(3,4))