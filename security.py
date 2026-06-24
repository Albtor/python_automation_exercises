import os
import pickle
import google.auth
from flask import Request

# from google_auth_oauthlib.flow import installed AppFlow
# from googleapiclient.discovery import build

api_key = os.getenv('API_KEY_DUMMY')

# pip install google-auth google-auth-oautlhlib google-auth-httplib2 google-api-ython-client


def oauth20_authentication():
    SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
    def authenticate():
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        return creds

    def list_events():
        print('Listing events')

