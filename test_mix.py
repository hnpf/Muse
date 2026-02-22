import json
from ytmusicapi import YTMusic
with open("data/headers_auth.json") as f:
    headers = json.load(f)
yt = YTMusic(auth=headers)

mix_id = "VLRDTMAK5uy_kset8DisdE7LSD4TNjEVvrKRTmG7a56sY"
mix_res = yt.get_watch_playlist(playlistId=mix_id)
# Print the first track fully
import pprint
pprint.pprint(mix_res['tracks'][0])
