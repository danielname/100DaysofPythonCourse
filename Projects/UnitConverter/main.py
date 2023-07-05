from tkinter import *

MI_TO_KM = 1.609344


def calculate():
    conversion.config(text=str(float(num_box.get()) * MI_TO_KM))

def radio_used():
#     config all the things

window = Tk()
window.config(padx=20, pady=20)
window.minsize(width=300, height=200)

radio_state = IntVar()
conv_select = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)

unit_1 = Label(text="Miles")
unit_1.grid(column=2, row=0)

unit_2 = Label(text="Km")
unit_2.grid(column=2, row=1)

saying = Label(text="is equal to")
saying.grid(column=0, row=1)

conversion = Label(text="0")
conversion.grid(column=1, row=1)

num_box = Entry()
num_box.grid(column=1, row=0)

calc_btn = Button(text="Calculate", command=calculate)
calc_btn.grid(column=1, row=2)





window.mainloop()
