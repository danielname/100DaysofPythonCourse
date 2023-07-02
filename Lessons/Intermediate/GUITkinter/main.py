import tkinter

window = tkinter.Tk()
# characteristic parameters
window.title("First GUI Program")
window.minsize(width=450, height=300)

# Labels
my_label = tkinter.Label(text="I am a label", font=("Arial", 12, "normal"))
my_label.pack(side="left")

# my_label["text"] = "Not a label"
my_label.config(text="Not a label")


def button_clicked():
    my_label.config(text=my_input.get())

button = tkinter.Button(text="Click me", command=button_clicked)
button.pack(side="right")


my_input = tkinter.Entry(width=10)
my_input.place(x=0, y=0)




# mainloop must exist at the end of main
window.mainloop()
