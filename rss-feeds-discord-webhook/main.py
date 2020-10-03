from json import load
from utility import generate_feed,discord_dict,file_handling,post_it
with open("feed_links.json","r") as input_file:
    links = load(input_file)
for key in links.keys():
    entry = generate_feed(links[key])
    discord_content = discord_dict(key,entry)
    flag = file_handling(key,entry)
    if flag:
        post_it(discord_content)