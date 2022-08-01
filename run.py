"""
Hangman game created for third project with Code Institute
"""
import time
import random
import auth
from validate_inputs import validate_guess, validate_list
from colors import Color as Col
from hangman import graphic
from words import words


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


def start_game():
    """
    Check if player is logged in
    If not create account for player
    """
    while True:
        print('Have you played this game before?')
        answer = input("Enter 'y' for Yes and 'n' for No: ").lower()
        validate_list(answer, ['y', 'n'])
        if answer == 'y':
            details = auth.login()
            return details
        if answer == 'n':
            print('\nPlease create an account to continue')
            details = auth.create_account()
            return details


def get_word(word_list):
    """
    Choose random word from list of words in imported list
    @param word_list: list of strings
    """
    word = random.choice(word_list)
    return word


def set_difficulty():
    """
    Allow user to choose the difficulty level of the game
    Set the number of guesses allowed based on difficulty selected
    """
    while True:
        print(" ")
        print('Please enter Easy, Medium or Hard')
        difficulty = input('Please select your difficulty level: ').lower()
        validate_list(difficulty, ['easy', 'medium', 'hard'])
        if difficulty == 'easy':
            return 8
        elif difficulty == 'medium':
            return 7
        elif difficulty == 'hard':
            return 6


def end_game(name):
    print(' ')
    print("Enter 'y' to play again and 'n' to end the game")
    replay = input('Would you like to play another game: ')\
        .lower()
    validate_list(replay, ['y', 'n'])
    if replay == 'y':
        word = get_word(words)
        play_game(name, word)
    elif replay == 'n':
        print(Col.BLUE + f"\nGoodbye {name.capitalize()}\n")
        exit()


def play_game(name, word):
    """
    Start game loop
    """
    # lives = 6
    lives = set_difficulty()
    guessed_letters = []
    correct_guesses = []
    word_list = list(word.strip(" "))
    print('_ ' * len(word))
    print(word)

    while lives > 0:
        while True:
            guess = input('Please guess a letter: ').lower()
            if validate_guess(guess):
                break
        guessed_letters += guess
        if guess in word:
            print(Col.GREEN + f'Well done {name}! {guess} is in the word')
            correct_guesses += guess
            print(graphic[lives])
            word_list = [letter if letter in guessed_letters
                         else '_' for letter in word]
            guessed_word = ''.join(word_list)
            print(' ')
            print(f'Current word: {guessed_word}')
            print(' ')

            if word == guessed_word:
                print(Col.GREEN + f'Congratulations {name.capitalize()}, you \
guessed the correct word, {word}')
                while True:
                    end_game(name)
        else:
            lives -= 1
            print(graphic[lives])
            print(Col.RED + f'Sorry but {guess} is not in the word.')

    end_game(name)


def main():
    """
    Run program functions
    """
    welcome()
    # name = get_player_name()
    player_details = start_game()
    word = get_word(words)
    play_game(player_details[1], word)


main()
