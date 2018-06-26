#!/usr/bin/env python3
"""
Guess my number exercise from the edX MIT 6.00.1x intro to cs course
Author: Joby/nomadfarmer
"""

# Paste your code into this box
upperLimit = 100
lowerLimit = 0
guess = (upperLimit + lowerLimit) // 2
answer = ""

print("Please think of a number between 0 and 100!")
while True:
    print("Is your secret number " + str(guess) + "?")
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    #answer = answer.lower()
    if len(answer) == 0:
        answer = "?"
    if answer == "c":
        break
    elif answer == "h":
        upperLimit = guess
    elif answer == "l":
        lowerLimit = guess
    else:
        print("Sorry, I did not understand your input.")
    guess = (upperLimit + lowerLimit) // 2
print("Game over. Your secret number was: " + str(guess))
