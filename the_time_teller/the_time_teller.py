from tkinter import *
from time import *

window = Tk()
window.title("The Time Teller")


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    time_label.after(1000, update)


time_label = Label(window, font=("Arial", 50), fg="orange", bg="blue")
day_label = Label(window, font=("Ink Free", 25), fg="blue")
date_label = Label(window, font=("Ink Free", 30), fg="orange")

update()

time_label.pack()
day_label.pack()
date_label.pack()
window.mainloop()