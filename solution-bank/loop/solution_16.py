"""
WAP that generates a random number and asks the user to guess what the number is. If the user's guess
is higher than the random number, the program should display "Too high, try again." If the user's guess is lower
than the random number, the program should display "Too low, try again." The program should use a loop that repeats
until the user correctly guesses the random number.
"""

import random

randomNumber = random.randint(1, 100)
i = 0

while True:
    guess = int(input('Enter Guess:\t'))
    i += 1
    if guess == randomNumber:
        print(f'You guessed the number in {i} tries')
        break
    elif guess < randomNumber:
        print('Too low')
    else:
        print('Too high')
