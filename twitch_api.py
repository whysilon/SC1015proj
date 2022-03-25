from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope
import pandas as pd
from csv import DictWriter

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
print(stream_info)

headers = ['id', 'user_id', 'user_login', 'user_name', 'game_id', 'game_name', 'type', 'title', 'viewer_count', 'started_at', 'language', 'thumbnail_url', 'tag_ids', 'is_mature']

data = stream_info['data']

with open('twitch_data.csv', 'w', newline='') as f:
    d = DictWriter(f, fieldnames=headers)
    d.writeheader()
    d.writerows(data)
    f.close()
