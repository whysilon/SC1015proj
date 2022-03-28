from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope
import pandas as pd
from csv import DictWriter
import csv
import os.path

app_id = 'oatab7pvysht8ho60uwl3qft7iapy0'
app_secret = 'gh70o6bplxah7aiiq8xoyof7woii59'   
twitch = Twitch(app_id, app_secret)

target_scope = [AuthScope.BITS_READ]
auth = UserAuthenticator(twitch, target_scope, force_verify=False)
# this will open your default browser and prompt you with the twitch verification website
token, refresh_token = auth.authenticate()
# add User authentication
twitch.set_user_authentication(token, target_scope, refresh_token)

stream_info = twitch.get_streams(first=100)

#print(stream_info)

filename = 'twitch_data.csv'
headers = ['id', 'user_id', 'user_login', 'user_name', 'game_id', 'game_name', 'type', 'title', 'viewer_count', 'started_at', 'language', 'thumbnail_url', 'tag_ids', 'is_mature', 'follow_count','total_views']

data = stream_info['data']

fileEmpty = os.stat(filename).st_size == 0

with open(filename, 'a', newline='') as f:
    d = DictWriter(f, fieldnames=headers)
    if fileEmpty:
        d.writeheader()
    #print(type(data))
    for row in data:
        #print(row['user_id'])
        follow_count = twitch.get_users_follows(to_id=row['user_id'])
        view_count = twitch.get_users(logins=row['user_login'])
        row['total_views'] = view_count['data'][0]['view_count']
        row['follow_count'] = follow_count['total']
    print('done')
    d.writerows(data)
    f.close()
