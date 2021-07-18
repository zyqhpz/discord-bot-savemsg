import discord

client = discord.Client()

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

serverID = 866348685990166588

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send_message(f"""Welcome to the server {member.mention}""")

@client.event
async def on_ready():
    print('{0.user} is live!'.format(client))

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
            await message.channel.send("SAVED!")

client.run(token)
