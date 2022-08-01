'''Import gspread and Google OAuth modules'''
import gspread
from google.oauth2.service_account import Credentials
from email_validator import validate_email, EmailNotValidError
from colors import Color as Col


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_auth')


def validate_user_email(email):
    """
    Validate the email address.
    It must be of the form name@example.com
    @param email: Player's email address
    """
    try:
        validate_email(email)
        return False
    except EmailNotValidError as error:
        print(Col.RED + "\n" + str(error))
        print(Col.RED + "Please try again.\n")
        return True


def get_details():
    """
    Get login details from user
    """
    print("\nWelcome back, please log in to continue")
    while True:
        username = input("Please enter your email address: ")
        validate_user_email(username)
        break
    name = input("Please enter your name: \n").lower()
    password = input("Please enter a password: \n")
    return [username, name, password]


def create_account():
    """
    Get username from player
    """
    details = get_details()
    data = SHEET.worksheet('auth_details').get_all_values()
    if details in data:
        print(Col.RED + "Sorry but an account already exists with this email")
        print(Col.RED + "Please log in with existing account")
        exit()
    print('Creating account...')
    worksheet = SHEET.worksheet('auth_details')
    worksheet.append_row(details)
    print(Col.BLUE + f'Thank you {details[1].capitalize()}, your account has\
 been created.')
    return details


def login():
    """
    Get username from player
    """
    login_details = get_details()
    data = SHEET.worksheet('auth_details').get_all_values()
    if login_details not in data:
        print(Col.RED + "Couldn't find your account")
        exit()
    for account in data:
        if account == login_details:
            print(Col.GREEN + 'Logged in')
            return account
