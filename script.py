# Telethon utility # pip install telethon
from telethon import TelegramClient, events
from telethon.tl.custom import Button

import configparser # Library for reading from a configuration file, # pip install configparser
import datetime # Library that we will need to get the day and time, # pip install datetime


#### Access credentials
config = configparser.ConfigParser() # Define the method to read the configuration file
config.read('config.ini') # read config.ini file

api_id = config.get('default','api_id') # get the api id
api_hash = config.get('default','api_hash') # get the api hash
BOT_TOKEN = config.get('default','BOT_TOKEN') # get the bot token

# Create the client and the session called session_master. We start the session as the Bot (using bot_token)
client = TelegramClient('sessions/session_master', api_id, api_hash).start(bot_token=BOT_TOKEN)

# Define the /start command
@client.on(events.NewMessage(pattern='/(?i)start')) 
async def start(event):
    sender = await event.get_sender()
    SENDER = sender.id
    text = "Docker Bot 🤖 ready\nHello! I'm answering you from Docker Ora parlo italiano!"
    await client.send_message(SENDER, text, parse_mode="HTML")



### First command, get the time and day
@client.on(events.NewMessage(pattern='/(?i)time')) 
async def time(event):
    # Get the sender of the message
    sender = await event.get_sender()
    SENDER = sender.id
    text = "Received! Day and time: " + str(datetime.datetime.now())
    await client.send_message(SENDER, text, parse_mode="HTML")


# Define the /testiamo command samir zarouali
@client.on(events.NewMessage(pattern='/(?i)samir')) 
async def samir(event):
    sender = await event.get_sender()
    SENDER = sender.id
    text = "Ciao \nSamir Zaro! Dai le scarpe di calcetto ad achraf!"
    await client.send_message(SENDER, text, parse_mode="HTML")


# Andrew Tate Commento Matrix
@client.on(events.NewMessage(pattern='/(?i)topg')) 
async def samir(event):
    sender = await event.get_sender()
    SENDER = sender.id
    text = "Matrix lo ha attaccato \n Guarda questo video: https://youtube.com/shorts/8rxiK3cpu-0?feature=share"
    await client.send_message(SENDER, text, parse_mode="HTML")







### MAIN
if __name__ == '__main__':
    print("Bot Started!")
    client.run_until_disconnected()
