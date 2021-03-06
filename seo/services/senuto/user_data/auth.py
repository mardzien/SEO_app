import requests
import json

url = "https://api.senuto.com//api/users/token.json"


def load_auth():
    with open("auth.json") as fh:
        result = json.load(fh)
    return result


def get_token():
    login_data = load_auth()
    r = requests.post(url, data=login_data)
    # loading json users data for token
    user_data = json.loads(r.text)
    # getting token
    token = user_data['data']['token']
    return token
