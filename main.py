''' 
Project: Snake Water Gun Game
Snake = 1
Water = -1
Gun = 0

'''
import random

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")
you_dict = {"s" : 1, "w" : -1, "g" : 0}
rev_dict = {1: "Snake", -1: "Water", 0: "Gun"}

you = you_dict[youstr]
print(f"Your Choice: {rev_dict[you]}\nComputer Choice: {rev_dict[computer]}")

if (computer == you):
    print("It's draw!")

elif(computer == 1) and (you == -1):
    print("You lose!")

elif(computer == -1) and (you == 1):
    print("You win!")

elif(computer == 0) and (you == -1):
    print("You win!")

elif(computer == 1) and (you == 0):
    print("You win!")

elif(computer == -1) and (you == 0):
    print("You lose!")

elif(computer == 0) and (you == 1):
    print("You lose!")

else:
    print("Something went wrong")