import random

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

game_list = ["Rock", "Paper", "Scissors"]
computer = c = 0
command = p = 0
print("Score:Computer" + str(c) + "Player" + str(p))

while True:
    computer_choice = random.choice(game_list)
    command = input("Rock , Paper , Scissors or Quit: ")
    if command == computer_choice:
        print("Tie")
    elif command == "Rock":
        if computer_choice == "Scissors":
            print("Player won!!")
            p += 1
        else:
            print("Computer won!!")
            c += 1
    elif command == "Paper":
        if computer_choice == "Rock":
            print("Player won!!")
            p += 1
        else:
            c += 1
    elif command == "Scissors":
        if computer_choice == "Paper":
            print("Player won!!")
            p += 1
        else:
            c += 1
    elif command == "Quit":
        print("Thank You for playing.")
        break
    else:
        print("Wrong Command!")

print("Player: " + command)
print("Computer: " + computer_choice)
print("")
print("Score:Computer" + str(c) + "Player" + str(p))
print("")
