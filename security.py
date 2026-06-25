import datetime
import os
import pickle
import time
import google.auth
from flask import Request
from sqlalchemy.event.base import _HasEventsDispatch
from tensorflow.python.autograph.pyct.cfg import build

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
        creds = authenticate()
        try:
            service = build('calendar', 'v3', credentials=creds)
            events_result = service.events().list(calendarId='primary', timeMin=datetime.datetime.utcnow().isoformat(),
                                                  maxResults=10, singleEvents=True, orderBy='startTime').execute()
            events = events_result.get('items', [])
            if not events:
                print('No upcoming events found.')
                for event in events:
                    start = event['start'].get('dateTime', events['start'].get('date'))
                    print(f'{start}-{event["summary"]}')
        except Exception as error:
            print(f"An error occured: {error}")


    list_events()

