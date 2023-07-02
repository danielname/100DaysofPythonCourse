from tkinter import *

window = Tk()
window.title("Grid Challenge")
window.minsize(width=500, height=500)

# label at 1,1
my_label = Label(text="On top left")
my_label.grid(column=1, row=1)

# button at 2,2
first_button = Button(text="down right from label")
first_button.grid(column=2, row=2)

# button at 3,1
second_button = Button(text="up right from button")
second_button.grid(column=3, row=1)


# entry at 4,3
my_entry = Entry()
my_entry.grid(column=4, row=3)

window.mainloop()