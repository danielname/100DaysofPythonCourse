from tkinter import *

MI_TO_KM = 1.609344
KM_TO_MI = 0.62137119


def calculate_km_mi():
    conversion.config(text=str(float(num_box.get()) * MI_TO_KM))

def calculate_mi_km():
    conversion.config(text=str(float(num_box.get()) * KM_TO_MI))

def radio_used_1():
    unit_1.config(text="Miles")
    unit_2.config(text="Km")
    conversion.config(text="0")
    calc_btn.config(command=calculate_km_mi)

def radio_used_2():
    unit_1.config(text="Km")
    unit_2.config(text="Miles")
    conversion.config(text="0")
    calc_btn.config(command=calculate_mi_km)

window = Tk()
window.config(padx=20, pady=20)
window.minsize(width=300, height=200)

radio_state = IntVar()
mi_km_select = Radiobutton(text="mi to km", value=1, variable=radio_state, command=radio_used_1)
km_mi_select = Radiobutton(text="km to mi", value=2, variable=radio_state, command=radio_used_2)
mi_km_select.grid(column=3, row=0)
km_mi_select.grid(column=3, row=1)

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

calc_btn = Button(text="Calculate", command=calculate_km_mi)
calc_btn.grid(column=1, row=2)





window.mainloop()
