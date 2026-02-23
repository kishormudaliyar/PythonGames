"""
import time
import os

# Function to clear terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

credits = [
    "GUESS THE WRONG NUMBER",
    "",
    "",
    "Created by: Kishor",
    "",
    "Game Design: Kishor",
    "",
    "Story & Lore: Kishor",
    "",
    "Testing & Debug: Kishor",
    "",
    "Special Thanks:",
    "All Python coders",
    "Pyroid Community",
    "",
    "2026 © Kishor",
    "See ya"
]

display = [""] * 10  # screen height (lines visible at once)

for line in credits:
    display.append(line)      # add new line at bottom
    display.pop(0)            # remove top line to scroll up
    clear_screen()
    for l in display:
        print(l)
    time.sleep(0.5)           # adjust scroll speed
    
    """
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Rough terminal width
width = 45

credits = [
    "Credits",
    "",
    "",
    "GUESS THE WRONG NUMBER",
    "",
    "Created by: Kishor",
    "Game Design: Kishor",
    "Story & Lore: Kishor",
    "Testing & Debug: Kishor",
    "",
    "Special Thanks:",
    "Players (You)",
    "Pyroid",
    "Chatgpt for Credit Screen :)",
    "",
    "2026 © Kishor",
    "See Ya!❤️"
]

display = [""] * 10  # visible lines on screen

for line in credits:
    display.append(line.rjust(width))  # right-align
    display.pop(0)
    clear_screen()
    for l in display:
        print(l)
    time.sleep(0.5)  # scroll speed