from turtle import *
from random import randint

speed(1000)
for k in range(700):
    for k in range(12):
        longueur = randint(10, 50)
        angle = randint(-80, 80)
        forward(longueur)
        right(angle)

    up()
    goto(0, 0)
    down()
