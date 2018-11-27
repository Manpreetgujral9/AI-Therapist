import os
from tkinter import *
from PIL import Image

root = Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.geometry("%dx%d" % (width, height))
root.title('Mood Booster')
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen', True)
root.configure(background='lavender')

def open_home():
    os.system('Gui1.py')
lb = Label(root, text='\n\n\nUnderstanding the life leads to happiness!\nHave a look to the quotes, and you\'ll'
                      ' be lighter...', font='Cambria 25 bold', bg='lavender')
lb.pack()

but13 = Button(root, text='Quit', command=root.quit, height=2, width=8,bg="lavender")
but13.pack(side=BOTTOM, pady=42)

but14 = Button(root, text='Home Page', command=open_home, height=3, width=18,bg="lavender")
but14.pack(side=BOTTOM, pady=82)

def action1():
    image = Image.open('a.png')
    image.show()

def action2():
    image = Image.open('b.png')
    image.show()

def action3():
    image = Image.open('c.png')
    image.show()

def action4():
    image = Image.open('d.png')
    image.show()

def action5():
    image = Image.open('e.png')
    image.show()

def action6():
    image = Image.open('f.png')
    image.show()

def action7():
    image = Image.open('g.png')
    image.show()

def action8():
    image = Image.open('h.png')
    image.show()

def action9():
    image = Image.open('i.png')
    image.show()

def action10():
    image = Image.open('j.png')
    image.show()

def action11():
    image = Image.open('k.png')
    image.show()

def action12():
    image = Image.open('l.png')
    image.show()



imag1 = PhotoImage(file='1.png')
but1 = Button(root, image=imag1, width=100, height=100, command=action1)
but1.pack(side=LEFT, padx=4)

imag2 = PhotoImage(file='2.png')
but2 = Button(root, image=imag2, width=100, height=100, command=action2)
but2.pack(side=LEFT, padx=4)

imag3 = PhotoImage(file='3.png')
but3 = Button(root, image=imag3, width=100, height=100, command=action3)
but3.pack(side=LEFT, padx=4)

imag4 = PhotoImage(file='4.png')
but4 = Button(root, image=imag4, width=100, height=100, command=action4)
but4.pack(side=RIGHT, padx=4)

imag5 = PhotoImage(file='5.png')
but5 = Button(root, image=imag5, width=100, height=100, command=action5)
but5.pack(side=RIGHT, padx=4)

imag6 = PhotoImage(file="6.png")
but6 = Button(root, image=imag6, width=100, height=100, command=action6)
but6.pack(side=RIGHT, padx=4)

imag7 = PhotoImage(file='7.png')
but7 = Button(root, image=imag7, width=100, height=100, command=action7)
but7.pack(side=LEFT, padx=4)

imag8 = PhotoImage(file='8.png')
but8 = Button(root, image=imag8, width=100, height=100, command=action8)
but8.pack(side=LEFT, padx=4)

imag9 = PhotoImage(file='9.png')
but9 = Button(root, image=imag9, width=100, height=100, command=action9)
but9.pack(side=LEFT, padx=4)

imag10 = PhotoImage(file='10.png')
but10 = Button(root, image=imag10, width=100, height=100, command=action10)
but10.pack(side=RIGHT, padx=4)

imag11 = PhotoImage(file='11.png')
but11 = Button(root, image=imag11, width=100, height=100, command=action11)
but11.pack(side=RIGHT, padx=4)

imag12 = PhotoImage(file="12.png")
but12 = Button(root, image=imag12, width=100, height=100, command=action12)
but12.pack(side=RIGHT, padx=4)




root.mainloop()