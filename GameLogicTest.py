"""
import random
import time
funny=["Input delay logged. Timestamp 2047-02-18T15:42.","Your choices are noted and evaluated.","User input detected. Analyzing behavior..."]
for I in funny:
    print(I)
    time.sleep(1)
    
b=funny[1]
a=funny[2]
a,b=b,a


fun={1:"Input delay logged. Timestamp 2047-02-18T15:42.",2:"Your choices are noted and evaluated.",3:"User input detected. Analyzing behavior..."}

for i in fun.values():
    print(i)
    time.sleep(1)
    
    """
# Syntax: \033[<style>;<text_color>;<bg_color>mYour Text\033[0m
"""
print("\033[1;31mThis is red text\033[0m") 
print("\033[91mThis is red text\033[0m")     # Red text
print("\033[1;32mThis is green text\033[0m")   
print("\033[32mThis is green text\033[0m") # Green text
print("\033[1;34mThis is bold blue text\033[0m")
  # Bold blue text

for i in range(30,38):
    print(f"\033[{i}mKishor\033[0m")
    

for i in range(40,48):
    print(f"\033[{i}mKishor\033[0m")
    
for i in range(100,108):
    print(f"\033[{i}mKishor\033[0m")
 """   
"""   
messages = {
    1: "Input delay logged.",
    2: "Your choices are noted.",
    3: "User input detected."
}
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"
def print_colored(msg, color):
    print(color + msg + "\033[0m")

print_colored("hii",GREEN)

 """
""" 
    #gpt method
GREEN = "\033[92m"
RESET = "\033[0m"

sentence = "User input detected. Analyzing behavior..."

words = sentence.split()

words[2] = GREEN + words[2] + RESET   w third word color

print(join(words)) 

      """
"""
def first() :
    print("I am frist funtion")  
    
       
def second():
    print("second")
    first()
                     

second()
"""
 
"""while True:
    try:
        for i in list:
            value=int(input(i))
            if value not in range(1,11):
                print("Range error")
                continue
            value_list.append(value)
            print(value_list) 
    except:
        print("Error")
        continue"""
    
value_list=[]
ai_words=[f"Can you read the machine’s mind? Number: ",
          f"The system scans your choice… your guess: ",
          f"A green light blinks. Try another number: "]
attempt=0                        
while attempt<len(ai_words):
   value=int(input(ai_words[attempt]))
   if attempt==0:
       pass    
       
   attempt+=1                                           
                      
                            