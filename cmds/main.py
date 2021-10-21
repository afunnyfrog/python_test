import discord
from discord import channel
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')
    #對話時機器人的延遲 

def setup(bot):
    bot.add_cog(Main(bot))