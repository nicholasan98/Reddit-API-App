import requests
import json
import pandas as pd


# Client ID and Secret Key from reddit's api account
CLIENT_ID = '63-zKnYTyVco--cIDwLBtA'
SECRET_KEY = 'MLaJTf0CI5SAOk5hPWRbo94oNY-KLQ'

# these next 3 with methods open different .txt files that can be sent in
with open('pw.txt', 'r') as f:
    pw = f.read()

with open('user_id.txt', 'r') as f:
    user_id = f.read()

with open('subreddit.txt', 'r') as f:
    subreddit = f.read()    


# authorization types and data given below
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

data = {
    'grant_type': 'password',
    'username': user_id,
    'password': pw
}

headers = {
    'User-Agent': 'YourApp/1.0 by YourUsername'
}

res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

TOKEN = res.json()

headers["Authorizaton"] = f"bearer {TOKEN}"

url = f'https://oauth.reddit.com/r/{subreddit}/hot'
res = requests.get(url, headers=headers)

if res.status_code == 200:
    # Successful response, parse JSON and print posts
    data = res.json().get('data', {}).get('children', [])
    if data:
        post_titles = [post['data']['title'] for post in data]
        df = pd.DataFrame({'Title': post_titles})
        print(df)
    else:
        print("No posts found in the response.")
else:
    # Handle errors
    print(f"Error: {res.status_code}")
    print(res.text)  # Print the response for debugging purposes