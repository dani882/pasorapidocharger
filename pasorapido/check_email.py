from apiclient import errors
import email
import base64
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import client, file, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

# Import my credentials setting from config file
# email = config.FROM_EMAIL


def get_credentials():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    return service


def ListMessagesMatchingQuery(service, user_id, query=''):
    """List all Messages of the user's mailbox matching the query.

    Args:
      service: Authorized Gmail API service instance.
      user_id: User's email address. The special value "me"
      can be used to indicate the authenticated user.
      query: String used to filter messages returned.
      Eg.- 'from:user@some_domain.com' for Messages from a particular sender.

    Returns:
      List of Messages that match the criteria of the query. Note that the
      returned list contains Message IDs, you must use get with the
      appropriate ID to get the details of a Message.
    """
    try:
       # service = get_credentials()
        response = service.users().messages().list(userId=user_id,
                                                   q=query).execute()

        if 'messages' in response:
            return response['messages'][0]['id']
        return None

    except errors.HttpError as error:
        print(f'An error occurred: {error}')
        return None



def GetMessage(service, user_id, msg_id):
    """Get a Message with given ID.

    Args:
      service: Authorized Gmail API service instance.
      user_id: User's email address. The special value "me"
      can be used to indicate the authenticated user.
      msg_id: The ID of the Message required.

    Returns:
      A Message.
    """

    try:
        message = service.users().messages().get(userId=user_id, id=msg_id).execute()
        return message['snippet'][85:91]
    except errors.HttpError as error:
        print(f'An error occurred: {error}')
        return None

service = get_credentials()
user_id = "dani882@gmail.com"
FROM = "no-reply@pasorapido.com"
msg_id = ListMessagesMatchingQuery(service, user_id, FROM)

print(int(GetMessage(service, user_id, msg_id)))
