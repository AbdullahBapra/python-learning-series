


"""
🐍💦🔫 Snake, Water, Gun Game in Python!  

This is a simple Python game based on the classic **Snake, Water, Gun** concept (similar to Rock, Paper, Scissors).  

Game Rules:  
- 🔫 **Gun (0)** defeats 🐍 **Snake (-1)**  
- 🐍 **Snake (-1)** defeats 💦 **Water (1)**  
- 💦 **Water (1)** defeats 🔫 **Gun (0)**  

- If both players choose the same, it's a **draw**!  

Let's build this fun project using Python! 🚀  
"""

import random

computer = random.choice([1, 0, -1])  # Randomly selects one of these numbers
 
  
youstr = input("enter your choice: ")
dect = {"g" : 0 , "w" : 1 , "s" : -1}
rev_dect = {0 : "Gun" , 1 : "water" , -1 : "snake"}
you = dect[youstr]


print(f"Your choice is {rev_dect[you]}")
print(f"Computer chose {rev_dect[computer]}") 

if(you == computer):
    print('its draw 🤝')

elif( you == 0 and computer == 1):
    print("You lose! 😢")  

elif( you == 0 and computer == -1):
    print("You win! 🎉")  

elif( you == 1 and computer == 0):
    print("You lose! 😢")  

elif( you == 1 and computer == -1):
    print("You win! 🎉")  

elif( you == -1 and computer == 0):
    print("You lose! 😢")  

elif( you == -1 and computer == 1):
    print("You win! 🎉")  

