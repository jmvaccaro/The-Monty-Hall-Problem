import pandas as pd
import numpy as np
import tkinter as tk
import random

door1 = ""
door2 = ""
door3 = ""

prize = ["Car","Goat","Goat"]

def lottery():
    global door1,door2,door3
    random.shuffle(prize)
    door1,door2,door3 = prize
    button1.config(state="normal")
    button2.config(state="normal")
    button3.config(state="normal")
    play_button.config(state="disabled")
    return door1,door2,door3

def choose_door(door: int):
    if door == 0 and prize[door] == "Car":
        if np.random.randint(1,2) == 1:
            button2.config(state="disabled")
        else:
            button3.config(state="disabled")
    print(prize[door])
    return


screen = tk.Tk()
screen.title = "Monty Hall's Problem"
screen.geometry("600x400")

title = tk.Label(screen, text="Choose a Door", font=("Helvetica",16))
title.pack(pady=20)

play_button = tk.Button(screen,text="Play",width=20,command=lottery)
play_button.pack(pady=10)

button1 = tk.Button(screen,text="Door N° 1",width=20,command=lambda: choose_door(0))
button1.pack(pady=10)
button2 = tk.Button(screen,text="Door N° 2",width=20,command=lambda: choose_door(1))
button2.pack(pady=10)
button3 = tk.Button(screen,text="Door N° 3",width=20,command=lambda: choose_door(2))
button3.pack(pady=10)

button1.config(state="disabled")
button2.config(state="disabled")
button3.config(state="disabled")

screen.mainloop()

