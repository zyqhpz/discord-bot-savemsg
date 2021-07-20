import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot, context

client = discord.Client()

# getMsg = discord.Message()

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
async def savemsg(author, msj, mesej):
    msg = client.get_channel(866348939270553600)
    # msj = await context.fetch_message(msj)
    # await msg.send('> {}'.format(msj.content))
    # await msg.send('>>> %s saved this: {}.'.format(msj.content) %author)
    await msg.send('%s simpan nota ini\n>>> %s' % (author, mesej))
    # print ("{}".format(author))
    # print("Saved")
    # await channel.send("Saved!")

# async def getmsg():
#     msg = await fetch_message()

@client.event
async def on_message(message):
    id = client.get_guild(serverID)
    channels = ["commands"]
    valid_users = ["hzqhpz#5666"]

    x = message.content.split(' ', 1)
    comm = x[0]
    mesej = x[1]
    # print(mesej)

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi") 
        elif message.content == "!users":
            await message.channel.send(f"""# of Members: {id.member_count}""")
        # elif message.content.find("/simpan") != -1:
        elif comm == '/simpan':
            by = '<@242852663392206851>'
            msgID = message.id
            author = '<@{}>'.format(message.author.id)
            msg_channel = message.channel
            msg = await msg_channel.fetch_message(866571390215127080)
            msg = await msg_channel.fetch_message(866682707375685655)
            print(msg)
            # await message.channel.send("SAVED! by <@{}>".format(message.author)) msg author
            # msg = await context.Context.fetch_message(self=_, id=int(866571390215127080))
            # await message.channel.send('>>> {}'.format(message.content.split(' ', 1)[1]))
            # await message.channel.send('>>> _{}_'.format(msg.content.split(' ', 1)[1])) msg get from msg.id
            # await message.channel.send(' : %s is the best' % who)
            # await msg.send('Hi')
            await savemsg(author, msg, mesej)

client.run(token)



@bot.command(pass_context=True, name="command")
async def _command(ctx):
    channel_id = "123"
    channel = bot.get_channel(channel_id)
    if not channel:
        await bot.say("Error: Could not resolve controller channel")
        return
    server_id = ctx.message.server.id
    async for message in bot.logs_from(channel, limit=500):
        if server_id in message.content:
            await bot.say("SSM")
            return
    await bot.say("SSM ELSE")