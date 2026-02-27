import time
import random
import os

#Constants -color
RED_BOLD="\033[1;31m"
red="\033[31m"
GREEN="\033[1;32m"
green="\033[32m"
YELLOW="\033[1;33m"
yellow="\033[33m"
PURPLE="\033[1;35m"
purple="\033[35m"
reset="\033[0m"
WHITE="\033[1m"

#temp var (remove b4 game start)
i=0

#Tweak Game speed 
lore_speed=0.05
ls=lore_speed
main_speed=0.0
ms=main_speed
credit_speed=0
credit_inbetween_text_speed=1
cts=credit_inbetween_text_speed

#==============Staring Lore=========
def startlore():
   lore = (
            f" In the year 2047,\n Scientists created a {PURPLE}SYSTEM{reset} to measure human "
            f"{GREEN}intelligence{reset},\n but a {PURPLE}glitch{reset} twisted its purpose. "
            f"The {PURPLE}machine{reset} no longer seeks the \n{GREEN} correct number{reset}—\n"
            f" it watches,\n it judges,\n and it {RED_BOLD}PUNISHES{reset} {GREEN}predictability{reset}\n\n "
            f"Now the rules are inverted: only those who deliberately choose\n the {YELLOW}wrong number{reset}, "
            f"who dare to think against {GREEN}logic{reset}, can survive its trials. "
            f"Guessing right is {RED_BOLD}DEATH{reset}; being wrong is the only path to\n {YELLOW}victory{reset}. "
            
            f"\n\n This is a {GREEN}contest of probability{reset}. "
            f"{YELLOW}Win five rounds{reset} and the \n{PURPLE} system fractures{reset}."
            f"{RED_BOLD}Lose..{reset} and you were {RED_BOLD}never meant to persist{reset}.\n"
          )
            
   for I in lore:
    print(I,end="",flush=True)
    time.sleep(ls)

  
#=================main logic of game            
def startmain():
    main_start_text=(f"\n {RED_BOLD}User detected. Analyzing behavior...{reset}"
                     f"\n Input delay logged. Timestamp 2047-02-18T15:42."
                     f"\n Your choices are {WHITE}noted and evaluated.{reset}"
                     f"\n Protocol Initialized: Input must be within range {RED_BOLD}1–10{reset}\n"
                     f"\n\n {WHITE}Round initiated.{reset} {WHITE}Human C̶o̶n̶f̶i̶d̶e̶n̶c̶e̶ under{RED_BOLD}observation.{reset}\n\n")

                
#yo gpt ka upper ka idea se.. i made a Syntax shorter:> notloop function..for k in maintext[0]:
                   
 #beginner shi..                  
        #             print(k,end="",flush=True)
        #            time.sleep(ms)
        #        for l in maintext[2]:
        #            print(l,end="",flush=True)
        #            time.sleep(ms)
        #        for m in maintext[1]:
        #           print(m,end="",flush=True)
        #            time.sleep(ms)
                        
#got tips from gpt (this code is good but still not reusable coz.. typewriter funtion mei use krne bol rha hai.. 1 typewriter function (reusable) and then use it with maintext[i] typew(maintext[i])) like this, === Great idea.. but I dont wana use gpt idea .. let this game be human made (85%) :>
#typew type hi hai but :> I made it..
    for o in main_start_text:
        print(o,end="",flush=True)
        time.sleep(ms)
        
    
    #def start_type_writer(i):
#       for n in main_start_text[i]:
#           print(n,end="",flush=True)
#           time.sleep(ms)
#                                                     
#    start_type_writer(0)
#    start_type_writer(2)
#    start_type_writer(1)
#    start_type_writer(3)
#    
    main_game_text=[f"Can you read the machine’s mind? Number: ",
                    f"\nThe system {GREEN}scans{reset} your choice… your guess: ",
                    f"\nA {GREEN}green light{reset} blinks. Try another number: ",
                    f"\nThe clock is {GREEN}ticking…{reset} what’s your move? ",
                    
                    f"\n{RED_BOLD}Survival{reset} depends on being wrong…",
                    f"{GREEN}Input received:{reset}User still {RED_BOLD}alive{reset}. \nProbability of {RED_BOLD}survival: 37.2%.{reset} Lol.\n",
                    f"Observation log : {RED_BOLD}User{reset} survived 4 rounds.\nSystem slightly traumatized.\n"]
    
    def main_type_writer(i):
        for w in main_game_text[i]:
            print(w,end="",flush=True)
            time.sleep(ms)
    main_game_error=[f"Parameters outside expected range.(1-10)"
                     f"Parameter Error: human randomness exceeds safe parameters."
                     f"The system hates your choice."
                     f"Stochastic behavior too high"]
                    
    def main_type_writer(i):
        for w in main_game_error[i]:
            print(w,end="",flush=True)
            time.sleep(ms)
    #var
    attempt=0
    value_list=[]
    while attempt < 5:
        main_type_writer(attempt)
        value=int(input(""))
        if value not in range(1,11):
            error=random.choice(0,1,2,3)
            
            main_game_error.pop(error)                          
        value_list.append(value)
        attempt+=1
        if attempt==4:
            main_type_writer(-1)                            
        if attempt==3:
            main_type_writer(-2)          
                  
    
                     
#end lore logic
def endlore():
                pass
                
                
#self credit?😅  gpt's section   
def credits():
    width = 45

    credit = [
    f"{YELLOW}Credits:{reset}",
    "",
    f"{RED_BOLD}Game:{reset}",
    f"{PURPLE}GUESS THE WRONG NUMBER{reset}",
    "",
    f"Created by: {GREEN}Kishor{reset}",
    f"Game Design: {GREEN}Kishor{reset}",
    f"Story & Lore: {GREEN}Kishor{reset}",
    f"Testing & Debug: {GREEN}Kishor{reset}",
    "",
    f"{YELLOW}Special Thanks:{reset}",
    f"{GREEN}Players (You){reset}",
    f"{PURPLE}Pyroid{reset}",
    f"{GREEN}ChatGPT{reset} for Credit Screen :)",
    "",
    f"{YELLOW}2026 © Kishor{reset}",
    f"{RED_BOLD}See Ya <3{reset}",
    f"Made with {RED_BOLD}love <3{reset}",
    f"{YELLOW}\n\n\nBefore you disappear… rate this experiment (1–5):{reset} ",
    
]

    display = [""] * 10

    for line in credit:
        display.append(line)
        display.pop(0)

        os.system('cls' if os.name == 'nt' else 'clear')  # ✅ clear every frame

        for l in display:
            print(l)

        time.sleep(credit_speed)
    rating = input(f"{YELLOW}\nRate this experiment (1-5): {reset}")

    if rating not in ["1", "2", "3", "4", "5"]:
        print(f"{RED_BOLD}SYSTEM ERROR: Invalid rating detected.{reset}")
        return

    rating = int(rating)

    print(f"\n{GREEN}You rated the experiment: {rating}/5{reset}")
    time.sleep(cts)

    if rating == 5:
        print(f"{PURPLE}SYSTEM OVERRIDE DETECTED...{reset}")
        time.sleep(cts)
        print(f"{GREEN}Elite Mind Confirmed. Probability bends for you.{reset}")
        time.sleep(cts)
        print("The system could not predict you.You broke the pattern.")

    elif rating == 4:
        print(f"{YELLOW}SYSTEM RESPONSE: High cognitive variance detected.{reset}")
        time.sleep(cts)
        print(f"{GREEN}You almost broke the machine.{reset}")
        time.sleep(cts)

    elif rating == 3:
        print(f"{YELLOW}SYSTEM RESPONSE: Acceptable instability logged.{reset}")

    else:  # 1 or 2
        print(f"{RED_BOLD}SYSTEM RESPONSE: Subject lacks chaos instinct.{reset}")
        print(f"{RED_BOLD}Recalibration advised...{reset}")
    end=(f"{green}SYSTEM OFFLINE — {reset}{RED_BOLD}Transmission Ended.{reset}")
    for e in end:
                print(e,end="",flush=True)
                time.sleep(.1)
                
def main():
    #startlore()
    startmain()
    endlore()
    #credits()
    
main()



