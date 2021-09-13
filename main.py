from tkinter import *
from tkinter.ttk import *
expression = ""
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")
 
 

if __name__ == "__main__":

    gui = Tk()
    gui.configure(background="light green")
    gui.title("Simple Calculator")
    gui.geometry("420x250")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation, font=("arial","23"))
    expression_field.grid(columnspan=7,ipadx=34,ipady= 10)
    style = Style()
    style.configure('W.TButton',width=8, font=("arial","15","bold"))


    button1 = Button(gui, text=' 1 ', style = 'W.TButton',command=lambda: press(1))
    button1.grid(row=2, column=0)
 
    button2 = Button(gui, text=' 2 ',style = 'W.TButton',command=lambda: press(2))
    button2.grid(row=2, column=1)
 
    button3 = Button(gui, text=' 3 ',style = 'W.TButton',command=lambda: press(3))
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text=' 4 ', style = 'W.TButton',command=lambda: press(4))
    button4.grid(row=3, column=0)
 
    button5 = Button(gui, text=' 5 ',      style = 'W.TButton',command=lambda: press(5))
    button5.grid(row=3, column=1)
 
    button6 = Button(gui, text=' 6 ',style = 'W.TButton',command=lambda: press(6))
    button6.grid(row=3, column=2)
 
    button7 = Button(gui, text=' 7 ',style = 'W.TButton',command=lambda: press(7))
    button7.grid(row=4, column=0)
 
    button8 = Button(gui, text=' 8 ', style = 'W.TButton',command=lambda: press(8))
    button8.grid(row=4, column=1)
 
    button9 = Button(gui, text=' 9 ',style = 'W.TButton',command=lambda: press(9))
    button9.grid(row=4, column=2)
 
    button0 = Button(gui, text=' 0 ',style = 'W.TButton',command=lambda: press(0))
    button0.grid(row=5, column=0)
 
    plus = Button(gui, text=' + ',  style = 'W.TButton',command=lambda: press("+"))
    plus.grid(row=2, column=3)
 
    minus = Button(gui, text=' - ',  style = 'W.TButton',command=lambda: press("-"))
    minus.grid(row=3, column=3)
 
    multiply = Button(gui, text=' * ',style = 'W.TButton',command=lambda: press("*"))
    multiply.grid(row=4, column=3)
 
    divide = Button(gui, text=' / ',style = 'W.TButton',command=lambda: press("/"))
    divide.grid(row=5, column=3)
 
    equal = Button(gui, text=' = ', style = 'W.TButton',command=equalpress)
    equal.grid(row=5, column=2)
 
    clear = Button(gui, text='Clear',  style = 'W.TButton',command=clear)
    clear.grid(row=5, column='1')
 
    Decimal= Button(gui, text='.',style = 'W.TButton',command=lambda: press('.'))
    Decimal.grid(row=6, column=0)

    gui.mainloop()