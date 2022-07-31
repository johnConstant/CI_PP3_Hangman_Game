"""
Hangman game created for third project with Code Institute
"""
import time


def welcome():
    """
    Show welcome screen
    """
    print("Welcome to:")
    print(" ")
    print("██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██ ")
    print("██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██ ")
    print("███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██ ")
    print("██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██ ")
    print("██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████ ")
    print(" ")
    print(" ")
    print(" ")
    time.sleep(1)


def get_player_name():
    """
    Get player name
    """
    while True:
        name = input("Please enter your name: ")
        try:
            name.isalpha()
            print(f"Hello {name}, welcome to Hangman")
            return name
        except ValueError:
            print('Only letters can be entered')


def set_difficulty():
    """
    Allow user to choose the difficulty level of the game
    Set the number of guesses allowed based on difficulty selected
    """
    print(" ")
    print('Please enter Easy, Medium or Hard', 'red')
    difficulty = input('Please select your difficulty level: ').lower()
    if difficulty == 'easy':
        return 8
    elif difficulty == 'medium':
        return 7
    elif difficulty == 'hard':
        return 6
    else:
        raise ValueError('Please enter a valid difficulty level')


def main():
    """
    Run program functions
    """
    welcome()
    name = get_player_name()


main()
