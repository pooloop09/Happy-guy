import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import time

intents = discord.Intents.all()
intents.members = True

TOKEN = "MTE3NjcwNDMxMzU1MzMyMjA0NQ.GdGRCF.E3nmc0YFBuaUfb0BJ0g-YNCqnfoJSL29rPLWgc"

client = commands.Bot(command_prefix= "!", intents=intents)
url = "https://ipv4.icanhazip.com/"
html = requests.get(url)
IP = BeautifulSoup(html.content, "html.parser")

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")
    while 1:
        channel = client.get_channel(1078774075859665106)
        await channel.send(str(IP))
        time.sleep(3600)

client.run(TOKEN)