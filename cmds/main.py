from email import utils
from sqlite3 import Timestamp
import discord
from discord import channel,utils
from discord.ext import commands
from core.classes import Cog_Extension
from datetime import datetime as dt,timezone,timedelta
import random



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
            timestamp=dt.utcnow())
        embed.set_author(name="青蛙", url="https://discord.gg/4Y2XPxf5nn", icon_url="https://upload.wikimedia.org/wikipedia/zh/thumb/6/6f/Icon_of_%E6%97%85%E3%81%8B%E3%81%88%E3%82%8B_20180122.png/220px-Icon_of_%E6%97%85%E3%81%8B%E3%81%88%E3%82%8B_20180122.png")
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/zh/thumb/6/6f/Icon_of_%E6%97%85%E3%81%8B%E3%81%88%E3%82%8B_20180122.png/220px-Icon_of_%E6%97%85%E3%81%8B%E3%81%88%E3%82%8B_20180122.png")
        embed.add_field(name="1", value="1", inline=True)
        embed.add_field(name="2", value="12", inline=True)
        embed.add_field(name="3", value="123", inline=True)
        embed.add_field(name="4", value="1234", inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)

    @commands.command()
    async def rand_squad(self,ctx):

        online=[]

        for member in ctx.guild.members:
            print(member,member.status)
            if str(member.status) == "online" and member.bot == False:
                online.append(member.name)

        randon_online=random.sample(online,k=20)
        for squad in range(4):
            group=random.sample(randon_online,k=5)
            await ctx.send(f"第{squad+1}小隊：",str(group))
            for name in group:
                randon_online.remove(name)

    @commands.group()
    async def 顏文字(self,ctx):
        pass

    @顏文字.command()
    async def owob(self,ctx):
        await ctx.send("owob")     

    @顏文字.command()
    async def ouob(self,ctx):
        await ctx.send("ouob")   

    @顏文字.command()
    async def ovob(self,ctx):
        await ctx.send("ovob")   

def setup(bot):
    bot.add_cog(Main(bot))