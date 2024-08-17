# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from words import easy_words, medium_words, hard_words

def display_instructions():
    print("Welcome to Hangman!")
    print("Instructions:")
    print("1. You will be asked to choose a difficulty level: Easy, Medium, or Hard.")
    print("2. A word will be chosen based on your difficulty choice.")
    print("3. You have a limited number of attempts to guess the letters in the word.")
    print("4. For each correct guess, the letter will be revealed in the word.")
    print("5. If you guess incorrectly, you will lose an attempt.")
    print("6. The game ends when you guess the word correctly or run out of attempts.")
    print("7. After the game ends, you can choose to play again or exit.")
    print("\nGood luck!\n")



