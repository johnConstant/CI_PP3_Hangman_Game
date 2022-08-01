"""
Hangman game created for third project with Code Institute
"""
import time
import random
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


def get_player_name():
    """
    Get player name
    """
    while True:
        name = input("Please enter your name: ")
        try:
            name.isalpha()
            print(Col.BLUE + f"Hello {name}, welcome to Hangman")
            return name
        except ValueError:
            print(Col.RED + 'Only letters can be entered')


def get_word(word_list):
    """
    Choose random word from list of words in imported list
    """
    word = random.choice(word_list)
    return word


def set_difficulty():
    """
    Allow user to choose the difficulty level of the game
    Set the number of guesses allowed based on difficulty selected
    """
    print(" ")
    print('Please enter Easy, Medium or Hard')
    difficulty = input('Please select your difficulty level: ').lower()
    if difficulty == 'easy':
        return 8
    elif difficulty == 'medium':
        return 7
    elif difficulty == 'hard':
        return 6
    else:
        raise ValueError(Col.RED + 'Please enter a valid difficulty level')


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
        guess = input('Please guess a letter: ').lower()
        guessed_letters += guess

        if guess in word:
            print(Col.GREEN + f'Well done {name}! {guess} is in the word')
            correct_guesses += guess
            # https://www.youtube.com/watch?v=8ext9G7xspg
            word_list = [letter if letter in guessed_letters
                         else '_' for letter in word]
            guessed_word = ''.join(word_list)
            print(' ')
            print(f'Current word: {guessed_word}')
            print(' ')

            if word == guessed_word:
                print(Col.GREEN + f'Congratulations {name}, you guessed the\
 correct word, {word}')
                print(' ')
                print("Enter 'y' to play again and 'n' to end the game")
                replay = input('Would you like to play another game: ').lower()
                if replay == 'y':
                    word = get_word(words)
                    play_game(name, word)
                else:
                    break
        else:
            lives -= 1
            print(graphic[lives])
            print(Col.RED + f'Sorry but {guess} is not in the word.')
    else:
        print(' ')
        print('Sorry but that is game over')
        print(' ')
        print("Enter 'y' to play again and 'n' to end the game")
        replay = input('Would you like to play another game: ').lower()
        if replay == 'y':
            word = get_word(words)
            play_game(name, word)
        else:
            exit()


def main():
    """
    Run program functions
    """
    welcome()
    name = get_player_name()
    word = get_word(words)
    play_game(name, word)


main()
