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
main_speed=.01
ms=main_speed
end_lore_speed=0.05
es=end_lore_speed
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
                     f"\n\n {WHITE}Round initiated.{reset} {WHITE}Human I̶n̶t̶e̶l̶l̶i̶g̶e̶n̶c̶e̶ under{RED_BOLD}observation.{reset}\n\n")

                
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
    main_game_text=[f" Can you read the machine’s mind? Number: ",
                    f"\nThe system {GREEN}scans{reset} your choice… your guess: ",
                    f"\nA {GREEN}green light{reset} blinks. Try another number: ",
                    f"\nThe clock is {GREEN}ticking…{reset} what’s your move? ",
                    f"\n{RED_BOLD}Survival{reset} depends on being wrong…"]
                 
    
    main_game_error=[f" Parameters outside expected range.(1-10)\n",
                     f" Parameter Error: human randomness exceeds safe parameters.\n",
                     f" The system hates your choice.\n",
                     f" Stochastic behavior too high\n",
                     f" Whoa there… the range is 1 to 10, not 1 to infinity.\n",
                     f" Range: 1–10. You chose chaos.\n",
                     f" Out of range. The system raises an eyebrow.\n",
                     f" Impressive confidence. Terrible range awareness.\n",
                     f" Limits were given. You ignored them.\n",
                     f" The system recognizes only bounded thought.\n",
                     f" You attempt to defy defined limits.\n",]
                     
                     
    main_game_derror=[f" [System] Duplicate value detected.\n", 
                     f" [Developer] The system remembers,Try again.\n",
                     f" [System] Trying the same trick twice?\n",
                     f" [System] Repeating fate changes nothing.\n",
                     f" [PATCH_REQUIRED] Install common sense v1.0.\n"
                     f" No further warnings will be issued.\n"
                     f" No retries remaining.\n"]
                     
                     
    main_game_fun=[f" Alert: human smiles detected. Processing sarcasm… failed.\n",
                   f" Memory leak detected: user thinking too much. Reboot recommended.\n",
                   f" [DEBUG] No bugs detected. Just you.\n",
                   f" [SESSION] You’re still alive. For now.\n",
                   f" [SYSTEM] Are you thinking… or guessing?\n",
                   f" {GREEN}Input received:{reset}User still {RED_BOLD}alive{reset}. \nProbability of {RED_BOLD}survival: 37.2%.{reset} Lol.\n",
                   f" Observation log : {RED_BOLD}User{reset} survived 4 rounds.\nSystem slightly traumatized.\n"]
    
    main_game_end=(f"[BOOM] You weren’t supposed to be right.\n"
                   f"Round Terminated.\n"
                   f"YOU HAVE BEEN ELIMINATED.\n"
                   f"{RED_BOLD}GAME OVER.{reset}\n")
                                    
    def main_type_writer(i):
        for w in main_game_text[i]:
            print(w,end="",flush=True)
            time.sleep(ms)                                
    def error_type_writer(i):
        for w in main_game_error[i]:
            print(w,end="",flush=True)
            time.sleep(ms)
    def derror_type_writer(i):
        for k in main_game_derror[i]:
            print(k,end="",flush=True)
            time.sleep(ms) 
    def fun_type_writer(i):
        for a in main_game_fun[i]:
            print(a,end="",flush=True)
            time.sleep(ms)
    #temp type_writer() checker
    def type(text):
        for p in text:
            print(p,end="",flush=True)
            time.sleep(ms)
    #var
    attempt=0
    error=0
    d_error=0
    value_list=[] 
    game_status="win"
    boom=random.randint(1,10)
    while attempt < 5:
        try:
            main_type_writer(attempt)
            value=int(input(""))
            print(boom)
            if value in value_list:
                derror_type_writer(d_error)
                d_error+=1
                error+=1
            elif value==boom:
                for y in main_game_end:
                    print(y,end="",flush=True)
                    time.sleep(ms)
                game_status="lose"
                break     
            elif value in range(1,11):
                value_list.append(value)
                attempt+=1
                randfun=random.randint(0,4)
                if attempt==1:fun_type_writer(randfun)
                if attempt==2:fun_type_writer(randfun);main_game_fun.pop(randfun)
                if attempt==3:fun_type_writer(-2)
                if attempt==4:fun_type_writer(-1);fun_type_writer(0)
            else:
                error+=1
                if error == 4:derror_type_writer(4);continue
                if error+d_error == 5:
                    type("\nSystem Lockdown: human control terminated. All functions automated.\nAutonomous Mode Engaged: Player influence nullified. System now in control.\nEnd of Line: user intervention no longer permitted. System takeover complete.")
                    game_status="lose"
                    break
                error_type_writer(error)
        except:
            r_error=random.randint(0,len(main_game_error)-1)
            error_type_writer(r_error)
            main_game_error.pop(r_error)
            error+=1
            continue        
    return game_status             
                #error=random.choice(0,1,2,3)
                #error_type_writer(error)
                #main_game_error.pop(error) 
                     
#end lore logic
def endlore(game_status):
    endlore=(f"User victory logged. AI requests coffee break… forever."
             f"System override complete. Human logic prevailed — won… somehow."
             f"System shutdown initiated… user laughed. AI cries internally.")
    if game_status=="win":         
        for w in endlore:
            print(w,end="",flush=True)
            time.sleep(ms)                        
                
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
    game_status=startmain()
    endlore(game_status)
    #credits()
    
main()



