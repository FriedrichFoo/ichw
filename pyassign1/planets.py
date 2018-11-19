import turtle
import math
w = turtle.Screen()
w.bgcolor('black')
w.bgpic('Planetary Rotation in the Solar System')
turtle.setworldcoordinates(-500,-500,500,500)

sun = turtle.Turtle()
sun.shape('circle')
sun.color('yellow')
sun.setposition(0,0)
    
plant = ['mercury','venus','earth','mars','jupiter','saturn']
color = ['white','green','blue','brown','orange','purple']
lenth = [70,110,150,250,450,500]
a = [58,110,150,230,450,500]
q = [12,0,0,20,0,0]
b = [50,108,149,210,450,500]
v = [20,60,90,150,230,400]

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
            v0 = v[i]
            if (x/v0)%360 <= 180:
                v1 = v0-10
            else:
                v1 = v0+10
            plant[i].goto(a[i]*math.cos(x/v1)+q[i],b[i]*math.sin(x/v1))

def main():
    initial()
    circles()

if __name__ == "__main__":
    main()
    
    
    
import turtle
import math
w = turtle.Screen()
w.bgcolor('black')
turtle.setworldcoordinates(-500,-500,500,500)

sun = turtle.Turtle()
sun.shape('circle')
sun.color('yellow')
sun.setposition(0,0)
    
plant = ['mercury','venus','earth','mars','jupiter','saturn']
color = ['white','green','blue','brown','orange','purple']
lenth = [70,110,150,250,450,500]
a = [58,110,150,230,450,500]
q = [12,0,0,20,0,0]
b = [50,108,149,210,450,500]
v = [20,60,90,150,230,400]

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
    initial()
    circles()

if __name__ == "__main__":
    main()
