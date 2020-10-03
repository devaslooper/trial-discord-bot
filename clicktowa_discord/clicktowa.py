import discord
import os
from utils import cwa
client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('CWA!'):
        arg = str(message.content).split("!")[1]
        string = cwa(arg)
        await message.channel.send(string)
client.run(os.getenv("DISCORD_BOT_TOKEN"))
