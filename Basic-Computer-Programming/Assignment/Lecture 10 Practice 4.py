from tkinter import *

def inch_to_cm():
    inch=float(e2.get())
    cm=inch*2.54
    e3.insert(0, str(cm))

window=Tk()

l1=Label(window,text="인치를 센치미터로 변환하는 프로그램: ")
l1.grid(columnspan=2)
l2=Label(window,text="인치를 입력하시오: ")
l2.grid(row=1,column=0)
l3=Label(window,text="변환결과")
l3.grid(row=2,column=0)
e3=Entry(window)
e3.grid(row=2,column=1)
button=Button(window,text="변환!",command=inch_to_cm)
button.grid(row=3, column=1)

e2=Entry(window)
e2.grid(row=1,column=1)
