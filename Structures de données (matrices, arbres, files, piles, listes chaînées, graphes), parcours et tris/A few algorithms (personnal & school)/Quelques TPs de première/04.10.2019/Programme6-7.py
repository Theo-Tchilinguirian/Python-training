from turtle import *

n = int(input("Nb de coté: "))
for k in range(0, n):
    forward(50)
    right(360/n)
