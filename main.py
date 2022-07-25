from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps%8==0:
     count_down(long_break_sec)
     timer.config(text="Breakkk",fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        timer.config(text="Breakkk", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Breakkk", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")

    # print(count)
    if(count>0):
        window.after(1000,count_down,count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.config(padx=100,pady=58,bg=YELLOW)
window.title("Pomodora")

timer=Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME,50))
timer.grid(column=1,row=1)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)

z=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=z)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=0)

# count_down(5)

button1=Button(text="Start",command=start_timer)
button1.grid(column=0,row=2)
button2=Button(text="Reset")
button2.grid(column=2,row=2)

check_mark=Label(text="✔",fg=GREEN, bg=YELLOW)
check_mark.grid(column=1,row=3)


window.mainloop()
