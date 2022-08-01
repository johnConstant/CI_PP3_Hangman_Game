"""
Validate game inputs
"""
from colors import Color as Col


def validate_guess(value):
    """
    Validate user guess
    @param: value should be a single alphabet character
    """
    try:
        if not value.isalpha():
            raise TypeError(
                    "Please enter a letter"
                )
        elif len(value) > 1:
            raise ValueError(
                    Col.RED + f"You entered {value}, please only enter one\
 letter at a time"
                )
    except ValueError as err:
        print(Col.RED + f"Invalid data: {err}, please try again")
        return False
    return True


def validate_list(value, values_list):
    """
    Validate user guess
    @param: value should be a single alphabet character
    """
    try:
        if value not in values_list:
            raise ValueError(
                    Col.RED + f"You entered {value}, please enter \
{' or '.join(values_list)}"
                )
    except ValueError as err:
        print(Col.RED + f"\nInvalid data: {err}, please try again\n")
        return False
    return True
