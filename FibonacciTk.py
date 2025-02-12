from tkinter import *


def PrintFibonacci():

    Amount = int(Limit.get())

    x = 0
    y = 1

    print(x)
    print(y)

    print("Fibonacci".center(80, "-"))

    for N in range(Amount):
        Fib = x + y
        x = y
        y = Fib
        print(Fib)
    print("\n")


Window = Tk()

Window.title("Fibonacci (TKinter)")

Icon = PhotoImage(file="FibonacciStatue.png")
Window.iconphoto(True, Icon )

LimitSign = Label(Window, text="Enter how many fibonacci numbers you would like: ", font=("Arial", 20))
LimitSign.pack(side=LEFT)
Limit = Entry(Window, font=("Arial", 20))
Limit.pack(side=LEFT)

Submit = Button(Window, text="Submit", font=("Arial", 20), command=PrintFibonacci)
Submit.pack(side=RIGHT)

Window.mainloop()

