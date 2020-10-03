from feedparser import parse
from requests import post
from os import getenv
from json import load, dump
def generate_feed(url):
    Feed = parse(url)
    entry = Feed.entries[0]
    return entry
def post_it(input_data):
    hook = getenv("HOOK")
    post(hook,input_data)
def file_handling(name, data):
    flag = False
    with open("datafile.json","r") as ip:
        existing_data = load(ip)
    try:
        if existing_data[name]['link'] != data['link']:
            existing_data[name] = data
            with open("datafile.json","w") as op:
                dump(existing_data,op,indent=4)
            flag = True
        return flag
    except:
        existing_data[name] = data
        with open("datafile.json","w") as op:
            dump(existing_data,op,indent=4)
        flag = True
        return flag
def discord_dict(name, entry):
    output_data = {}
    output_data["username"] = name
    output_data["content"] =entry["title"]+" \n "+entry["link"]
    return output_data