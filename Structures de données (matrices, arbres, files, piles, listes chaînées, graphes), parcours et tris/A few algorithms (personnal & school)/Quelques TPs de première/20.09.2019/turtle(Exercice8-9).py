from turtle import *
from random import *

taille = 40
angle = 120

down()
for i in range(3):
    forward(taille)
    left(angle)

up()
goto(100, 100)
down()

width(7)
for i in range(3):
    forward(taille)
    dot(20)
    left(angle)

up()
goto(-100, -100)
down()

width(1)
color("blue")
forward(taille)
color("green")
left(angle)
forward(taille)
color("red")
left(angle)
forward(taille)
left(angle)

up()
goto(100, -100)
down()

width(7)
for i in range(3):
    color("green")
    forward(taille)
    left(angle)

up()
goto(100, -100)
down()

color("purple")
dot(20)
up()
forward(taille)
left(angle)
down()
dot(20)
up()
forward(taille)
left(angle)
down()
dot(20)
up()
forward(taille)
left(angle)
down()

up()
goto(-100, 100)
down()

width(2)
color("blue")

circle(30, 360)
up()
goto(-100, 90)
down()
circle(20, 360)
up()
goto(-100, 80)
down()
circle(10, 360)

up()
goto(-100, 100)
down()
goto(-100, 140)













