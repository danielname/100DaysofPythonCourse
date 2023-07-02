from tkinter import *

window = Tk()
window.title("Grid Challenge")
window.minsize(width=500, height=500)

# label at 0,0
my_label = Label(text="On top left", padx=20, pady=50)
my_label.grid(column=0, row=0)

# button at 1,1
first_button = Button(text="down right from label", padx=20, pady=50)
first_button.grid(column=1, row=1)

# button at 2,0
second_button = Button(text="up right from button", padx=20, pady=50)
second_button.grid(column=2, row=0)


# entry at 3,2
my_entry = Entry()
my_entry.grid(column=3, row=2)

window.mainloop()
