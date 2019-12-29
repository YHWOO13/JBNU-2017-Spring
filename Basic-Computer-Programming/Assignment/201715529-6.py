import turtle
t=turtle.Turtle()
t.shape("turtle")


t.up()
a=int(input("A점의 x좌표를 입력하시오:" ))
b=int(input("A점의 y좌표를 입력하시오:" ))
A=(a,b)
t.goto(A)
t.down()
t.circle(1)


t.up()
c=int(input("B점의 x좌표를 입력하시오:" ))
d=int(input("B점의 y좌표를 입력하시오:" ))
B=(c,d)
t.goto(B)
t.down()
t.circle(1)
t.up()
t.goto(A)
t.down()
t.goto(B)

length=((a-c)**2+(b-d)**2)**0.5
t.up()
t.write("선의길이는= ",True,"left")

t.write(length,True)
t.goto(B)
