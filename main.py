import discord
import os

intent = discord.Intents.default()
intent.members = True
intent.message_content = True

client = discord.Client(intents=intent)
bot_secret = os.environ['BOT_TOKEN']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('Hi'):
        await message.channel.send('Hello!')
 
client.run(bot_secret)