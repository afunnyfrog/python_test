import discord
from discord import channel
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json,asyncio,datetime
with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata =json.load(jfile)
class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        async def interval():
            user_id=927316051887276082
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(927359811081871470)
            while not self.bot.is_closed():
                await self.channel.send(f"disconect")
                await asyncio.sleep(60)#單位：秒

        self.bg_task = self.bot.loop.create_task(interval())
 
    @commands.command()
    async def set_channel(self,ctx,ch:int):
        self.channel = self.bot.get_channel(ch) 
        await ctx.send(f'設定頻道:{self.channel.mention}')

def setup(bot):
    bot.add_cog(Task(bot))
