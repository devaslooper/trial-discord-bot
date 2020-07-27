import requests
import json
import os
key = os.getenv('YT')
hook = os.getenv('DC')
channel_id = "UCBJycsmduvYEL83R_U4JriQ"
request = requests.get(f"https://www.googleapis.com/youtube/v3/search?key={key}&part=snippet&channelId={channel_id}&order=date&maxResults=1")
data = request.json()
with open("YT.json","r") as io:
    loaddata = json.load(io)
if data['items'][0]['id']['videoId'] != loaddata['items'][0]['id']['videoId']:
    videoURL = "https://www.youtube.com/watch?v="+data['items'][0]['id']['videoId']
    title = data['items'][0]['snippet']['title']
    channelTitle = data['items'][0]['snippet']['channelTitle']
    requests.post(f"{hook}",data={"content":f"Most recent {channelTitle} video: {title} at {videoURL}"})

with open("YT.json","w+") as f:
    json.dump(data,f)
