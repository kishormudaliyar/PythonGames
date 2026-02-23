import time
import random

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

#Staring Lore
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
f"{RED_BOLD}Lose..{reset} and you were {RED_BOLD}never meant to persist{reset}."
)

   for I in lore:
    print(I,end="",flush=True)
    time.sleep(0.05)
    
def startmain():
                pass 

def endlore():
                pass
   
def credits():
                pass       
                
def main():
    startlore()
    startmain()
    endlore()
    credits()
    
main()



