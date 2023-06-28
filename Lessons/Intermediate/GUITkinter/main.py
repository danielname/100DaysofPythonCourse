import tkinter

window = tkinter.Tk()
# characteristic parameters
window.title("First GUI Program")
window.minsize(width=450, height=300)

# Labels
my_label = tkinter.Label(text="I am a label", font=("Arial", 12, "normal"))
my_label.pack()











# mainloop must exist at the end of main
window.mainloop()
