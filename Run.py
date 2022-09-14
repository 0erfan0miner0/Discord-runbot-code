import os
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix= "m!")

@client.event
async def on_ready():
    print('Bot Run Shod')


client.run(TOKEN)
