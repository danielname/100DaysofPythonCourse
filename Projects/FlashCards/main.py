from tkinter import *
from tkinter import messagebox
from random import randint, choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("/data/french_words.csv")
word_dict = data.to_dict()

french_word_list = [key for (key, value) in word_dict]
keys_in_order = []
for word_index in range(len(french_word_list)):
    ran_index = randint(0, len(french_word_list) - 1)
    keys_in_order.append(french_word_list[ran_index])
    french_word_list.pop(ran_index)

with open("./images/card_front.png") as file:
    FRONT_BACKGROUND_IMAGE = file.read()

#---------------next word-------------------#
def next_word():
    pass

#----------------card flip------------------#
def card_flip():
    pass

#------------------add to list (wrong)------#
def wrong_answer():
    next_word()

#------------------right answer-------------#
def right_answer():
    next_word()

#-----------------------timer_______________#
def timer():
    #if timer not 0, timer -1
    #else
    card_flip()

#---------------------UI--------------------#
window = Tk()
window.title("Learn French")
window.config(width=650, height=400)

background_image = PhotoImage(...)
background_label = Label(image=FRONT_BACKGROUND_IMAGE) #i think the problem here is that i have written the filepath, but I need an image, so the first step is to get the image from the file
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# front_canvas = Canvas(width=650, height=400, highlightthickness=0)
# front_image = PhotoImage(file=)
# front_canvas.create_image(650, 400, image=front_image)
# front_canvas.grid(row=0, column=0)

title = Label(text="something", justify="center")
title.grid(row=1, column=1)

word = Label(text="something else", justify="center")
word.grid(row=2, column=1)

right_canvas = Canvas(width=100, height=100, highlightthickness=0)
right_image = PhotoImage(file="images/right.png")
right_canvas.create_image(100, 100, image=right_image)


wrong_canvas = Canvas(width=100, height=100, highlightthickness=0)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_canvas.create_image(100, 100, image=wrong_image)


#need to make the images buttons in order to use commands
correct_button = Button(image=right_image, command=right_answer)
correct_button.grid(row=3, column=0)

incorrect_button = Button(image=wrong_image, command=wrong_answer)
incorrect_button.grid(row=3, column=2)

window.mainloop()
