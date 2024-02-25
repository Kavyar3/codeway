import tkinter as tk
from tkinter import *

# Main window
screen = Tk()
screen.geometry("620x700")
screen.resizable(False, False)
screen['bg'] = '#FFFAF0'  # Ivory

# Function to add task
def add():
    job_text = JOB.get()
    if job_text:
        priority = PRIORITY.get()
        task = f"{job_text} ({priority})"
        VIEW.insert(END, task)
        DUTY.delete(0, END)

# Function to remove task
def remove():
    VIEW.delete(tk.ANCHOR)

# Heading
HEAD = Label(screen, text="Todolist", fg='#98FB98', bg='#4169E1', font=('display', 30, "bold"), width=25)  # RoyalBlue for fg
HEAD.place(relx=0.012)

# Input box
JOB = StringVar()
DUTY = Entry(screen, width=32, borderwidth=5, font=('system', 18), bd=2, textvariable=JOB)
DUTY.place(x=2, y=60)
DUTY.focus()

# Display box
VIEW = Listbox(screen, font=('system', 18), width=32, height=17, borderwidth=2,
               cursor='pencil', selectforeground='#0B60BA', selectbackground='#96EFFF', bg='#FFFACD')  # LemonChiffon
VIEW.place(x=2, y=100)

# Scrollbar to view up and down
VIEWBAR = Scrollbar(screen)
VIEWBAR.place(x=520, y=300)
VIEW.config(yscrollcommand=VIEWBAR.set)
VIEWBAR.config(command=VIEW.yview)

# Priority selection
PRIORTIES = ["High", "Medium", "Low"]
PRIORITY = StringVar()
PRIORITY.set("High")  # Default priority
PRIORITY_MENU = OptionMenu(screen, PRIORITY, *PRIORTIES)
PRIORITY_MENU.config(width=8, font=('system', 12), bd=2, bg='#FFFACD')  # LemonChiffon
PRIORITY_MENU.place(x=528, y=160)

# Button to add JOB
ADD = Button(screen, text="Add Task", pady=5, width=11, relief='raised', command=add, bg='#FFD700')  # Gold
ADD.place(x=528, y=60)

# Button to delete task
DONE = Button(screen, text="Delete Task", pady=5, width=11, relief='raised', command=remove, bg='#DC143C')  # Crimson
DONE.place(x=528, y=100)

screen.mainloop()
