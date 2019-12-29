import random
from tkinter import *

correct_answer=random.randint(1,10)
def a():
    answer=int(e2.get())
    if answer==correct_answer:
        l1['text']="정답"
    if answer>correct_answer:
        l1['text']="너무 높아요"
    if answer<correct_answer:
        l1['text']="너무 낮아요"

def b():
    e2.delete(0,END)
       
    
window=Tk()
window.title("숫자 맞추기 게임")
l1=Label(window,text=" ")
l1.grid(row=0,column=0,columnspan=2)
e2=Entry(window)
e2.grid(row=1,column=0,columnspan=2)

button1=Button(window,text="숫자를 입력",command=a)
button2=Button(window,text="게임을 다시 실행",command=b)
button1.grid(row=2,column=0)
button2.grid(row=2,column=1)



window.mainloop()

   
        



        

    
        
    
