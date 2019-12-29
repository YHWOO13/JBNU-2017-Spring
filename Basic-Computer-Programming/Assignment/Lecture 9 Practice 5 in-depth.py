#9강 연습문제 5번
import random
import turtle

t=turtle.Turtle()
x=0
y=0
way=[[x,y,"red"],
        [x,y,"yellow"],
        [x,y,"green"],
        [x,y,"gray"],
        [x,y,"orange"],
        [x,y,"black"],
        [x,y,"pink"],
        [x,y,"skyblue"]]

def shape():
    n=int(turtle.textinput("다각형그리기",
                   "몇각형을 그리시겠습니까?"))
    l=random.randint(13,113)
    for i in range(n):
        t.fd(l)
        t.left(360/n)

for x,y,c in way:
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.color(c)
    shape()
    t.end_fill()
   
    
