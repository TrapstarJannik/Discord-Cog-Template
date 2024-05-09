# discord imports
from discord.ext import commands
from discord import app_commands
import discord

# other imports 
import random

class Dice2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# roll slash command
    @app_commands.command(name="roll", description="🎲 roll a dice")
    async def roll(self, interaction):
        result = random.randint(1, 6)
        embed = discord.Embed(
            title="🎲 Dice Roll",
            description=f"**Result:** You rolled a `{result}`!",
            color=discord.Color.blurple()
        )
        await interaction.response.send_message(embed=embed)

# setup function
async def setup(bot):
    await bot.add_cog(Dice2(bot))