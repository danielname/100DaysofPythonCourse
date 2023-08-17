import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pw():
    lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
    upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
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
    new_data = {
        web_text: {
            "email": email_text,
            "password": pw_text
        }
    }

    if web_text != "" and email_text != "" and pw_text != "":
        is_ok = messagebox.askokcancel(title=web_text, message=f"The details entered are:\nEmail: {email_text}"
                                                               f"\nPassword: {pw_text}\nIs it ok to save?")
        if is_ok:
            try:
                with open("password_list.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
                    # Updating old data with new data
                    data.update(new_data)
            except:
                data = new_data
            finally:
                with open("password_list.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)

            # need to clear all input sections
            website_input.delete(0, END)
            email_input.delete(0, END)
            pw_input.delete(0, END)
    else:
        messagebox.showerror(title="Error: Empty Field", message="Please don't leave any fields empty")


# ---------------------------- PASSWORD LOOKUP ------------------------------- #
def search():
    data = {}
    try:
        with open("password_list.json", "r") as data_file:
            data = json.load(data_file)
            email_input.insert(0, data[website_input.get()]["email"])
            pw_input.insert(0, data[website_input.get()]["password"])
    except FileNotFoundError:
        messagebox.showerror(title="Error: No Passwords!", message="Silly goose, you don't have passwords yet!")
    except KeyError:
        messagebox.showerror(title="Error: No Passwords For Site!", message="You dont have a passeword for that "
                                                                            "website yet.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, width=240, height=240)

lock_canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
lock_canvas.create_image(100, 100, image=lock_image)
lock_canvas.grid(column=1, row=0)

website_label = Label(text="Website:", justify="right")
website_label.grid(column=0, row=1)

website_input = Entry(width=35, justify="left")
website_input.grid(column=1, row=1)
website_input.focus()

search_button = Button(text="Search", justify="left", command=search)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:", justify="right")
email_label.grid(column=0, row=2)

email_input = Entry(width=35, justify="left")
email_input.grid(column=1, columnspan=2, row=2)
email_input.insert(0, "myemail@email.com")

pw_label = Label(text="Password:", justify="right")
pw_label.grid(column=0, row=3)

pw_input = Entry(width=21, justify="left")
pw_input.grid(column=1, row=3)

pw_button = Button(text="Generate Password", justify="left", command=generate_pw)
pw_button.config(padx=0)
pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()
