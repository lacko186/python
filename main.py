from tkinter import *

app = Tk()

app.geometry("400x400")
app.title('hello')

szamlalo = 0

def on_button_click():
    global szamlalo  

    if szamlalo % 2 == 0:
        label.config(text="changed") 
    else:
        label.config(text="hello world")

    szamlalo += 1 

label = Label(app, text="hello world", font="Arial 40 bold")
btn = Button(app, text="click", width=10, command=on_button_click)

label.pack(pady=100)
btn.pack()

app.mainloop()