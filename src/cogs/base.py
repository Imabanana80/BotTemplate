import discord
from discord import app_commands
from discord.ext import commands



class Base(commands.Cog):
    def __init__(self, client):
        self.client: discord.Client = client
    
    @app_commands.command(name="ping", description="ping the bot")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.defer()
        await interaction.followup.send("Pong!")
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.client.user}')
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="(/) Commands"))

    
    


async def setup(client: commands.Bot) -> None:
    await client.add_cog(Base(client))