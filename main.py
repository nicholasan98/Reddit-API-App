CLIENT_ID = '63-zKnYTyVco--cIDwLBtA'
SECRET_KEY = 'MLaJTf0CI5SAOk5hPWRbo94oNY-KLQ'

import requests
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

with open('pw.txt', 'r') as f:
    pw = f.read()

with open('user_id.txt', 'r') as f:
    user_id = f.read()

data = {
    'grant_type': 'password',
    'username': user_id,
    'password': pw
}

headers = {'User-Agent': 'MyAPI/0.0.1'}

res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

TOKEN = res.json()

header = {**headers, **{'Authorization': f'bearer {TOKEN}'}}

res = requests.get('https://oauth.reddit.com/r/MobileWallpaper/hot', headers=headers)