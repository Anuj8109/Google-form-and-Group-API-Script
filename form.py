from __future__ import print_function
import os.path
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools
import io

import group

SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage('token.json')
creds = None
## We login every time in authentication not save token for security puspose
# if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#         print(creds)
if not creds or not creds.valid:
    flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
    creds = tools.run_flow(flow, store)

service = discovery.build('forms', 'v1', credentials=creds, discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

# Prints the responses of your specified form:
form_id = '11ZRHWXVtCpe9nH9IY-bI5Mo4jPjY5utMKptqiIqXPZU'
f = open('date.txt','r') #date where we want results
N = f.readline()
N = str(N)
## Few times filter not work beacause of incorrect timestamp format and timestamp must be formatted in RFC3339 UTC "Zulu" format
result = service.forms().responses().list(formId=form_id,filter = {'timestamp' > N}).execute()
emails = []
print(result['responses'])
for res in result["responses"]:
    a = res["answers"]["78e036d7"]["textAnswers"]["answers"][0]['value']
    emails.append(a)
print(emails)
file1 = open('date.txt','w')
file1.write(N) #date for next time script run
file1.close()
group.main(emails) # Call group python file to excute for Add these gmails in group
