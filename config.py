import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
API_URL_USER = os.getenv('API_URL_USER')
API_URL_SUB = os.getenv('API_URL_SUB')
PREMIUM_AMOUNT = 10
PLATINUM_AMOUNT = 20
USER_PROFILE = os.getenv('USER_PROFILE')
TELEBIRR_IMG = os.getenv('TELEBIRR_IMG')
CBEBIRR_IMG = os.getenv('CBEBIRR_IMG')

firebaseConfig = {
    "apiKey": os.getenv('apiKey'),
    "authDomain": os.getenv('authDomain'),
    "databaseURL": os.getenv('databaseURL'),
    "projectId": os.getenv('projectId'),
    "storageBucket": os.getenv('storageBucket'),
    "messagingSenderId": os.getenv('messagingSenderId'),
    "appId": os.getenv('appId'),
    "measurementId": os.getenv('measurementId')
}
