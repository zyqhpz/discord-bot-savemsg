import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

client = discord.Client()

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

serverID = 866348685990166588

bot = commands.Bot(command_prefix='/')

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send_message(f"""Welcome to the server {member.mention}""")

@client.event
async def on_ready():
    print('{0.user} is live!'.format(client))

@bot.command(pass_context = True)
async def savemsg(author):
    msg = client.get_channel(866348939270553600)
    await msg.send(' : %s saved this.' %author)
    # print ("{}".format(author))
    # print("Saved")
    # await channel.send("Saved!")

@client.event
async def on_message(message):
    id = client.get_guild(serverID)
    channels = ["commands"]
    valid_users = ["hzqhpz#5666"]

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi") 
        elif message.content == "!users":
            await message.channel.send(f"""# of Members: {id.member_count}""")
        elif message.content.find("/simpan") != -1:
            msg = client.get_channel(866348939270553600)
            by = '<@242852663392206851>'
            author = '<@{}>'.format(message.author.id)
            await message.channel.send("SAVED! by <@{}>".format(message.author))
            # await message.channel.send(' : %s is the best' % who)
            # await msg.send('Hi')
            await savemsg(author)

client.run(token)
