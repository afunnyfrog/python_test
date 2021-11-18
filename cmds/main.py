import discord
from discord import channel
from discord.ext import commands
from core.classes import Cog_Extension
from datetime import datetime,timezone,timedelta

from datetime import datetime, timedelta, timezone
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
time =utc_dt.strftime("%Y-%m-%d %H:%M:%S")
class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')
    #對話時機器人的延遲 

    @commands.command()
    async def frog(self,ctx):
        await ctx.send("早安你好")

    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="簡介", url="https://linktr.ee/wang_chao_zong",
             description="神奇的地方", color=0xe0ffc2, 
            timestamp=time)
        embed.set_author(name="青蛙", url="https://discord.gg/4Y2XPxf5nn", icon_url="https://upload.wikimedia.org/wikipedia/zh/thumb/6/6f/Icon_of_%E6%97%85%E3%81%8B%E3%81%88%E3%82%8B_20180122.png/220px-Icon_of_%E6%97%85%E3%81%8B%E3%81%88%E3%82%8B_20180122.png")
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/zh/thumb/6/6f/Icon_of_%E6%97%85%E3%81%8B%E3%81%88%E3%82%8B_20180122.png/220px-Icon_of_%E6%97%85%E3%81%8B%E3%81%88%E3%82%8B_20180122.png")
        embed.add_field(name="1", value="1", inline=True)
        embed.add_field(name="2", value="12", inline=True)
        embed.add_field(name="3", value="123", inline=True)
        embed.add_field(name="4", value="1234", inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Main(bot))