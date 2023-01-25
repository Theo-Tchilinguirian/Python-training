
L = [1, 2, 3]
it = iter(L)
print(it)
print(it.__next__())
print(next(it))
print(next(it))

for i in iter(L):
    print(i)

iterator = iter(L)
t = tuple(iterator)
print(t)

iterator = iter(L)
a, b, c = iterator
print(a, b, c)

L = [('Italy', 'Rome'), ('France', 'Paris'), ('Ponyland', 'Ponyville')]
print(tuple(iter(L)))
print(dict(iter(L)))
for i in iter(L):
    print(i)


def f(x):
    for i in range(x):
        yield i

f(10)









