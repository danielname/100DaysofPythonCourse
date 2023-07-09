from tkinter import *

MI_TO_KM = 1.609344
KM_TO_MI = 0.62137119
GAL_TO_LIT = 3.78541178
LIT_TO_GAL = 0.26417205


def calculate_km_mi():
    conversion.config(text=str(float(num_box.get()) * MI_TO_KM))

def calculate_mi_km():
    conversion.config(text=str(float(num_box.get()) * KM_TO_MI))

def calculate_f_c():
    conversion.config(text=str((float(num_box.get()) - 32) * 5/9))

def calculate_c_f():
    conversion.config(text=str(float(num_box.get()) * 9/5 + 32))

def calculate_gal_lit():
    conversion.config(text=str(float(num_box.get()) * GAL_TO_LIT))

def calculate_lit_gal():
    conversion.config(text=str(float(num_box.get()) * LIT_TO_GAL))

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

def radio_used_3():
    unit_1.config(text="Fahrenheit")
    unit_2.config(text="Celsius")
    conversion.config(text="0")
    calc_btn.config(command=calculate_f_c)

def radio_used_4():
    unit_1.config(text="Celsius")
    unit_2.config(text="Fahrenheit")
    conversion.config(text="0")
    calc_btn.config(command=calculate_c_f)

def radio_used_5():
    unit_1.config(text="Gallons")
    unit_2.config(text="Liters")
    conversion.config(text="0")
    calc_btn.config(command=calculate_gal_lit)

def radio_used_6():
    unit_1.config(text="Liters")
    unit_2.config(text="Gallons")
    conversion.config(text="0")
    calc_btn.config(command=calculate_lit_gal)

window = Tk()
window.title("Unit Converter")
window.config(padx=20, pady=20)
window.minsize(width=300, height=200)

radio_state = IntVar()
mi_km_select = Radiobutton(text="mi to km", value=1, variable=radio_state, command=radio_used_1)
km_mi_select = Radiobutton(text="km to mi", value=2, variable=radio_state, command=radio_used_2)
f_c_select = Radiobutton(text="fahrenheit to celsius", value=3, variable=radio_state, command=radio_used_3)
c_f_select = Radiobutton(text="celsius to fahrenheit", value=4, variable=radio_state, command=radio_used_4)
gal_lit_select = Radiobutton(text="gallons to liters", value=5, variable=radio_state, command=radio_used_5)
lit_gal_select = Radiobutton(text="liters to gallons", value=6, variable=radio_state, command=radio_used_6)

mi_km_select.grid(column=3, row=0)
km_mi_select.grid(column=3, row=1)
f_c_select.grid(column=3, row=2)
c_f_select.grid(column=3, row=3)
gal_lit_select.grid(column=3, row=4)
lit_gal_select.grid(column=3, row=5)

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
