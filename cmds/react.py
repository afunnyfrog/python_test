import discord
from discord import channel
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
from PIL import Image

with open ('setting.json',mode="r",encoding='utf8') as jfile:
    jdata=json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def 圖片(slef,ctx):
        random_pic=random.choice(jdata["pic"])
        pic = discord.File(random_pic)
        await ctx.send(file=pic)

    @commands.command()
    async def 貓咪(slef,ctx):
        random_pic=random.choice(jdata["url_pic"])
        await ctx.send(random_pic)

    @commands.command()
    async def 猜顏色(slef,ctx):
        color = ("#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
        await ctx.send(1)
        hex = color.lstrip('#')
        await ctx.send(2)
        rgb= tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
        await ctx.send(3)
        image = Image.new("RGB",(500,500),rgb)
        await ctx.send(4)
        await ctx.send(image.show())
        await ctx.send(5)

def setup(bot):
    bot.add_cog(React(bot))