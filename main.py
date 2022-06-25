import discord
import os
#import requests
#import json
import scraping
import reddit
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  # for server in client.servers:
  #     for channel in server.channels:
  #         if channel.type == 'Text':
  #             await channel.send("Yo! This is Bbot. Type '//help' to know more about me")

@client.event
async def on_message(msg):
  if(msg.author == client.user):
    return
    
  if(msg.content.startswith("//hello")):
    # print('received')
    await msg.channel.send('Yo! This is Bbot.')

  if(msg.content.startswith("//help")):
    # print('received')
    await msg.channel.send('commands - //hello, //svquote, //ramquote, //cryptocurrency')

  if(msg.content.startswith("//svquote")):
    txt = scraping.svquote()
    await msg.channel.send(txt)

  if(msg.content.startswith("//ramquote")):
    txt = scraping.ramquote()
    await msg.channel.send(txt)

  if(msg.content.startswith("//cryptocurrency")):
    txt = reddit.cryptocurrency()
    await msg.channel.send(txt)

keep_alive()
client.run(os.environ['TOKEN'])
