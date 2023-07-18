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
lock_canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1, columnspan=2, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(column=1, columnspan=2, row=2)

pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)

pw_input = Entry(width=21)
pw_input.grid(column=1, row=3)

pw_button = Button(text="Generate Password")
pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()
