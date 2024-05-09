# discord imports
from discord.ext import commands
import discord

# other imports 
import random

class Dice(commands.Cog):  
    def __init__(self, bot): 
        self.bot = bot  

# roll command 
    @commands.command()
    async def roll(self, ctx):
        result = random.randint(1, 6)
        embed = discord.Embed(
            title="🎲 Dice Roll",
            description=f"**Result:** You rolled a `{result}`!",
            color=discord.Color.blurple()
        )
        await ctx.send(embed=embed)

# setup function
async def setup(bot):
    await bot.add_cog(Dice(bot))