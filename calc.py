import tkinter as tk
from func import d, div, mult, add, sub, check, sqr, sqrroot, c2

giu_face = tk.Tk()
giu_face.title("Calculator")

calc13 = []


def mat():
    c = check(calc13)
    if c2(calc13) == "1":
        try:
            for _ in range(len(calc13[0])):
                if c == False:
                    calc0 = sqrroot(calc13)
                    calc1 = sqr(calc0)
                    calc2 = div(calc1)
                    calc3 = mult(calc2)
                    calc4 = add(calc3)
                    calc5 = sub(calc4)
                elif c == True:
                    calc0 = sqrroot(calc13)
                    calc1 = sqr(calc0)
                    calc2 = div(calc1)
                    calc3 = mult(calc2)
                    calc4 = add(calc3)
                    calc5 = sub(calc4)
            return calc5
        except:
            return "0"
    # - -
    elif c2(calc13) == "0":
        dis1 = tk.Label(giu_face, text="                                       Invalid Input", font="lucida 25 bold")
        dis1.grid(row=3, column=0, columnspan=4)
        calc13.clear()
        return "0"


def display(c):
    dis1 = tk.Label(giu_face, text=d(c), font="lucida 25 bold")
    dis1.grid(row=3, column=0, columnspan=4)


def equal():
    calc0 = mat()
    if calc0 != "0":
        display(calc0)


def one():
    calc13.append("1")
    display(calc13)


def two():
    calc13.append("2")
    display(calc13)


def three():
    calc13.append("3")
    display(calc13)


def four():
    calc13.append("4")
    display(calc13)


def five():
    calc13.append("5")
    display(calc13)


def six():
    calc13.append("6")
    display(calc13)


def seven():
    calc13.append("7")
    display(calc13)


def eight():
    calc13.append("8")
    display(calc13)


def nine():
    calc13.append("9")
    display(calc13)


def zero():
    calc13.append("0")
    display(calc13)


def minus():
    calc13.append("-")
    display(calc13)


def plus():
    calc13.append("+")
    display(calc13)


def clearall():
    calc13.clear()
    display(calc13)


def clear():
    try:
        calc13.pop(len(calc13) - 1)
    except:
        pass
    display(calc13)


def square():
    calc13.append("^")
    display(calc13)


def multiply():
    calc13.append("×")
    display(calc13)


def divide():
    calc13.append("÷")
    display(calc13)


def squrroot():
    calc13.append("²√")
    display(calc13)


def dot():
    calc13.append(".")
    display(calc13)


display(calc13)
bton1 = tk.Button(giu_face, text='   1    ', font="lucida 20 bold", command=one)
bton1.grid(row=7, column=0, ipady=4, ipadx=20)
bton2 = tk.Button(giu_face, text='   4    ', font="lucida 20 bold", command=four)
bton2.grid(row=6, column=0, ipady=4, ipadx=20)
bton3 = tk.Button(giu_face, text='   7    ', font="lucida 20 bold", command=seven)
bton3.grid(row=5, column=0, ipady=4, ipadx=20)
bton4 = tk.Button(giu_face, text='   ⌫  ', font="lucida 20 bold", command=clear)
bton4.grid(row=4, column=3, ipady=4, ipadx=20)
bton5 = tk.Button(giu_face, text='   nˣ   ', font="lucida 20 bold", command=square)
bton5.grid(row=4, column=1, ipady=4, ipadx=20)
bton6 = tk.Button(giu_face, text='    2   ', font="lucida 20 bold", command=two)
bton6.grid(row=7, column=1, ipady=4, ipadx=20)
bton8 = tk.Button(giu_face, text='   5    ', font="lucida 20 bold", command=five)
bton8.grid(row=6, column=1, ipady=4, ipadx=20)
bton9 = tk.Button(giu_face, text='   8    ', font="lucida 20 bold", command=eight)
bton9.grid(row=5, column=1, ipady=4, ipadx=22)
bton0 = tk.Button(giu_face, text='    C    ', font="lucida 20 bold", command=clearall)
bton0.grid(row=4, column=2, ipady=4, ipadx=20)
bton10 = tk.Button(giu_face, text='   0    ', font="lucida 20 bold", command=zero)
bton10.grid(row=8, column=1, ipady=4, ipadx=20)
bton11 = tk.Button(giu_face, text='    3     ', font="lucida 20 bold", command=three)
bton11.grid(row=7, column=2, ipady=4, ipadx=20)
bton12 = tk.Button(giu_face, text='     6    ', font="lucida 20 bold", command=six)
bton12.grid(row=6, column=2, ipady=4, ipadx=20)
bton13 = tk.Button(giu_face, text='    9     ', font="lucida 20 bold", command=nine)
bton13.grid(row=5, column=2, ipady=4, ipadx=20)
bton14 = tk.Button(giu_face, text='   ²√   ', font="lucida 20 bold", command=squrroot)
bton14.grid(row=4, column=0, ipady=4, ipadx=20)
bton15 = tk.Button(giu_face, text='    =     ', font="lucida 20 bold", command=equal)
bton15.grid(row=8, column=2, ipady=4, ipadx=20)
bton16 = tk.Button(giu_face, text='     -    ', font="lucida 20 bold", command=minus)
bton16.grid(row=7, column=3, ipady=4, ipadx=20)
bton17 = tk.Button(giu_face, text='    x    ', font="lucida 20 bold", command=multiply)
bton17.grid(row=6, column=3, ipady=4, ipadx=20)
bton18 = tk.Button(giu_face, text='    ÷    ', font="lucida 20 bold", command=divide)
bton18.grid(row=5, column=3, ipady=4, ipadx=20)
bton19 = tk.Button(giu_face, text='    +    ', font="lucida 20 bold", command=plus)
bton19.grid(row=8, column=3, ipady=4, ipadx=20)
bton20 = tk.Button(giu_face, text='    .    ', font="lucida 20 bold", command=dot)
bton20.grid(row=8, column=0, ipady=4, ipadx=20)
giu_face.mainloop()
