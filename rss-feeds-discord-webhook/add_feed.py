from json import load,dump
from os import path
key = input("Title: ")
feed_url = input("URL: ")
if path.isfile("feed_links.json"):
    with open("feed_links.json","r") as f:
        data = load(f)
    data[key] = feed_url
else:
    data = {}
    data[key] = feed_url
with open("feed_links.json","w") as f:
    dump(data,f,indent=4)