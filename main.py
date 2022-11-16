import discord
import os
import requests
import json
import random
from replit import db

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

if "responding" not in db.keys():
  db["responding"] = True

# helper fn to retrive and return quotes form the api
def get_quote(feature):
  
  url = 'https://api.api-ninjas.com/v1/quotes?category=happiness'
  headers = {'X-Api-Key': api_key}
  params = {'category': feature}
  
  response = requests.get(url, headers=headers, params=params)
  json_data = json.loads(response.text)
  quote = json_data[0]['quote']
  
  return quote

# helper fn to add responses messages to database
def update_responses(response_message):
  if "msgresponses" in db.keys():
    msgresponses = db["msgresponses"]
    msgresponses.append(response_message)
    db["msgresponses"] = msgresponses
  else:
    db["msgresponses"] = [response_message]

# helper fn to delete responses messages to database
def delete_responses(index):
  msgresponses = db["msgresponses"]
  if len(msgresponses) > int(index):
    del msgresponses[int(index)]
  db["msgresponses"] = msgresponses
    
# to ready the bot
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

# to provide responses from the bot
@client.event
async def on_message(message):
  msg = message.content
  if message.author == client.user:
    return

  # greeting to the user
  if msg.startswith('Hi'):
    await message.channel.send('Hello!')

  # Display inspirational quotes to the user from the API
  if msg.startswith('$inspire'):
    quote = get_quote('happiness')
    await message.channel.send(quote)

  # responding to sad triggers from the user
  if db["responding"]:
    options = starter_responses
    if "msgresponses" in db.keys():
      options = options + list(db["msgresponses"])
    
    if any(word in msg for word in unhappy_triggers):
      await message.channel.send(random.choice(options))

  # to add the responses from the database
  if msg.startswith("$new"):
    msgresponses = msg.split('$new ', 1)[1]
    update_responses(msgresponses)
    await message.channel.send("New response message added to database")

  # to delete the responses from the database
  if msg.startswith("$del"):
    msgresponses = []
    if "msgresponses" in db.keys():
      index = msg.split("$del", 1)[1]
      delete_responses(index)
      msgresponses = db["msgresponses"]
    await message.channel.send(msgresponses)

  # to list down the response messages entered by user
  if msg.startswith("$list"):
    msgresponses = []
    if "msgresponses" in db.keys():
      msgresponses = db["msgresponses"]
    await message.channel.send(msgresponses)
    
  # to control on/off of the chatbot responding
  if msg.startswith("$chatbot"):
    value = msg.split("$chatbot ", 1)[1]
    if value.lower() == "on":
      db["responding"] = True
      await message.channel.send("Chatbot responding is on")
    else:
      db["responding"] = False
      await message.channel.send("Chatbot responding is off")
    
# to run the bot
client.run(bot_secret)