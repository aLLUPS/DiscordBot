import discord
import os
import requests
import json
import random

intent = discord.Intents.default()
intent.members = True
intent.message_content = True
client = discord.Client(intents=intent)

bot_secret = os.environ['BOT_TOKEN']
api_key = os.environ['API_KEY']

unhappy_triggers = ["sad", 
                    "depressed", 
                    "unhappy", 
                    "angry", 
                    "depressing"]

starter_responses = ["Cheer up!",
                    "Don't worry!",
                    "You are great!"]

# to return quote from api
url = 'https://api.api-ninjas.com/v1/quotes?category=happiness'
headers = {'X-Api-Key': api_key}

def get_quote():
  response = requests.get(url, headers=headers)
  json_data = json.loads(response.text)
  quote = json_data[0]['quote']
  return quote

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
  msg = message.content
  if message.author == client.user:
    return
  if msg.startswith('Hi'):
    await message.channel.send('Hello!')
  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  if any(word in msg for word in unhappy_triggers):
    await message.channel.send(random.choice(starter_responses))


client.run(bot_secret)