from turtle import *

speed(255)
for k in range(360):
    UnM1 = k - 1
    Un = k
    forward(UnM1 + Un)
    right(1)
    goto(0, 0)
