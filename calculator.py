##import tkinter as tk
from tkinter import *
app = Tk()
app.geometry("170x230")
app.title("My-Calculator")

ent = Entry(app, width=16, borderwidth=4, relief=SUNKEN)
ent.grid(pady=10,row=0,sticky="w",padx=15)


def delete():
    a = ent.get()
    ent.delete(first=len(a)- 1, last="end")

def fresult():
    if ent.get() == "":
        pass
    elif ent.get()[0] == "0":
        ent.delete(0, "end")
    else:
        c_res = ent.get()
        c_res = eval(c_res)
        clearf()
        ent.insert("end", c_res)


def clearf():
    ent.delete(0, "end")

clean = Button(app,text="Clear",width=4,command=clearf,bg="green",fg="white",relief=SUNKEN)
clean.grid(row=0,sticky="w",padx=125)

nine = Button(text="9",width=2,command=lambda : ent.insert("end","9"),borderwidth=3,relief=SUNKEN,fg="black")
nine.grid(row=1,sticky="w",padx=15)

eight = Button(text="8",width=2,command=lambda : ent.insert("end","8"),borderwidth=3,relief=SUNKEN,fg="black")
eight.grid(row=1,sticky="w",padx=45)

seven = Button(app,text="7",width=2,command=lambda : ent.insert("end","7"),borderwidth=3,relief=SUNKEN,fg="black")
seven.grid(row=1,sticky="w",padx=75)

plus = Button(app,text="+",width=2,command=lambda : ent.insert("end","+"),borderwidth=3,relief=SUNKEN,fg="black")
plus.grid(row=1,sticky="e",padx=125)

six = Button(text="6",width=2,command=lambda : ent.insert("end","6"),borderwidth=3,relief=SUNKEN,fg="black")
six.grid(row=2,sticky="w",padx=15,pady=5)

five = Button(text="5",width=2,command=lambda : ent.insert("end","5"),borderwidth=3,relief=SUNKEN,fg="black")
five.grid(row=2,sticky="w",padx=45,pady=5)

four = Button(app,text="4",width=2,command=lambda : ent.insert("end","4"),borderwidth=3,relief=SUNKEN,fg="black")
four.grid(row=2,sticky="w",padx=75,pady=5)

minus = Button(app,text="-",width=2,command=lambda : ent.insert("end","-"),borderwidth=3,relief=SUNKEN,fg="black")
minus.grid(row=2,sticky="e",padx=125,pady=5)

three = Button(text="3",width=2,command=lambda : ent.insert("end","3"),borderwidth=3,relief=SUNKEN,fg="black")
three.grid(row=3,sticky="w",padx=15,pady=5)

two = Button(text="2",width=2,command=lambda : ent.insert("end","2"),borderwidth=3,relief=SUNKEN,fg="black")
two.grid(row=3,sticky="w",padx=45,pady=5)

one = Button(app,text="1",width=2,command=lambda : ent.insert("end","1"),borderwidth=3,relief=SUNKEN,fg="black")
one.grid(row=3,sticky="w",padx=75,pady=5)

multiply = Button(app,text="*",width=2,command=lambda : ent.insert("end","*"),borderwidth=3,relief=SUNKEN,fg="black")
multiply.grid(row=3,sticky="e",padx=125,pady=5)

zero = Button(text="0",width=2,command=lambda : ent.insert("end","0"),borderwidth=3,relief=SUNKEN,fg="black")
zero.grid(row=4,sticky="w",padx=15,pady=5)

double_zero = Button(text="00",width=2,command=lambda : ent.insert("end","00"),borderwidth=3,relief=SUNKEN,fg="black")
double_zero.grid(row=4,sticky="w",padx=45,pady=5)

dot = Button(app,text=".",width=2,command=lambda : ent.insert("end","."),borderwidth=3,relief=SUNKEN,fg="black")
dot.grid(row=4,sticky="w",padx=75,pady=5)

divide = Button(app,text="/",width=2,command=lambda : ent.insert("end","/"),borderwidth=3,relief=SUNKEN,fg="black")
divide.grid(row=4,sticky="e",padx=125,pady=5)

result = Button(app,text="=",width=10,command=fresult,bg="green",fg="white",borderwidth=3,relief=SUNKEN)
result.grid(row=5,sticky="w",padx=15,pady=5)

modulus = Button(app,text="%",width=2,command=lambda : ent.insert("end","%"),borderwidth=3,relief=SUNKEN,fg="black")
modulus.grid(row=5,sticky="e",padx=125,pady=5)

delete = Button(app,text="del",width=2,command=delete,borderwidth=3,relief=SUNKEN,fg="black")
delete.grid(row=5,sticky="w",padx=80,pady=5)

app.mainloop()





















##def add(number1,number2):
##        number3= number1+number2
##        return number3
##
##def sub(number1,number2):
##        number3= number1-number2
##        return number3
##
##def mul(number1,number2):
##        number3= number1*number2
##        return number3
##
##def div(number1,number2):
##        number3= number1/number2
##        return number3
##
##def allop(number1,number2):
##        Alloperation= (number1+number2,number1-number2,number1*number2,number1/number2)
##        return Alloperation
##
##def menus():
##    print("---- Menu----")
##    print("---- 1. Addition----")
##    print("---- 2. Subtraction----")
##    print("---- 3. Multiplication----")
##    print("---- 4. Division----")
##    print("---- 5. All Operation----")
##    print("---- 6. Exit----")
##    
##menus()
##choice = int(input("Enter your number:-  "))
##
##while choice<7:
##        if choice==6:
##                print("------You are exit------")
##                menus()
##                break
##
##        else:
##                number1 = int(input("Enter your first number :- "))
##                number2 = int(input("Enter your second number:- "))
##                if choice==1:
##                        print("Addition:- ", add(number1,number2))
##                elif choice==2:
##                        print("Subtraction:- ", sub(number1,number2))
##                elif choice==3:
##                        print("Multiplication:- ", mul(number1,number2))
##                elif choice==4:
##                        print("Division:- ", div(number1,number2))
##
##                elif choice==5:
##                        print("All Operation:- ", allop(number1,number2))
##                menus()        
##                break
