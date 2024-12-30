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
won_switch = 0
total_switch = 0
won_no_switch = 0
total_no_switch = 0

# Function to initialize the game and shuffle the doors
def lottery():
    global door1, door2, door3, chosen_door, prize, step_one
    # Shuffle the doors to randomize the prize positions
    step_one = 0
    random.shuffle(prize)
    door1, door2, door3 = prize
    chosen_door = None  # Reset chosen door
    # Enable the door buttons and reset the message
    button1.config(state="normal", text="Door N° 1")
    button2.config(state="normal", text="Door N° 2")
    button3.config(state="normal", text="Door N° 3")
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
        step_one += 1
    else:
        print(prize)
        button1.config(command=lambda: second_game(0))
        button2.config(command=lambda: second_game(1))
        button3.config(command=lambda: second_game(2))

# First game logic - opens other doors based on the initial choice
def first_game(door):
    if door == 0:
        if prize[1] == "Car":
            button2.config(state="normal")
            button3.config(state="disabled", text="GOAT")
        elif prize[2] == "Car":
            button2.config(state="disabled", text="GOAT")
            button3.config(state="normal")
        else:
            if np.random.randint(0, 2) == 1:
                button2.config(state="disabled", text="GOAT")
                button3.config(state="normal")
            else:
                button2.config(state="normal")
                button3.config(state="disabled", text="GOAT")
    elif door == 1:
        if prize[0] == "Car":
            button1.config(state="normal")
            button3.config(state="disabled", text="GOAT")
        elif prize[2] == "Car":
            button1.config(state="disabled", text="GOAT")
            button3.config(state="normal")
        else:
            if np.random.randint(0, 2) == 0:
                button1.config(state="disabled", text="GOAT")
                button3.config(state="normal")
            else:
                button1.config(state="normal")
                button3.config(state="disabled", text="GOAT")
    elif door == 2:
        if prize[0] == "Car":
            button1.config(state="normal")
            button2.config(state="disabled", text="GOAT")
        elif prize[1] == "Car":
            button1.config(state="disabled", text="GOAT")
            button2.config(state="normal")
        else:
            if np.random.randint(0, 2) == 0:
                button1.config(state="disabled", text="GOAT")
                button2.config(state="normal")
            else:
                button1.config(state="normal")
                button2.config(state="disabled", text="GOAT")

# Second game logic - after choosing a second door
def second_game(second_door: int):
    global won_switch, total_switch, won_no_switch, total_no_switch, prize, chosen_door

    # Verifica si la puerta elegida tiene el auto o la cabra
    if prize[second_door] == "Car":
        message.config(text=f"It's a Car, you win! Door {second_door + 1}")
        # Si ganaste cambiando, se cuenta como una victoria con cambio
        if second_door != chosen_door:
            won_switch += 1
            total_switch += 1
        else:
            # Si no cambiaste, es una victoria sin cambiar
            won_no_switch += 1
            total_no_switch += 1
    else:
        message.config(text=f"It's a Goat, you lose! Door {second_door + 1}")
        # Si perdiste cambiando, cuenta como una derrota con cambio
        if second_door != chosen_door:
            total_switch += 1
        else:
            # Si no cambiaste, cuenta como una derrota sin cambiar
            total_no_switch += 1

    # Deshabilitar los botones de las puertas después de la segunda elección
    button1.config(state="disabled")
    button2.config(state="disabled")
    button3.config(state="disabled")

    # Habilitar el botón de "Play" para empezar una nueva partida
    play_button.config(state="normal")

    # Actualizar los porcentajes de ganados cuando se cambia o no
    update_percentages()

# Función para actualizar los porcentajes
def update_percentages():
    # Calcula los porcentajes de ganados al cambiar o al no cambiar
    switch_percentage = (won_switch / total_switch) * 100 if total_switch > 0 else 0
    no_switch_percentage = (won_no_switch / total_no_switch) * 100 if total_no_switch > 0 else 0

    # Actualiza las etiquetas en la UI
    change_label.config(text=f"% won when switching: {switch_percentage:.2f}%")
    no_change_label.config(text=f"% won when not switching: {no_switch_percentage:.2f}%")

# Create the main window
screen = tk.Tk()
screen.title("Monty Hall's Problem")
screen.geometry("600x400")

# Percentage functions:
def percentage_switch():
    global total_switch, won_switch
    if total_switch == 0:
        return 0
    else:
        return won_switch * 100 / total_switch

def percentage_no_switch():
    global total_no_switch, won_no_switch
    if total_no_switch == 0:
        return 0
    else:
        return won_no_switch * 100 / total_no_switch

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

# Labels to show win percentages
change_label = tk.Label(screen, text=f"% won when switching: {percentage_switch():.2f}%", font=("Helvetica", 12))
change_label.pack(pady=5)
no_change_label = tk.Label(screen, text=f"% won when not switching: {percentage_no_switch():.2f}%", font=("Helvetica", 12))
no_change_label.pack(pady=5)

# Run the GUI
screen.mainloop()