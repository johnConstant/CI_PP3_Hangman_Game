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


def main():
    """
    Run program functions
    """
    welcome()
    name = get_player_name()


main()
