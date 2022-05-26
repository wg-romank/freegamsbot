import discord
import os
from discord.ext import commands, tasks
from datetime import datetime, time, timedelta

 # look at grabfreegames.com and grab games
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getTitles(result):
    url = "https://grabfreegames.com/"

    try:
       page = urlopen(url)
    except:
       print("Error opening the URL")

    soup = BeautifulSoup(page, 'html.parser')

    content = soup.find('div', {"class": "freebies row break-on-4"})

    for i in content.findAll('div'):
        for x in i.findAll('div', {"class": "free-title"}):
            for a in x.findAll('a', href=True):
                if 'Free Steam Game' in x.text:
                    result = result + ' ' +  x.text + '    -    ' + str(a['href'])
                if 'Free Epic Games Game' in x.text:
                    result = result + ' ' +  x.text + '    -    ' + str(a['href'])
                if 'Free GOG Game' in x.text:
                    result = result + ' ' +  x.text + '    -    ' + str(a['href'])
                    
    return str(result)

###########


# discord creds
TOKEN = os.environ['DISCORD_TOKEN']

target_channel_idXOX = 939170953290719322
target_channel_idMIN = 936999636625940540
##############

bot = commands.Bot("!")

@tasks.loop(count=1)
async def do_its_thing():
        await bot.wait_until_ready()

        message_channel = bot.get_channel(target_channel_idXOX)
        print(f"Got channel {message_channel}")
        # await message_channel.send(getTitles("xox"))
        t = getTitles("xox")
        print(f"mc {t} {message_channel}")

        message_channel = bot.get_channel(target_channel_idMIN)
        print(f"Got channel {message_channel}")
        # await message_channel.send(getTitles("min"))
        t = getTitles("min")
        print(f"mc {t} {message_channel}")

        await bot.close()


if __name__ == '__main__':
    do_its_thing.start()
    bot.run(TOKEN)