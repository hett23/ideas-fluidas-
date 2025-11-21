from turtle import*
from colorsys import* 

bgcolor("gray")
speed(0)
h=0

for i in range(371):
    c=hsv_to_rgb(h,1,1)
    h+=0.005
    color(c)
    circle(-i*0.68,200)
    right(88)

done()
