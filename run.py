import random
import string
import sys
from words import easy_words, medium_words, hard_words
from simple_term_menu import TerminalMenu
from hangman_visuals import visual_hangman_lives


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
    print("Please select your difficulty\n")
    options = ["Easy", "Medium", "Hard"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show() 
    user_selection = options[menu_entry_index]
    print(f"You have selected {options[menu_entry_index]}!\n")

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
    Displays the word as underscores, handles user guesses, updates the display, 
    and tracking lives. The game ends when the player either guesses the word 
    correctly or runs out of lives.
    """
    word_letters = set(word)
    guessed_letters = set()
    lives = 7

    display_word = ['_' for _ in word]
    print("Let's play Hangman!\n")

    while len(word_letters) > 0 and lives > 0:
        print('Current word:', ' '.join(display_word)) 
        print('\n')
        print(f"You have {lives} attempts remaining.\n")

        user_guess = input("Guess a letter or the full word: ").upper()

        if len(user_guess) == 1 and user_guess.isalpha():
            if user_guess in guessed_letters:
                print(f'You have already guessed the letter "{user_guess}". Please try again.') 
            else:
                guessed_letters.add(user_guess)

                if user_guess in word_letters:

                    for i, letter in enumerate(word):
                        if letter == user_guess:
                            display_word[i] = user_guess
                    word_letters.remove(user_guess)

                    if not word_letters:
                        print(f"You Win! You correctly guessed the word: {''.join(display_word)}")
                        break 
                else:
                    lives -= 1
                    print(f'Sorry, {user_guess} is not in the word.')

        elif len(user_guess) == len(word) and user_guess.isalpha():
            if user_guess == word:
                print(f"You Win! You've correctly guessed the word: {word}")
                break
            else:
                lives -= 1
                print(f'Sorry, "{user_guess}" is not the correct word.')
        
        else:
            print("Invalid input. Please enter a single letter or the full word.")
    
    if lives == 0:
        print(f"Game Over! The correct word was: {word}")
    
    user_choice = play_again_menu()

    if user_choice == "Play Again":
        main()
    else:
        print("Thank you for playing Hangman! Goodbye!")
        sys.exit()


def play_again_menu():
    """
    Prompts the user to choose whether they want to play again or exit.
    Options: "Play Again", "Exit".
    Returns the user's choice as a string.
    """
    print("What would you like to do next?\n")
    options = ["Play Again", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show() 
    user_selection = options[menu_entry_index]
    print(f"You have selected {options[menu_entry_index]}!\n")

    return user_selection
                

def main():
    display_instructions()
    user_selection = select_difficulty()
    get_word(user_selection)
    run_game(get_word(user_selection))

main()