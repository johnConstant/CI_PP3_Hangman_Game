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


def create_account():
    """
    Get username from player
    """
    username = input("Please enter your username: ")
    password = input("Please enter a password: ")
    details = [username, password]
    print('Creating account...')
    worksheet = SHEET.worksheet('auth_details')
    worksheet.append_row(details)
    print(f'Thank you {username}, your account has been created.')


create_account()
