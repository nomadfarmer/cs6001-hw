#!/usr/bin/env python3
"""
Hangman game. loadWords was came pre-written, but each problem in this problem
set will have me writing the other functions. Docstrings came pre-written as well.


NOTE: The grader doesn't accept f strings as valid syntax. I edited all lines
with f" in my submission, but kept them here because I prefer the style.
"""

# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for l in secretWord:
        if l not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    board = ""
    for l in secretWord:
        if l in lettersGuessed:
            board += l
        else:
            board += "_ "
    return board

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    avail_letters = "abcdefghijklmnopqrstuvwxyz"
    for l in lettersGuessed:
        avail_letters = avail_letters.replace(l, '')
    return avail_letters

def hangman(secret_word):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 8
    letters_guessed = []

    print("Welcome to the game, Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    while not isWordGuessed(secret_word, letters_guessed) and guesses > 0:
        print("-"*13)
        print(f"You have {guesses} guesses left.")
        print("Available letters: " + getAvailableLetters(letters_guessed))
        guess = input("Please guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("That is not a valid guess. Please try again.")
        elif guess in letters_guessed:
            board = getGuessedWord(secret_word, letters_guessed)
            print(f"Oops! You've already guessed that letter: {board}")
        else:
            letters_guessed.append(guess)
            board = getGuessedWord(secret_word, letters_guessed)

            if guess not in secret_word:
                guesses -= 1
                print(f"Oops! That letter is not in my word: {board}")
            else:
                print(f"Good Guess: {board}")
    print("-"*13)
    if guesses:
        print("Congratulations, you won!")
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
