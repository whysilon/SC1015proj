from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope
import pandas as pd
from csv import DictWriter
import csv
import os
import random


app_id = 'oatab7pvysht8ho60uwl3qft7iapy0'
app_secret = 'gh70o6bplxah7aiiq8xoyof7woii59'   
twitch = Twitch(app_id, app_secret)

target_scope = [AuthScope.BITS_READ]
auth = UserAuthenticator(twitch, target_scope, force_verify=False)
# this will open your default browser and prompt you with the twitch verification website
token, refresh_token = auth.authenticate()
# add User authentication
twitch.set_user_authentication(token, target_scope, refresh_token)

'''
randList = []
while(len(randList) != 5):
    randNum = random.randint(1,500)
    if randNum not in randList:
        randList.append(randNum)
print(randList)
'''
i = 0
view_count = []
data = []
cursor = ''
for var in range(100):
    stream_info = twitch.get_streams(first=100,after=cursor)
    cursor = stream_info['pagination']['cursor']
    #if (var == i * 25):
    print("Update number:",i+1)
    for k in range(25):
        data.append(stream_info['data'][k])
    uid = []
    try:
        for l in range(25):
            uid.append(stream_info['data'][l]['user_login'])
    except IndexError:
        print("Error occured, Index Number:",l)
    temp = twitch.get_users(logins = uid)
    view_count += temp['data']
    l = 0
    i += 1

        
filename = 'test_data.csv'
headers = ['id', 'user_id', 'user_login', 'user_name', 'game_id', 'game_name', 'type', 'title', 'viewer_count', 'started_at', 'language', 'thumbnail_url', 'tag_ids', 'is_mature', 'follow_count','total_views']


fileEmpty = os.stat(filename).st_size == 0


with open(filename, 'a', newline = '', encoding="utf-8") as f:
    d = DictWriter(f, fieldnames=headers)
    print("lmao")
    if fileEmpty:
        d.writeheader()
    #print(type(data))
    for number,row in enumerate(data):
        print("count",number+1)
        for count,num in enumerate(view_count):
            if row['user_id'] == view_count[count]['id']:
                row['total_views'] = view_count[count]['view_count']
                break;
        follow_count = twitch.get_users_follows(to_id=row['user_id'])
        row['follow_count'] = follow_count['total']
    print('done')
    d.writerows(data)
    f.close
