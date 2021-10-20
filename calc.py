import tkinter as tk
from func import d2, d1, d3, d4, div, mult, add, sub, check, sqr, sqrroot

giu_face = tk.Tk()
giu_face.title("Calculator")


calc132 = []

def mat():
    c=check(calc132)
    for _ in range(len(calc132)):
        if c==False:
            calc0 = sqrroot(calc132)
            calc1 = sqr(calc0)
            calc2 = div(calc1)
            calc3 = mult(calc2)
            calc4 = add(calc3)
            calc5 = sub(calc4)
        elif c==True:
            calc0 = sqrroot(calc132)
            calc1 = sqr(calc0)
            calc2 = div(calc1)
            calc3 = mult(calc2)
            calc4 = add(calc3)
            calc5 = sub(calc4)
            return calc5



def display():
    dis1 = tk.Label(giu_face, text=d1(calc132), font="lucida 20 bold")
    dis1.grid(row=3, column=3)
    dis2 = tk.Label(giu_face, text=d2(calc132), font="lucida 20 bold")
    dis2.grid(row=3, column=2)
    dis2 = tk.Label(giu_face, text=d3(calc132), font="lucida 20 bold")
    dis2.grid(row=3, column=1)
    dis2 = tk.Label(giu_face, text=d4(calc132), font="lucida 20 bold")
    dis2.grid(row=3, column=0)


def equal():
    calc0 = mat()
    display()


def one():
    calc132.append("1")
    display()


def two():
    calc132.append("2")
    display()


def three():
    calc132.append("3")
    display()


def four():
    calc132.append("4")
    display()


def five():
    calc132.append("5")
    display()


def six():
    calc132.append("6")
    display()


def seven():
    calc132.append("7")
    display()


def eight():
    calc132.append("8")
    display()


def nine():
    calc132.append("9")
    display()


def zero():
    calc132.append("0")
    display()


def minus():
    calc132.append("-")
    display()


def plus():
    calc132.append("+")
    display()


def clearall():
    calc132.clear()
    display()


def clear():
    try:
        calc132.pop(len(calc132) - 1)
    except:
        pass
    display()


def square():
    calc132.append("^")
    display()


def multiply():
    calc132.append("×")
    display()


def divide():
    calc132.append("÷")
    display()

def squrroot():
    calc132.append("²√")
    display()

def twozero():
    for _ in range(2):
        zero()
    display()


display()
bton1 = tk.Button(giu_face, text=' 1  ', font="lucida 20 bold", command=one)
bton1.grid(row=7, column=0, ipady=4, ipadx=20)
bton2 = tk.Button(giu_face, text=' 4  ', font="lucida 20 bold", command=four)
bton2.grid(row=6, column=0, ipady=4, ipadx=20)
bton3 = tk.Button(giu_face, text=' 7  ', font="lucida 20 bold", command=seven)
bton3.grid(row=5, column=0, ipady=4, ipadx=20)
bton4 = tk.Button(giu_face, text=' ⌫', font="lucida 20 bold", command=clear)
bton4.grid(row=4, column=3, ipady=4, ipadx=20)
bton5 = tk.Button(giu_face, text=' nˣ ', font="lucida 20 bold", command=square)
bton5.grid(row=4, column=1, ipady=4, ipadx=20)
bton6 = tk.Button(giu_face, text='  2 ', font="lucida 20 bold", command=two)
bton6.grid(row=7, column=1, ipady=4, ipadx=20)
bton8 = tk.Button(giu_face, text=' 5  ', font="lucida 20 bold", command=five)
bton8.grid(row=6, column=1, ipady=4, ipadx=20)
bton9 = tk.Button(giu_face, text=' 8  ', font="lucida 20 bold", command=eight)
bton9.grid(row=5, column=1, ipady=4, ipadx=22)
bton0 = tk.Button(giu_face, text=' C ', font="lucida 20 bold", command=clearall)
bton0.grid(row=4, column=2, ipady=4, ipadx=20)
bton10 = tk.Button(giu_face, text=' 0  ', font="lucida 20 bold", command=zero)
bton10.grid(row=8, column=1, ipady=4, ipadx=20)
bton11 = tk.Button(giu_face, text=' 3  ', font="lucida 20 bold", command=three)
bton11.grid(row=7, column=2, ipady=4, ipadx=20)
bton12 = tk.Button(giu_face, text='  6 ', font="lucida 20 bold", command=six)
bton12.grid(row=6, column=2, ipady=4, ipadx=20)
bton13 = tk.Button(giu_face, text=' 9  ', font="lucida 20 bold", command=nine)
bton13.grid(row=5, column=2, ipady=4, ipadx=20)
bton14 = tk.Button(giu_face, text=' ²√ ', font="lucida 20 bold",command=squrroot)
bton14.grid(row=4, column=0, ipady=4, ipadx=20)
bton15 = tk.Button(giu_face, text=' =  ', font="lucida 20 bold", command=equal)
bton15.grid(row=8, column=2, ipady=4, ipadx=20)
bton16 = tk.Button(giu_face, text='  -  ', font="lucida 20 bold", command=minus)
bton16.grid(row=7, column=3, ipady=4, ipadx=20)
bton17 = tk.Button(giu_face, text='  x ', font="lucida 20 bold", command=multiply)
bton17.grid(row=6, column=3, ipady=4, ipadx=20)
bton18 = tk.Button(giu_face, text='  /  ', font="lucida 20 bold", command=divide)
bton18.grid(row=5, column=3, ipady=4, ipadx=20)
bton19 = tk.Button(giu_face, text='  + ', font="lucida 20 bold", command=plus)
bton19.grid(row=8, column=3, ipady=4, ipadx=20)
bton20 = tk.Button(giu_face, text=' 00 ', font="lucida 20 bold", command=twozero)
bton20.grid(row=8, column=0, ipady=4, ipadx=20)
giu_face.mainloop()
