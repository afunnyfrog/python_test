import discord
From discord.ext import commands


bot = commands.Bot(commands_prefix="f!")
#定義呼叫機器人的命令字首

@bot.event
async def on_ready():
    print(">>bot is online<<")



bot.run("ODc2NzI5MTc0NTMyOTU2MTYw.YRoTrA.s2yUDQcuPnyNX73PsgulLQ4jTNY")
