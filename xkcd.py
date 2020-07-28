import requests
from bs4 import BeautifulSoup
import json
import os
with open("xkcdlog.json","r") as ipfile:
    index = int(json.load(ipfile))
xkcd = requests.get("https://xkcd.com/"+str(index))
if xkcd.status_code == 200:
    soup = BeautifulSoup(xkcd.text,features="html.parser")
    comic = soup.find("div",{"id":"comic"})
    comic_url = "https:"+comic.img["src"]
    alt_text = comic.img["title"]
    content = "XKCD "+str(index)+f"\n{alt_text}\n{comic_url}"
    disc_url = os.getenv("XKCD")
    if disc_url[0] !='h':
        disc_url='https://'+disc_url
    requests.post(disc_url,data={"content":f"{content}"})
    index+=1
    with open("xkcdlog.json","w+") as opfile:
        json.dump(index,opfile)
