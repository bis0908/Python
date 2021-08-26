# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 15:04:02 2021

@author: wonseok
"""

import base64
import requests
import json
import pandas as pd
import os

key_path = os.path.abspath(".\secret.json")
secrets = json.loads(open(key_path).read())

# Twitter API information
client_key = secrets.get('TWITTER_API_KEY')
client_secret = secrets.get('TWITTER_API_SECRET_KEY')

# to make base64 encoding
key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

# Header
auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = { 'grant_type': 'client_credentials'}

auth_resp = requests.post(auth_url, headers = auth_headers, data = auth_data)
print(auth_resp.status_code)

access_token = auth_resp.json()['access_token']
search_headers = { 'Authorization': 'Bearer {}'.format(access_token) }
search_params = {
    'q': '난민',
    'result_type': 'recent',
    'count': 5,
    'lang': 'ko',
    'retryonratelimit': True
}

search_url = '{}1.1/search/tweets.json'.format(base_url)
search_resp = requests.get(search_url, headers = search_headers, params = search_params)

Data = json.loads(search_resp.content)

df = pd.DataFrame(Data['statuses'])
# user column에 사용자 이름이 있어 그 부분만 추출 하고자 함.
# {'id': 851587306809040897, 'id_str': '851587306809040897', 'name': '쌈', 'screen_name': 'foolee_', ~~}
# print(df.values)
df2 = pd.DataFrame(df['user'].values.tolist(), index=df.index)

df['name'] = df2['name']
df['screen_name'] = df2['screen_name']
df = df[['name', 'screen_name', 'text', 'created_at']]
df.to_csv('./twit_results.csv', sep = ',', na_rep = 'NaN', encoding = 'utf-8-sig',
          columns = ['name', 'screen_name', 'text', 'created_at'], index = False)
