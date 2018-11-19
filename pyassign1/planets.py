""" planets.py: Model of Planetary rotation in the solar system (mercury,venus,earth,mars,jupiter,saturn)
__author__ = 'Friedrich Foo'
__pkuid__ = '1800011746'
__email__ = '1800011746@pku.edu.cn'
"""
import math

import turtle
w = turtle.Screen()
w.bgcolor('black')
turtle.setworldcoordinates(-500,-500,500,500)
    
plant = ['mercury','venus','earth','mars','jupiter','saturn']
color = ['white','green','blue','brown','orange','purple']
lenth = [70,110,150,250,450,500]
a = [58,110,150,230,450,500]
q = [12,0,0,20,0,0]
b = [50,108,149,210,450,500]
v = [20,60,90,150,230,400]

def sunpos():
    sun = turtle.Turtle()
    sun.shape('circle')
    sun.color('yellow')
    sun.setposition(0,0)
    
def initial():
    for i in [0,1,2,3,4,5]:
        plant[i] = turtle.Turtle()
        plant[i].speed(0)
        plant[i].shape('circle')
        plant[i].color(color[i])
        plant[i].ht()
        plant[i].up()
        plant[i].setposition(lenth[i],0)
        plant[i].down()
        plant[i].st()

def circles():
    for x in range(36000):
        for i in [0,1,2,3,4,5]:
            plant[i].goto(a[i]*math.cos(x/v[i])+q[i],b[i]*math.sin(x/v[i]))

def main():
    sunpos()
    initial()
    circles()

if __name__ == "__main__":
    main()
