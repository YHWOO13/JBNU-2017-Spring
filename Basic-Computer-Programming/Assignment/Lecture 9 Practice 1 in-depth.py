#평균구하기
list=[ ]
n=int(input("입려할 숫자의 개수를 쓰시오: "))
c=0
x=0
while True:
    a=int(input("정수를 입력하시오: "))
    list.append(a)
    c=c+a
    x=x+1
    if x==n:
        break
        
print(list)
print(c/n)

#모든 곱 구하기

list=[ ]
n=int(input("n개의 숫자를 입력하시오: "))
c=1
for i in range(n):
    a=int(input("정수를 입력하시오: "))
    list.append(a)
    c=c*a
    
print(list)
print(c)

#선택

list=[ ]
n=int(input("n개의 숫자를 입력하시오: "))
answer=["모든곱","평균"]
print(answer)
answer=input("원하는 계산을 고르시오: ")

if answer=="모든곱":
    c=1
    for i in range(n):
        a=int(input("정수를 입력하시오: "))
        list.append(a)
        c=c*a
    print(list)
    print(c)


if answer=="평균":
    c=0
    for i in range(n):
        a=int(input("정수를 입력하시오: "))
        list.append(a)
        c=c+a
    
    print(list)
    print(c/n)
