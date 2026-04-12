import random as r
import time
import os

#Text speed for Rules
default=0.030
fast=0.01
tsr=default
#Text speed for Main game
default=0.040
fast=0.01
tsm=default

def game_logo():
    os.system("clear")
    for i in "\tRock🪨 ","Paper📜 ","Scissor✂️\n":
        print(i,end="",flush=True)
        time.sleep(1)

def game_rules():
    rules=f"""\nRules 📝.
10 Rounds Only.
Each win leads to increment in score.
At the end the person with high score wins.
Ctrl-d To quit(Don't Quit)..
Input:Rock,Paper,Scissor(case insensitive)..
\n\nGame Begins.!🍿\n"""
    for i in rules:
        if i == ".":
            time.sleep(1)
        print(i,end="",flush=True)
        time.sleep(tsr)
    

def game_start_main():
    ask_user=["Firstmove?Rock/Paper/Scissor ","RPS Which one? ","Again ","Guess?","My move (Rock) your move😆 ","I know your move! Move please? ","Opponent Feels sleepy,Guess Fast: ","Snoring..😴","Press W to win,jk ..guess?: ","Last move!(sighs*) "]
    roundcount=1
    computer_score=0
    user_score=0
    game_choice=["Rock","Paper","Scissor"]
    game_choice_check=["Rock","Paper","Scissor"]
    def typewriter(text):
        for i in text:
            print(i,end="",flush=True)
            time.sleep(tsm)
        return ""

    while roundcount<=10:
        computer_move=r.choice(game_choice)
        try:
            print()
            print("_"*33)
            text=ask_user[roundcount-1]
            typewriter(f"\033[1;33mRound {roundcount}:\033[0m")
            user_guess=input(typewriter(text)).title().strip()
            if user_guess in game_choice_check:
                if user_guess==computer_move:
                    typewriter(f"Computer move:{computer_move}\n")
                    typewriter("\n\033[32mDraw\033[0m")
                    roundcount+=1
                elif user_guess =="Rock" and computer_move =="Scissor":
                    typewriter(f"Computer Move:{computer_move}\n")
                    typewriter("\n\033[32mYou won:Rock Crushes Scissor\033[0m")
                    roundcount+=1
                    user_score+=1
                elif user_guess =="Scissor" and computer_move =="Paper":
                    typewriter(f"Computer Move:{computer_move}\n")
                    typewriter("\n\033[32mYou won:Scissors cuts Papers\033[0m")
                    roundcount+=1
                    user_score+=1
                elif user_guess=="Paper"  and computer_move=="Rock":
                    typewriter(f"Computer Move:{computer_move}\n")
                    typewriter("\n\033[32mYou won:Paper captures rock!\033[0m")
                    roundcount+=1
                    user_score+=1
                else:
                    typewriter(f"Computer move:{computer_move}\n")
                    typewriter(f"\n\033[31mComputer wins! {computer_move}\033[0m")
                    roundcount+=1
                    computer_score+=1
            else:
                typewriter("\n\033[31mError: Enter a valid Choice\033[0m")
        except (EOFError,KeyboardInterrupt):
            typewriter("\033[31m\nQuitters never win 🤐\033[0m")
            break
    print()
    print("_"*33)
    print("Computer | You")
    print(f"{computer_score:9}|{user_score}")
    if user_score==computer_score:
        print("\n\n\033[32mDraw\033[0m")
    elif user_score>computer_score:
        print("\n\n\033[32mYou won :)\033[0m")
    else:
        print("\n\n\033[31mYou lost to a computer :)\033[0m")
def main():
    game_logo()
    game_rules()
    game_start_main()

main()
