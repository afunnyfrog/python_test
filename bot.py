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


for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
         bot.load_extension(f"cmds.{filename[:-3]}")

@bot.command()
async def load(ctx,extension):
    bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"loaded {extension} done.")

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"un-loaded {extension} done.")

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"re-loaded {extension} done.")

if __name__ == "__main__":
    bot.run(jdata["Token"])