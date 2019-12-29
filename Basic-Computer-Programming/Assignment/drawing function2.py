#함수 그리기 다른 버전
import turtle
t1=turtle.Turtle()
t2=turtle.Turtle()

t1.shape("triangle")
t2.shape("classic")

t1.fd(200)
t1.stamp()
t1.backward(200)
t1.left(90)
t1.fd(200)
t1.stamp()
t1.backward(200)

def y():
    x=0
    while x<50:
        y=((1/10)*(x**2))+1
        x=x+1
        t2.goto(x,y)

y()   


