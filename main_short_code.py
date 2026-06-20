# It is short form of code in which (computer-you) performed


import random

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")
you_dict = {"s" : 1, "w" : -1, "g" : 0}
rev_dict = {1: "Snake", -1: "Water", 0: "Gun"}

you = you_dict[youstr]
print(f"Your Choice: {rev_dict[you]}\nComputer Choice: {rev_dict[computer]}")

if (computer == you):
    print("It's draw!")
else:    
    if((computer - you) == -2 or (computer - you) == 1):
        print("You win!")
    else:
        print("You lose!")