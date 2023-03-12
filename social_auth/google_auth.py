from google.oauth2 import id_token
from google.auth.transport import requests
from google.oauth2.credentials import Credentials


def get_id_token_from_google(client_id, client_secret, authorization_code):
    """
    Given a Google client ID, client secret, and authorization code, returns an ID token.
    """
    credentials = Credentials.from_authorized_user_info(
        info={
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uri': 'https://www.google.com/',
            'scope': ['openid', 'email', 'profile']
        }
    )
    token_response = credentials.fetch_token(
        authorization_response=authorization_code
    )

    id_token = token_response.get("id_token")
    if id_token is None:
        raise ValueError("No ID token found in token response")
    return id_token

def get_access_token_from_google(_client_id, _id_token):
    try:
        id_info = id_token.verify_oauth2_token(_id_token, requests.Request(), _client_id)
        if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')
        access_token = id_info["sub"]
    except ValueError:
        access_token = None
    return access_token

# Collecting authorization code from postman using client_id and secret key
client_id = "461023473322-pl8omk5hq8lcnpl6u50jvbpe70prijb1.apps.googleusercontent.com"
client_secret = "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"
authorization_code = "4%2F0AWtgzh5dVfinchjnGCefiVw17w7ONmihkJLu_fJDdFzLNpaamtJeqniXVDPue6OyYYk0zg"
print(get_id_token_from_google(client_id,client_secret,authorization_code))