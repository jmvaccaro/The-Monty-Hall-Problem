import tkinter as tk
import random
import tkinter.messagebox  # Import for pop-up messages
import numpy as np

# Global variables initialization
door1 = ""
door2 = ""
door3 = ""
chosen_door = None  # To store the player's chosen door
prize = ["Car", "Goat", "Goat"]  # The possible outcomes for the doors
step_one = 0

# Function to initialize the game and shuffle the doors
def lottery():
    global door1, door2, door3, chosen_door, prize
    # Shuffle the doors to randomize the prize positions
    random.shuffle(prize)
    door1, door2, door3 = prize
    chosen_door = None  # Reset chosen door
    # Enable the door buttons and reset the message
    button1.config(state="normal")
    button2.config(state="normal")
    button3.config(state="normal")
    play_button.config(state="disabled")  # Disable Play button after starting the game
    message.config(text="Choose a door!")


# Function to handle the player's door selection
def choose_door(door: int):
    global chosen_door, step_one
    chosen_door = door
    # Show a pop-up message with a "Choose Again" message
    if step_one == 0:
        tkinter.messagebox.showinfo("Choose Again", f"You've chosen door {door + 1}. Now you can choose again!")
        first_game(chosen_door)
        step_one =+ 1
    else:
        button1.config(command= second_game(0))
        button2.config(command= second_game(1))
        button3.config(command= second_game(2))
    # Disable the other doors so the player cannot click them again

def first_game(door):
    if door == 0:
        if prize[1] == "Car":
            button2.config(state="normal")
            button3.config(state="disabled")
        elif prize[2] == "Car":
            button2.config(state="disabled")
            button3.config(state="normal")
        else:
            if np.random.randint(0,2) == 1:
                button2.config(state="disabled")
                button3.config(state="normal")
            else:
                button2.config(state="normal")
                button3.config(state="disabled")

    elif door == 1:
        if prize[0] == "Car":
            button1.config(state="normal")
            button3.config(state="disabled")
        elif prize[2] == "Car":
            button1.config(state="disabled")
            button3.config(state="normal")
        else:
            if np.random.randint(0,2) == 0:
                button1.config(state="disabled")
                button3.config(state="normal")
            else:
                button1.config(state="normal")
                button3.config(state="disabled")
    elif door == 2:
        if prize[0] == "Car":
            button1.config(state="normal")
            button2.config(state="disabled")
        elif prize[1] == "Car":
            button1.config(state="disabled")
            button2.config(state="normal")
        else:
            if np.random.randint(0,2) == 0:
                button1.config(state="disabled")
                button2.config(state="normal")
            else:
                button1.config(state="normal")
                button2.config(state="disabled")

def second_game(door:int):
    if prize[door] == "Car":
        message.config(text="It's a Car, you win!")
    else:
        message.config(text="It's a Goat, you lose!")
# Create the main window
screen = tk.Tk()
screen.title("Monty Hall's Problem")
screen.geometry("600x400")

# Game title
title = tk.Label(screen, text="Choose a Door!", font=("Helvetica", 16))
title.pack(pady=20)

# Message that shows the current game status
message = tk.Label(screen, text="", font=("Helvetica", 12))
message.pack(pady=20)

# Buttons to choose the doors (larger buttons, horizontal layout)
button_frame = tk.Frame(screen)
button_frame.pack(pady=10)

button1 = tk.Button(button_frame, text="Door N° 1", width=12, height=5, command=lambda: choose_door(0))
button1.grid(row=0, column=0, padx=10)

button2 = tk.Button(button_frame, text="Door N° 2", width=12, height=5, command=lambda: choose_door(1))
button2.grid(row=0, column=1, padx=10)

button3 = tk.Button(button_frame, text="Door N° 3", width=12, height=5, command=lambda: choose_door(2))
button3.grid(row=0, column=2, padx=10)

# Play button to start a new game
play_button = tk.Button(screen, text="Play", width=20, command=lottery)
play_button.pack(pady=10)

# Disable the door buttons at the start
button1.config(state="disabled")
button2.config(state="disabled")
button3.config(state="disabled")

# Run the GUI
screen.mainloop()