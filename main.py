# discord Imports
from discord.ext import commands
import discord

# other imports
import asyncio
import json
import os

# load onfig file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# bot configs 
TOKEN = config['token'] # <-- changeable, in config.json
PREFIX = config['prefix'] # <-- changeable in config.json

# bot = variable for commands/events, prefix ".", permissions "all"
bot = commands.Bot(command_prefix=PREFIX, intents = discord.Intents.all()) # <-- set your PREFIX in config.json 

# start message 
@bot.event
async def on_ready():
    await bot.tree.sync() # <-- sync slash commands on start
    print(f"Logged in as {bot.user.name}") # <-- bot name
    print(f"Bot ID: {bot.user.id}") # <-- bot ID
    print("Bot is ready.") # <-- ready message

# cogs loading
async def main():
    async with bot:
        # load .py files out of the extentions folder
        for filename in os.listdir('./extensions'): # <-- folder name
            if filename.endswith('.py'): # <-- checking if the file ends with .py
                await bot.load_extension(f'extensions.{filename[:-3]}') # <-- remove the last 3 characters (.py)
        await bot.start(TOKEN) # <-- set your token in config.json 

# run main.py
if __name__ == '__main__': # <-- checks if name = main
    asyncio.run(main()) # <-- run main
