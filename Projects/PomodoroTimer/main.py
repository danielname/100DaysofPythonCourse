from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
BLUE = "#00235b"
RED = "#e21818"
GREEN = "#98dfd6"
YELLOW = "#ffdd83"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(pady=50, padx=100, bg=BLUE)

canvas = Canvas(width=200, height=224, bg=BLUE, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()


window.mainloop()
