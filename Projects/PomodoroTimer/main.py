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
def start_timer():
    countdown(1500)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    formatted_count = str(count // 60) + ":" + str(count % 60)
    canvas.itemconfig(timer_text, text=formatted_count)
    if count > 0:
        window.after(1000, countdown, count - 1)





def reset_timer():
    pass


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(pady=50, padx=100, bg=BLUE)

timer_label = Label(text="Timer", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=BLUE)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=BLUE, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_space = Label(text="", bg=BLUE, fg=GREEN)
check_space.grid(column=1, row=3)



window.mainloop()
