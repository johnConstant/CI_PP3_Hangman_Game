"""
Validate game inputs
"""


def validate_guess(value):
    """
    Validate user guess
    @param: value should be a single alphabet character
    """
    try:
        # if value.isalpha() == True:
        #     raise ValueError(
        #             "Please enter a letter"
        #         )
        if len(value) > 1:
            raise ValueError(
                    f"You entered {value}, please only enter one letter"
                )
    except ValueError as err:
        print(f"Invalid data: {err}, please try again")
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
                    f"You entered {value}, please enter \
{' or '.join(values_list)}"
                )
    except ValueError as err:
        print(f"Invalid data: {err}, please try again")
        return False
    return True
