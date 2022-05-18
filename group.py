from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ['https://apps-apis.google.com/a/feeds/groups/','https://www.googleapis.com/auth/admin.directory.group','https://www.googleapis.com/auth/admin.directory.user.readonly']

def main(emails):
    # print(emails)
    creds = None
   
    if os.path.exists('token1.json'):
        creds = Credentials.from_authorized_user_file('token1.json', SCOPES)
        print(creds)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secrets.json', SCOPES)
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token1.json', 'w') as token:
            token.write(creds.to_json())
    
    service = build('admin', 'directory_v1', credentials=creds)


    # body = {
    #      "primaryEmail": "uma04599@example.com".format(firstname="Uma", secondname="04599"),
    #    }

    # # Execute Add User
    # user_add = service.users().insert(body=body).execute()

    # body_group = {"email": "uma04599@example.com".format(firstname="Uma", secondname="04599")}
    # add_group = service.members().insert(body=body_group).execute()
    for email in emails:
        group_result = service.groups().insert(body={
                            'groupKey': 'elitmus798', # group key
                            'email': email # user email who need to insert in google groups
                        }).execute() 

# main(["abc@gmail.com","fun@gmail.com"])