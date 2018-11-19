""" planets.py: Model of Planetary rotation in the solar system (6 planets)
__author__ = 'Friedrich Foo'
__pkuid__ = '1800011746'
__email__ = '1800011746@pku.edu.cn'
"""
import math

import turtle
w = turtle.Screen()
w.bgcolor('black')
turtle.setworldcoordinates(-500,-500,500,500)

# following are lists by which we try to simulate the rotation
# shapesizes : diameter of planets
# lenth, a, q and b : parameter of rotation
# v : speed
# x controls motion
# ratation equation for (m,n): 
# m = a*cos(x/v)+q
# n = b*sin(x/v)
plant = ['mercury','venus','earth','mars','jupiter','saturn']
color = ['white','green','blue','brown','orange','purple']
shapesizes = [0.5, 0.9, 0.9, 0.6, 1.2, 1.2]
lenth = [70, 110, 150, 250, 450, 500]
a = [58, 110, 150, 230, 450, 500]
q = [12, 0, 0, 20, 0, 0]
b = [50, 108, 149, 210, 450, 500]
v = [20, 60, 80, 150, 230, 300]

def sunpos():
    """set the position of Sun
    """
    sun = turtle.Turtle()
    sun.shape('circle')
    sun.shapesize(1.5)
    sun.color('yellow')
    sun.setposition(0,0)
    
def initial():
    """set the position of planets
    """
    for i in [0,1,2,3,4,5]:
        plant[i] = turtle.Turtle()
        plant[i].speed(0)
        plant[i].shape('circle')
        plant[i].shapesize(shapesizes[i])
        plant[i].color(color[i])
        plant[i].ht()
        plant[i].up()
        plant[i].setposition(lenth[i],0)
        plant[i].down()
        plant[i].st()

def circles():
    """control the rotation of planets
    """
    for x in range(360000):
        for i in [0,1,2,3,4,5]:
            plant[i].goto(a[i]*math.cos(x/v[i])+q[i],b[i]*math.sin(x/v[i]))

def main():
    sunpos()
    initial()
    circles()
    turtle.done()

if __name__ == "__main__":
    main()
