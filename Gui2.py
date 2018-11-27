import os
from tkinter import *
from tkinter import messagebox

from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sub():
    f = e.get()
    print(f)

    scores = sid.polarity_scores(f)

    # for key in sorted(scores):
    # print('{0}: {1}, \n'.format(key, scores[key]), end='')

    if "compound" in scores:
        c = scores["compound"]

    if "neg" in scores:
        n = scores["neg"]

    if "neu" in scores:
        nu = scores["neu"]

    if "pos" in scores:
        ps = scores["pos"]

    # print(c,n,nu,ps)`
    if (c < 0):
        b = "a"
    if (n > ps and b == "a"):
        messagebox.showinfo("You are feeling sad", "But here we are to help you")
        os.system('Gui3.py')
    elif (nu > n and nu > ps):
        messagebox.showinfo("", "You are feeling happy but also sad")
        os.system('Gui3.py')

    else:
        messagebox.showinfo("Congratulations!!!", "You are feeling happy :)")

def negative():
    print("Hello")



sid = SentimentIntensityAnalyzer()


root = Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.geometry("%dx%d" % (width, height))
root.title('Mood Booster')
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen', True)
root.configure(background='lavender')

but13 = Button(root, text='Quit', command=root.quit, height=2, width=8,bg="lavender")
but13.pack(side=BOTTOM, pady=42)
lb = Label(root, text='\nMOOD BOOSTER', bg="lavender", font=('Cambria 50 bold'))
lb.pack()
lb.place(x=width/3, y=20)

lb2 = Label(root, text='How are you feeling?', bg='lavender', font=('Cambria', 15, 'normal'))
lb2.pack()
lb2.place(x=width/10, y=height/3)

e=StringVar()
e1 = Entry(root, font=('Cambria', 15, 'normal'), width=100,textvariable=e)
e1.pack()
e1.place(x=width/10, y=height/2.6)

but = Button(root, text='Submit', font=('Cambria', 15, 'normal'), bg='lavender', width=7, height=1,command=sub)
but.pack()
but.place(x=width/10, y=height/2.3)

root.mainloop()