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


button = tkinter.Button(text="Click me")
button.pack(side="right")







# mainloop must exist at the end of main
window.mainloop()
