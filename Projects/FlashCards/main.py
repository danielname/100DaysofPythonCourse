from tkinter import *
from tkinter import messagebox
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"

#---------------next word-------------------#


#----------------card flip------------------#


#------------------add to list (wrong)------#


#---------------------UI--------------------#
window = Tk()
window.title("Learn French")
window.config(width=650, height=400)

front_canvas = Canvas(width=650, height=400, highlightthickness=0)
front_image = PhotoImage(file="../FlashCards/images/card_front.png")
front_canvas.create_image(650, 400, image=front_image)
front_canvas.grid(row=0, column=0)

title = Label(text="something", justify="center")
title.grid(row=1, column=1)

word = Label(text="something else", justify="center")
word.grid(row=2, column=1)

window.mainloop()
