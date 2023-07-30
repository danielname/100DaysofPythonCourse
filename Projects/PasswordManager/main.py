from tkinter import *
import pandas

try:
    data = pandas.read_csv("password_list.csv")
    password_dict = data.to_dict() #{
#     "website": [web_text],
#     "email": [email_text],
#     "password": [pw_text]
# }
except:
    with open("password_list.csv", mode="w") as file:
        file.write("website,email,password")
    data = pandas.read_csv("password_list.csv")
    password_dict = data.to_dict()

print(password_dict)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_press():
    web_text = website_input.get()
    email_text = email_input.get()
    pw_text = pw_input.get()

    # make dataframe
    password_dict["website"][len(password_dict["website"])] = web_text #this mostly works. It seems there is an unnamed column being built every iteration.
    password_dict["email"][len(password_dict["email"])] = email_text
    password_dict["password"][len(password_dict["password"])] = pw_text

    password_csv = pandas.DataFrame(password_dict)
    password_csv.to_csv("password_list.csv")

    # need to make and append info to txt file


    # need to clear all input sections
    website_input.delete(0,len(website_input.get()))
    email_input.delete(0,len(email_input.get()))
    pw_input.delete(0,len(pw_input.get()))

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

pw_button = Button(text="Generate Password", justify="left")
pw_button.config(padx=0)
pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add_press)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()
