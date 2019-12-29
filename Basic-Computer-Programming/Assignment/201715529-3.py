x=int(input("정수를 입력하시요" ))

a=x//10**3
x=x-(10**3)*a
b=x//10**2
x=x-(10**2)*b
c=x//10
x=x-10*c
d=x

result=a+b+c+d

print("자리수의 합:",result)
