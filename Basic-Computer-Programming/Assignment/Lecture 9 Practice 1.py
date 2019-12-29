#평균구하기

list=[ ]
n=int(input("n개의 숫자를 입력하시오: "))
c=0
for i in range(n):
    a=int(input("정수를 입력하시오: "))
    list.append(a)
    c=c+a
    
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
answer=input("원하는 계산을 선택하시오: ")

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
