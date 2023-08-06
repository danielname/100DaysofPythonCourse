from tkinter import *
from tkinter import messagebox
import pandas
from random import choice, randint
import pyperclip

try:
    data = pandas.read_csv("password_list.csv")
    password_dict = data.to_dict()
except:
    with open("password_list.csv", mode="w") as file:
        file.write("website,email,password")
    data = pandas.read_csv("password_list.csv")
    password_dict = data.to_dict()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pw():
    lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    lo_letter_list = []
    up_letter_list = []
    sym_list = []
    num_list = []

    password_list = []

    for letter in range(4):
        lo_letter_list.append(choice(lower_letters))
    for letter in range(4):
        up_letter_list.append(choice(upper_letters))
    for symbol in range(2):
        sym_list.append(choice(symbols))
    for symbol in range(2):
        num_list.append(choice(numbers))

    lists = lo_letter_list
    lists.extend(up_letter_list)
    lists.extend(sym_list)
    lists.extend(num_list)
    for char in range(12):
        ran_index = randint(0, len(lists) - 1)
        password_list.append(lists[ran_index])
        lists.pop(ran_index)
    password = "".join(password_list)
    pw_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_text = website_input.get()
    email_text = email_input.get()
    pw_text = pw_input.get()

    if web_text != "" and email_text != "" and pw_text != "":
        is_ok = messagebox.askokcancel(title=web_text, message=f"The details entered are:\nEmail: {email_text}"
                                                       f"\nPassword: {pw_text}\nIs it ok to save?")
        if is_ok:
            # make dataframe
            password_dict["website"][len(password_dict["website"])] = web_text #this mostly works. It seems there is an unnamed column being built every iteration.
            password_dict["email"][len(password_dict["email"])] = email_text
            password_dict["password"][len(password_dict["password"])] = pw_text

            new_dict = {
                "website": password_dict["website"],
                "email": password_dict["email"],
                "password": password_dict["password"]
            }

            password_csv = pandas.DataFrame(new_dict)
            password_csv.to_csv("password_list.csv")

            # need to clear all input sections
            website_input.delete(0, END)
            email_input.delete(0, END)
            pw_input.delete(0, END)
    else:
        messagebox.showerror(title="Error: Empty Field", message="Please don't leave any fields empty")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, width=240, height=240)

lock_canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
lock_canvas.create_image(100, 100, image=lock_image)
lock_canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=35, justify="left")
website_input.grid(column=1, columnspan=2, row=1)
website_input.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = Entry(width=35, justify="left")
email_input.grid(column=1, columnspan=2, row=2)
email_input.insert(0, "myemail@email.com")

pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)

pw_input = Entry(width=21, justify="left")
pw_input.grid(column=1, row=3)

pw_button = Button(text="Generate Password", justify="left", command=generate_pw)
pw_button.config(padx=0)
pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()
