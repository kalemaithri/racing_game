import turtle
import random
import sys
n=int(input("enter the number of turtles :"))
t1=turtle.Turtle()
l=[]
turtle.screensize(400,300,"#994444")
for i in range(n):
    t=turtle.Turtle()
    t.shape("turtle")
    t.speed(0)
    t.pu()
    t.setposition(-340,260-(i*100))
    t.pd()
    t1.pensize(3)
    t1.pu()
    t1.setposition(-340,240-(i*100))
    t1.pd()
    t1.fd(760)
    l.append(t)
def hh():
    for i in range(n):
        l[i].fd(random.randint(0,10))
        x,y=l[i].position()
        if(x>=360):
            print(i+1,"is the winner ")
            sys.exit(0)
    turtle.ontimer(hh,1)
hh()
