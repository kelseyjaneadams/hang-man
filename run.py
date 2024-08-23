import random
import string
import sys
from colorama import Fore, Back, Style
from simple_term_menu import TerminalMenu
from words import easy_words, medium_words, hard_words
from hangman_visuals import visual_hangman_lives


def main_menu():
    """
    Displays the main menu with options to view instructions,
    start the game or exit. Returns the user's choice as a string.
    """
    print(f""""
                            Welcome to Hangman!
    """)

    options = ["How to Play", "Start Game", "Exit"]
    terminal_menu = TerminalMenu(
        options,
        menu_highlight_style=("bg_green",),
        menu_cursor_style=("fg_green",)
    )
    menu_entry_index = terminal_menu.show()
    user_selection = options[menu_entry_index]

    print(f"""
You have selected {Back.GREEN}{Fore.BLACK}{user_selection}!{Style.RESET_ALL}
""")

    return user_selection


def display_instructions():
    """
    Dispaly game instructions for the user.
    """
    print("""\
Welcome to Hangman!
Instructions:
1. Choose a difficulty level: Easy, Medium, or Hard.
2. A word will be selected based on your chosen difficulty.
3. You have 7 attempts to guess the letters in the word.
4. Each correct letter guessed will be revealed in the word.
5. You can also attempt to guess the entire word at any time.
6. Each incorrect guess costs an attempt and draws part of the Hangman.
7. The game ends when you guess the word or run out of attempts.

Try to guess the word before the Hangman is complete. Good luck!
""")


def select_difficulty():
    """
    Prompts the user to select a difficulty level from a terminal menu.
    Options: "Easy", "Medium", "Hard".
    Returns the selected difficulty as a string.
    """
    print("Please select your difficulty\n")
    options = ["Easy", "Medium", "Hard"]
    terminal_menu = TerminalMenu(
        options,
        menu_highlight_style=("bg_green",), 
        menu_cursor_style=("fg_green",)
    )
    menu_entry_index = terminal_menu.show()
    user_selection = options[menu_entry_index]

    print(f"""
You have selected {Back.GREEN}{Fore.BLACK}{user_selection}!{Style.RESET_ALL}
""")

    return user_selection


def get_word(user_selection):
    """
    This function returns the word list based on the selected difficulty level.
    It takes the user_selection argument, which can be
    "Easy", "Medium", or "Hard", and maps it to the corresponding word list.
    Chooses a random word from the list in uppercase."
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
    Displays the word as underscores, handles user guesses,
    updates the display, and tracking lives. The game ends when the player
    either guesses the word correctly or runs out of lives.
    """
    word_letters = set(word)
    guessed_letters = set()
    lives = 7

    display_word = ['_' for _ in word]
    print("Let's play Hangman!\n")

    while len(word_letters) > 0 and lives > 0:
        print(f"""

Current word: {' '.join(display_word)}

You have {lives} attempts remaining.
""")

        if guessed_letters:
            print(f"""
{Fore.BLUE}Already guessed letters: {" ".join(sorted(guessed_letters))}
{Style.RESET_ALL}
""")

        user_guess = input("Guess a letter or the full word: ").upper()

        if len(user_guess) == 1 and user_guess.isalpha():
            if user_guess in guessed_letters:
                print(f"""
{Fore.RED}You have already guessed the letter "{user_guess}".
Please try again.{Style.RESET_ALL}
""")
            else:
                guessed_letters.add(user_guess)

                if user_guess in word_letters:
                    for i, letter in enumerate(word):
                        if letter == user_guess:
                            display_word[i] = user_guess
                    word_letters.remove(user_guess)

                    if not word_letters:
                        print(f"""
{Back.GREEN}You Win! The word was: {word}{Style.RESET_ALL}
""")
                        break
                else:
                    lives -= 1
                    print(f"""
{Fore.YELLOW}Sorry, {user_guess} is not in the word.{Style.RESET_ALL}
""")
                    print(visual_hangman_lives[lives])

        elif len(user_guess) == len(word) and user_guess.isalpha():
            if user_guess == word:
                print(f"""
{Back.GREEN}You Win! The word was: {word}{Style.RESET_ALL}
""")
                break
            else:
                lives -= 1
                print(f"""
{Fore.YELLOW}Sorry, "{user_guess}" is not the correct word.{Style.RESET_ALL}
""")
                print(visual_hangman_lives[lives])

        else:
            print(f"""
{Fore.RED}INVALID INPUT. Please enter a single letter
or the full word.{Style.RESET_ALL}
""")

    if lives == 0:
        print(f"""
{Back.RED}{Fore.WHITE}You Lose! The correct word was: {word}{Style.RESET_ALL}
""")

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
    terminal_menu = TerminalMenu(
        options,
        menu_highlight_style=("bg_green",),
        menu_cursor_style=("fg_green",)
    )
    menu_entry_index = terminal_menu.show()
    user_selection = options[menu_entry_index]

    print(f"""
You have selected {Back.GREEN}{Fore.BLACK}{user_selection}!{Style.RESET_ALL}
""")

    return user_selection


def main():
    """
    The main entry point for the Hangman game.
    Displays the main menu with options to view instructions, start the game,
    or exit the program. Continuously runs the main menu until the player
    chooses to exit.
    """
    while True:
        user_selection = main_menu()

        if user_selection == "How to Play":
            display_instructions()
        elif user_selection == "Start Game":
            user_selection = select_difficulty()
            word = get_word(user_selection)
            run_game(word)
        elif user_selection == "Exit":
            print("Thank you for playing Hangman! Goodbye!")
            sys.exit()


if __name__ == "__main__":
    main()
