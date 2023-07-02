import os
import discord
import json
from discord.ext import commands, tasks
from dotenv import load_dotenv
from itertools import cycle

load_dotenv()

class Client(commands.Bot):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents, command_prefix=commands.when_mentioned_or('>'))

    async def setup_hook(self):                 
        with open("./src/config.json", 'r') as df:
            cogs = json.load(df)['cogs']
        for ext in cogs:
            try:
                await client.load_extension(f'cogs.{ext}')
                print(f"Loaded cog: {ext}")
            except commands.errors.ExtensionNotFound:
                print(f"Cog doesn't exist: {ext}")
        await self.tree.sync()

intents = discord.Intents(messages=True)
intents.guilds = True
client = Client(intents=intents)

client.run(os.getenv("TOKEN"))

