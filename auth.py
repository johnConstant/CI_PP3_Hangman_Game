'''Import gspread and Google OAuth modules'''
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_auth')


def get_details():
    """
    Get login details from user
    """
    username = input("Please enter your email address: ")
    name = input("Please enter your name: ")
    password = input("Please enter a password: ")
    return [username, name, password]


def create_account():
    """
    Get username from player
    """
    details = get_details()
    print('Creating account...')
    worksheet = SHEET.worksheet('auth_details')
    worksheet.append_row(details)
    print(f'Thank you {details[0]}, your account has been created.')
    return details


def login():
    """
    Get username from player
    """
    login_details = get_details()
    data = SHEET.worksheet('auth_details').get_all_values()
    for account in data:
        if account == login_details:
            print('Logged in')
            return account
