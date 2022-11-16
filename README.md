# Discord Bot using Python

*Run on Replit:* https://replit.com/@PawaraSiriward1/DiscordMessageBot#main.py

*Preview:*
![image](https://user-images.githubusercontent.com/56413657/202190250-18874b10-aae5-4177-b8d3-e06a3057a428.png)

# Steps to follow

## Step 01: Create discord server
- Sign up or log in to your discord account: https://discord.com/
- Create a server where you need to integrate the bot

## Step 02: Create discord app
- Go to https://discord.com/developers/applications
- Create a New Application
- Go to OAuth2 section
- Under 'URL Generator', under 'SCOPES' select 'bot', under 'BOT PERMISSIONS' select all under 'TEXT PERMISSIONS' except 'Send TTS Messages', and select 'Read Messages/View Channels' under 'GENERAL PERMISSIONS'
- Copy the generated URL and goto the link.
- Select the server and the bot and authorize (can close the particular tab afterwards)
- You will see the newly created bot is added to the discord server you created (but it will appear offline until you run the code and initilaize the bot).

## Step 03: Generate the token
- Go back to discord bot application you created 
- Under bot section make 'SERVER MEMBERS INTENT' and 'MESSAGE CONTENT INTENT' on.
- Generate token and copy the token

## Step 04: Run the code
- Open the code in replit IDE: https://replit.com/@PawaraSiriward1/DiscordMessageBot#main.py
- Create a scret (key: BOT_TOKEM, and value: the_token_copied_earlier)
- Run the code
