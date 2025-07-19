from tkinter import *

app = Tk()

app.geometry("400x400")
app.title('hello')

# Initialize counter
counter = 0

def on_button_click():
    """
    This function is called when the button is clicked.
    It updates the label text based on the counter.
    """
    global counter  # Declare counter as global to modify it

    if counter % 2 == 0:
        label.config(text="changed") # Use .config to update widget properties
    else:
        label.config(text="hello world")

    counter += 1 # Increment counter after each click

label = Label(app, text="hello world", font="Arial 40 bold")
btn = Button(app, text="click", width=10, command=on_button_click) # Assign the function to command

label.pack(pady=100)
btn.pack()

app.mainloop()