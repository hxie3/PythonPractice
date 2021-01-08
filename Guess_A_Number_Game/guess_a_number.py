# This simple game will ask a user to guess a number between 1 and 20. The player has six chances to guess the number.

import random

count = 0
flag = False
username = input("What is your name?\n")
random_number = random.randrange(1,21)
print(f"Hi {username}, I'm thinking of a number between 1 and 20.")
guess = 0
while count < 6:
    count += 1
    guess = int(input("Take a guess.\n"))
    if guess < random_number:
        print("Your guess is too low.")
    elif guess > random_number:
        print("Your guess is too high.")
    else:
        flag = True
        break
if flag:
    print(f"Good job {username}! You guessed the number in {count} guesses!")
else:
    print(f"Sorry. {username}. You could not guess my number {random_number}.")