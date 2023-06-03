from tkinter import *
from math import floor, ceil

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""


def timer_reset():
    global reps
    window.after_cancel(timer)
    title_label.config(text="Pomodoro")
    canvas.itemconfig(timer_text, text="00.00")
    check_label.config(text="")
    reps = 0


def start_timer():
    start_button.config(state=DISABLED)
    global reps
    reps += 1
    if reps % 8 == 0:
        title_label.config(text="Long Break")
        countdown(LONG_BREAK_MIN*60)

    elif reps % 2 == 0:
        title_label.config(text="Short Break")
        countdown(SHORT_BREAK_MIN*60)
    elif reps == 9:
        reps = 1
        countdown(WORK_MIN*60)
    else:
        title_label.config(text="Work")
        countdown(WORK_MIN*60)


def countdown(count):

    count_second_text = count % 60
    count_minutes_text = count / 60
    count_minutes_text = floor(count_minutes_text)
    if count_second_text < 10:
        count_second_text = f"0{count_second_text}"
    if count_minutes_text < 10:
        count_minutes_text = f"0{count_minutes_text}"

    canvas.itemconfig(timer_text, text=f"{count_minutes_text}.{count_second_text}")
    if count > 0:
        global timer
        timer = window.after(3000, countdown, count-1)
    else:
        marks = ""
        work_sessions = ceil(reps / 2)
        for n in range(work_sessions):
            marks += "✔"
        print(marks)
        check_label.config(text=marks)
        start_timer()


window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.geometry("500x500")
window.resizable(False, False)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00.00", fill="white", font=(FONT_NAME, 35, "bold"))


title_label = Label(text="Pomodoro", font=(FONT_NAME, 35, "bold"), fg=GREEN, highlightthickness=0, bg=YELLOW)
title_label.grid(row=0, column=3)
canvas.grid(row=1, column=3)
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0,)
reset_button = Button(text="Reset", command=timer_reset)
reset_button.grid(row=2, column=6)
check_label = Label(text="", font=(FONT_NAME, 20, "bold"), fg=GREEN, highlightthickness=0, bg=YELLOW)
check_label.grid(row=3, column=3)

window.mainloop()

"✔"
