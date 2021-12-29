import discord
from discord import channel
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json,asyncio,datetime

class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        async def interval():
            await self.bot.wait_untial_ready()
            self.channel = self.bot.get_channel(920930478729596928) 
            while not self.bot.is_cloesd():
                await self.channel.send('呱，我在')
                await asyncio.sleep(5)#單位：秒

        self.bg_task=self.bot.loop.creat_task(interval())

def setup(bot):
    bot.add_cog(Task(bot))
  