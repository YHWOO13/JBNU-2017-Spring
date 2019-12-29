import random
import turtle
t=turtle.Turtle()
turtle.bgcolor("black")

star_colorlist=["red","yellow","green","gray","orange","black","pink","skyblue"]

def star():
    l=random.randint(13,113)
    for i in range(5):
        t.fd(l)
        t.right(144)


def drawit(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    star()
    s=turtle.textinput("별의 색깔","리스트에 있는 색 중 색칠할 색을 고르시오: ")
    t.color(s)
    t.end_fill()
s=turtle.Screen()
s.onscreenclick(drawit)

    
