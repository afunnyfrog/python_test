import discord
from discord import channel
from discord.ext import commands
from core.classes import Cog_Extension, commands
import random
import json 

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata =json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(int(jdata["Welcome_channel"]))
        await channel.send(f'{member} 歡迎你進來呱呱')
#歡迎訊息

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(int(jdata["Leave_channel"]))
        await channel.send(f'{member} 趕快走吧呱呱')
#再見訊息 

   

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = jdata["Keyword"]
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send("找我有事嗎owo")

def setup(bot):
    bot.add_cog(Event(bot))