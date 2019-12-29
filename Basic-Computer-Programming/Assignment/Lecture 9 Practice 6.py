import random
import turtle
t=turtle.Turtle()
turtle.bgcolor("black")

t.speed(0)
star_colorlist=["red","yellow","green","gray","orange","black","pink","skyblue"]

def star():
    l=random.randint(13,113)
    for i in range(5):
        t.fd(l)
        t.right(144)

i=0
while True:
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    star()
    t.color(random.choice(star_colorlist))
    t.end_fill()
    i=i+1

    
