from pypresence import Presence
import time

client_id="YOUR_CLIENT_ID" #Replace YOUR_CLIENT_ID with your client ID
RPC=Presence(client_id)
RPC.connect()
while True:
    x=open('SNIP.TXT_LOCATION', 'r') #Replace SNIP.TXT_LOCATION with the location of your Snip.txt file
    song=x.read()
    search=song.replace(" ", "%20")
    search_term=("https://music.apple.com/gb/search?term="+search)
    if len(search_term)<=128:
        print(RPC.update(state=song, details="Listening to:", buttons=[{"label": "Listen Along", "url":"https://music.apple.com/gb/search?term="+search}]))
    else:
        print(RPC.update(state=song[0:127], details="Listening to:"))
    time.sleep(3)