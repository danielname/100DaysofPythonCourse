from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20, width=240, height=240)

lock_canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
lock_canvas.create_image(100, 100, image=lock_image)
lock_canvas.grid(column=0, row=0)

website_label = Label()
website_input = Entry()

email_label = Label()
email_input = Entry()

pw_label = Label()
pw_input = Entry()
pw_button = Button()

add_button = Button()

window.mainloop()
