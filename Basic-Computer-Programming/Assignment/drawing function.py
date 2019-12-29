#함수 그리기
import turtle
t1=turtle.Turtle()
t2=turtle.Turtle()

t1.shape("turtle")
t2.shape("classic")


t1.fd(200)
t1.backward(200)
t1.left(90)
t1.fd(200)
t1.backward(200)

x=0
while x<50:
    
    y=((1/10)*(x**2))+1
    x=x+1
    t2.goto(x,y)


