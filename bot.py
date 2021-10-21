import discord
from discord import channel
from discord.ext import commands
import json 
import random
import os
 

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata =json.load(jfile)
    

intents = discord.Intents.all()


bot = commands.Bot(command_prefix=commands.when_mentioned_or('F!'),intents = intents)
#定義呼叫機器人的命令字首

@bot.event
async def on_ready():
    print(">>bot is online<<")
#顯示bot在線上

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata["Welcome_channel"]))
    await channel.send(f'{member} 歡迎你進來呱呱')
#歡迎訊息

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata["Leave_channel"]))
    await channel.send(f'{member} 趕快走吧呱呱')
#再見訊息

@bot.command()
async def load(ctx,extension):
    bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"loaded {extension}done.")

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"un-loaded {extension}done.")

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"re-loaded {extension}done.")

for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")


if __name__ == "__main__":
    bot.run(jdata["Token"])
