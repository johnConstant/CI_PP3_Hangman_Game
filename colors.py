"""
Add colour to terminal
"""
from colorama import init

# Initializes Colorama
init(autoreset=True)


class Color:
    """
    Declare colour values
    """
    RED = "\033[1;31;48m"
    GREEN = "\033[1;32;48m"
    BLUE = "\033[1;34;48m"
