import tkinter as tk
import random
from tkinter import messagebox

# Game variables
choices = ["Rock", "Paper", "Scissors"]
user_score = 0
system_score = 0
rounds_to_win = 5

def get_svg(choice):
    """Returns an SVG-like text representation based on the choice."""
    svgs = {
        "Rock": "\u270A",  # ✊
        "Paper": "\u270B", # ✋
        "Scissors": "\u270C" # ✌
    }
    return svgs.get(choice, "")

def play(choice):
    global user_score, system_score
    system_choice = random.choice(choices)
    result_text.set(f"System chose {system_choice}")
    
    if choice == system_choice:
        outcome.set("It's a Tie!")
    elif (choice == "Rock" and system_choice == "Scissors") or \
         (choice == "Paper" and system_choice == "Rock") or \
         (choice == "Scissors" and system_choice == "Paper"):
        user_score += 1
        outcome.set("You Win this Round!")
    else:
        system_score += 1
        outcome.set("System Wins this Round!")
    
    user_score_label.config(text=f"User: {user_score}")
    system_score_label.config(text=f"System: {system_score}")
    
    user_choice_label.config(text=get_svg(choice))
    system_choice_label.config(text=get_svg(system_choice))
    
    check_winner()

def check_winner():
    global user_score, system_score
    if user_score == rounds_to_win:
        messagebox.showinfo("Game Over", "Congratulations! You won the game!")
        reset_game()
    elif system_score == rounds_to_win:
        messagebox.showinfo("Game Over", "System won the game! Better luck next time.")
        reset_game()

def reset_game():
    global user_score, system_score
    user_score = 0
    system_score = 0
    outcome.set("Let's Play!")
    result_text.set("Choose Rock, Paper, or Scissors")
    user_score_label.config(text="User: 0")
    system_score_label.config(text="System: 0")
    user_choice_label.config(text="")
    system_choice_label.config(text="")

# UI Setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x500")
root.configure(bg="#2C3E50")

outcome = tk.StringVar(value="Let's Play!")
result_text = tk.StringVar(value="Choose Rock, Paper, or Scissors")

title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), fg="white", bg="#2C3E50")
title.pack(pady=10)

user_score_label = tk.Label(root, text="User: 0", font=("Arial", 14), fg="white", bg="#2C3E50")
user_score_label.pack()

system_score_label = tk.Label(root, text="System: 0", font=("Arial", 14), fg="white", bg="#2C3E50")
system_score_label.pack()

frame = tk.Frame(root, bg="#34495E")
frame.pack(pady=10)

user_choice_label = tk.Label(frame, text="", font=("Arial", 30), bg="#34495E", fg="white")
user_choice_label.grid(row=0, column=0, padx=50)

system_choice_label = tk.Label(frame, text="", font=("Arial", 30), bg="#34495E", fg="white")
system_choice_label.grid(row=0, column=1, padx=50)

message_label = tk.Label(root, textvariable=result_text, font=("Arial", 12), fg="white", bg="#2C3E50")
message_label.pack(pady=5)

status_label = tk.Label(root, textvariable=outcome, font=("Arial", 14, "bold"), fg="yellow", bg="#2C3E50")
status_label.pack(pady=5)

button_frame = tk.Frame(root, bg="#2C3E50")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock ✊", width=10, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper ✋", width=10, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors ✌", width=10, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

reset_button = tk.Button(root, text="Reset", command=reset_game, bg="#E74C3C", fg="white")
reset_button.pack(pady=10)

root.mainloop()