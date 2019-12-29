#9강 연습문제 5번
import random
import turtle

t=turtle.Turtle()
n_color_list=["red","yellow","green","gray","orange","black","pink","skyblue"]


def shape():
    n=int(turtle.textinput("다각형그리기",
                   "몇각형을 그리시겠습니까?"))
    l=random.randint(13,113)
    for i in range(n):
        t.fd(l)
        t.left(360/n)

while True:
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.color(random.choice(n_color_list))
    shape()
    t.end_fill()
   
    
