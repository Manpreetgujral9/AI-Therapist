from tkinter import *
import os


root = Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.geometry("%dx%d" % (width, height))
root.title('AI Therapist')
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen', True)
root.configure(background='lavender')

def open_moodbooster():
    os.system('Gui2.py')

def open_Diseasepredictor():
    os.system('Data_Analysis.py')
label = Label(root, text="\nAI THERAPIST", font='Cambria 50 bold', bg="lavender")
label.pack()

label2 = Label(root, text='\n\nWelcome to the AI Therapist! We help you in boosting your mood in case you feel low,'
                         ' and predicting the disease\n\n you might be suffering from. So, buck up! And seek the help.',
            font='Cambria 15', bg='lavender')
label2.pack()

but13 = Button(root, text='Quit', command=root.quit, height=2, width=8,bg='lavender')
but13.pack(side=BOTTOM, pady=42)
button1 = Button(text='Mood Booster', bg='lavender', width=30, height=3, command=open_moodbooster)
button1.config(font=('Cambria', 15, 'bold'))
button1.place(x=width/5.5, y=height/2)

button2 = Button(text='Disease Predictor', bg='lavender', width=30, height=3, command=open_Diseasepredictor)
button2.config(font=('Cambria', 15, 'bold'))
button2.place(x=width/1.8, y=height/2)

root.mainloop()