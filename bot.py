import discord
from discord import channel
from discord.ext import commands
import json 


with open("setting.json",mode="r",encoding="utf8") as jfile:
    jdata =json,json.load(jfile)

intents = discord.Intents.all()


bot = commands.Bot(command_prefix=commands.when_mentioned_or('f!'),intents = intents)
#定義呼叫機器人的命令字首

@bot.event
async def on_ready():
    print(">>bot is online<<")
#顯示bot在線上

@bot.event
async def on_member_join(member):
    print("welcome")
    channel = bot.get_channel(int(jdata["Welcome_channel"]))
    await channel.send(f'{member} 歡迎你進來呱呱')
#歡迎訊息

@bot.event
async def on_member_remove(member):
    print("byebye")
    channel = bot.get_channel(int(jdata["Leave_channel"]))
    await channel.send(f'{member} 趕快走吧呱呱')
#再見訊息

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')
#對話時機器人的延遲



bot.run(jdata["TOKEN"])
