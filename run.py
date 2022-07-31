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

   
def main():
    """
    Run program functions
    """
    welcome()


main()
