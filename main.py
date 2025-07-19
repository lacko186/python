from tkinter import *

app = Tk()

app.geometry("400x400")
app.title('hello')

label = Label(app, text="hello world", font="Arial 40 bold")
btn = Button(app, text="click", width=10, command="submit")


label.pack(pady=100)
btn.pack()
app.mainloop()