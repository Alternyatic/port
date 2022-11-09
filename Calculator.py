from tkinter import *
root = Tk()
root.title("Calculator")
root.resizable(0,0)

content = ""
txt_input = StringVar(value="0")

def btn(number):
    global content
    content = content+str(number)
    txt_input.set(content)

def equal():
    global content
    calculate = float(eval(content))
    txt_input.set(calculate)
    content = ""

def clear():
    global content
    content = ""
    txt_input.set("")
    display.insert(0,"0")
    
# แสดงผล 5 x 4
display = Entry(font=('open-sans',30),bg="white",textvariable=txt_input,justify="right")
display.grid(columnspan=4)


# row1
btn7 = Button(fg="white",bg="dimgrey",font=('Open Sans',20),text="7",command=lambda:btn(7),padx=38,pady=5).grid(row=1,column=0)
btn8 = Button(fg="white",bg="dimgrey",font=('Open Sans',20),text="8",command=lambda:btn(8),padx=35,pady=5).grid(row=1,column=1)
btn9 = Button(fg="white",bg="dimgrey",font=('Open Sans',20),text="9",command=lambda:btn(9),padx=40,pady=5).grid(row=1,column=2)
btnac = Button(fg="coral",bg="dimgrey",font=('Open Sans',20),text="AC",command=clear,padx=42,pady=5).grid(row=1,column=3)

# row2
btn4 = Button(fg="white",bg="dimgrey",font=('Open Sans',20),text="4",command=lambda:btn(4),padx=38,pady=5).grid(row=2,column=0)
btn5 = Button(fg="white",bg="dimgrey",font=('Open Sans',20),text="5",command=lambda:btn(5),padx=35,pady=5).grid(row=2,column=1)
btn6 = Button(fg="white",bg="dimgrey",font=('Open Sans',20),text="6",command=lambda:btn(6),padx=40,pady=5).grid(row=2,column=2)
btnplus = Button(fg="coral",bg="dimgrey",font=('Open Sans',20),command=lambda:btn("("),text="(",padx=55,pady=5).grid(row=2,column=3)

# row3
btn1 = Button(fg="white",bg="dimgrey",font=('Open Sans',20),text="1",command=lambda:btn(1),padx=38,pady=5).grid(row=3,column=0)
btn2 = Button(fg="white",bg="dimgrey",font=('Open Sans',20),text="2",command=lambda:btn(2),padx=35,pady=5).grid(row=3,column=1)
btn3 = Button(fg="white",bg="dimgrey",font=('Open Sans',20),text="3",command=lambda:btn(3),padx=40,pady=5).grid(row=3,column=2)
btnminus = Button(fg="coral",bg="dimgrey",font=('Open Sans',20),command=lambda:btn(")"),text=")",padx=55,pady=5).grid(row=3,column=3)

# row4
btn0 = Button(fg="white",bg="dimgrey",font=('Open Sans',20),command=lambda:btn("0"),text="0",padx=38,pady=5).grid(row=4,column=0)
btnpower = Button(fg="coral",bg="dimgrey",font=('Open Sans',20),command=lambda:btn("**"),text="^",padx=35,pady=5).grid(row=4,column=1)
btndivision = Button(fg="coral",bg="dimgrey",font=('Open Sans',20),command=lambda:btn("*"),text="*",padx=40,pady=5).grid(row=4,column=2)
btnmultiply = Button(fg="coral",bg="dimgrey",font=('Open Sans',20),command=lambda:btn("/"),text="/",padx=54,pady=5).grid(row=4,column=3)

# row5
btnequal = Button(fg="white",bg="deepskyblue",font=('Open Sans',20),text="=",command=equal,padx=38,pady=5).grid(row=5,column=0)
btndot = Button(fg="coral",bg="dimgrey",font=('Open Sans',20),text=".",command=lambda:btn("."),padx=39,pady=5).grid(row=5,column=1)
btnopen = Button(fg="coral",bg="dimgrey",font=('Open Sans',20),command=lambda:btn("+"),text="+",padx=40,pady=5).grid(row=5,column=2)
btnclose = Button(fg="coral",bg="dimgrey",font=('Open Sans',20),command=lambda:btn("-"),text="-",padx=55,pady=5).grid(row=5,column=3)
root.mainloop()