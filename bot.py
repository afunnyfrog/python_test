import discord
from discord import channel
from discord.ext import commands

intents = discord.Intents.all()


bot = commands.Bot(command_prefix=commands.when_mentioned_or('f!'),intents = intents)
#定義呼叫機器人的命令字首

@bot.event
async def on_ready():
    print(">>bot is online<<")

@bot.event
async def on_member_join(member):
    print("welcome")
    channel = bot.get_channel(898159587922935869)
    await channel.send(f'{member} 歡迎你進來呱呱')
    

@bot.event
async def on_member_remove(member):
    print("byebye")
    channel = bot.get_channel(898159634911752212)
    await channel.send(f'{member} 趕快走吧呱呱')

bot.run("ODc2NzI5MTc0NTMyOTU2MTYw.YRoTrA.Wg4eDQwarrPnkh4dj5A6WG5GgJg")
