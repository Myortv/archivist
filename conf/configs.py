import logging
import os
import discord

from discord.ext import commands, tasks
from dotenv import load_dotenv
import demjson

load_dotenv()
TOKEN = os.getenv('DISCORD_ARCHIVE_BOT_TOKEN')
GUILDS = os.getenv('DISCORD_CONNECTED_GUILDS')
DEBUG = os.getenv('DEBUG')


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(BASE_DIR,'descriptions.json'),'r') as file:
    DESCRIPTIONS = demjson.decode(file.read())


logging.basicConfig(level=logging.INFO)

LOCATIONS_CATEGORY_ID = 980934432980615178


bot =  commands.Bot(command_prefix='!', intents=discord.Intents.all())
