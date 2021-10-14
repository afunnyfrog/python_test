import discord

def read_token():
    with open("token.exe","r") as f :
        line = f.readline()
        return line[0].strip()

token= read_token

client = discord.Client()
client.run(token)