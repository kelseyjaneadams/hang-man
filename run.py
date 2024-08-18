# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import string
from words import easy_words, medium_words, hard_words
from simple_term_menu import TerminalMenu


def display_instructions():
    print("Welcome to Hangman!")
    print("Instructions:")
    print("1. You will be asked to choose a difficulty level: Easy, Medium, or Hard.")
    print("2. A word will be chosen based on your difficulty choice.")
    print("3. You have 7 attempts to guess the letters in the word.")
    print("4. For each correct guess, the letter will be revealed in the word.")
    print("5. If you guess incorrectly, you will lose an attempt.")
    print("6. The game ends when you guess the word correctly or run out of attempts.")
    print("7. After the game ends, you can choose to play again or exit.")
    print("\nGood luck!\n")

def select_difficulty():
    """
    Prompts the user to select a difficulty level from a terminal menu.
    Options: "Easy", "Medium", "Hard".
    Returns the selected difficulty as a string.
    """
    print("Please select your difficulty")
    options = ["Easy", "Medium", "Hard"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show() 
    user_selection = options[menu_entry_index]
    print(f"You have selected {options[menu_entry_index]}!")

    return user_selection

def get_word(user_selection):
    """
    This function returns the word list based on the selected difficulty level.
    It takes the user_selection argument, which can be "Easy", "Medium", or "Hard",
    and maps it to the corresponding word list. Chooses a random word from the list in uppercase."
    """
    word_lists = {
        "Easy": easy_words,
        "Medium": medium_words,
        "Hard": hard_words
    }

    selected_word_list = word_lists[user_selection]
    word = random.choice(selected_word_list)
    
    return word.upper()

def run_game(word):
    """
    The main game loop for Hangman.
    Converts the random word into a string of letters.
    Stores user guesses.
    Display the word as underscores initially.
    """
    word_letters = set(word)
    guessed_letters = set()
    lives = 7

    display_word = ['_' for _ in word]
    print('Current word:', ' '.join(display_word))




def main():
    display_instructions()
    user_selection = select_difficulty()
    get_word(user_selection)
    run_game(get_word(user_selection))
    
    
    



main()