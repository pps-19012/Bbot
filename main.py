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
    await msg.channel.send('commands - //hello, //svquote, //ramquote, //cryptocurrency, //bnp, //memes, //dankmemes, //redditannounce, //worldnews, //gaming, //music, //movies, //news, //gif, //books, //sports, //showerthoughts, //earth, //jokes')

  if(msg.content.startswith("//svquote")):
    txt = scraping.svquote()
    await msg.channel.send(txt)

  if(msg.content.startswith("//ramquote")):
    txt = scraping.ramquote()
    await msg.channel.send(txt)

  if(msg.content.startswith("//cryptocurrency")):
    txt = reddit.cryptocurrency()
    await msg.channel.send(txt)

  if(msg.content.startswith("//bnp")):
    txt = reddit.bnp()
    await msg.channel.send(txt)

  if(msg.content.startswith("//memes")):
    txt = reddit.memes()
    await msg.channel.send(txt)

  if(msg.content.startswith("//dankmemes")):
    txt = reddit.dankmemes()
    await msg.channel.send(txt)

  if(msg.content.startswith("//redditannounce")):
    txt = reddit.redditannounce()
    await msg.channel.send(txt)

  if(msg.content.startswith("//worldnews")):
    txt = reddit.worldnews()
    await msg.channel.send(txt)

  if(msg.content.startswith("//gaming")):
    txt = reddit.gaming()
    await msg.channel.send(txt)

  if(msg.content.startswith("//music")):
    txt = reddit.music()
    await msg.channel.send(txt)
    
  if(msg.content.startswith("//movies")):
    txt = reddit.movies()
    await msg.channel.send(txt)

  if(msg.content.startswith("//news")):
    txt = reddit.news()
    await msg.channel.send(txt)

  if(msg.content.startswith("//gif")):
    txt = reddit.gifs()
    await msg.channel.send(txt)

  if(msg.content.startswith("//books")):
    txt = reddit.books()
    await msg.channel.send(txt)

  if(msg.content.startswith("//sports")):
    txt = reddit.sports()
    await msg.channel.send(txt)

  if(msg.content.startswith("//showerthoughts")):
    txt = reddit.showerthoughts()
    await msg.channel.send(txt)

  if(msg.content.startswith("//earth")):
    txt = reddit.earth()
    await msg.channel.send(txt)

  if(msg.content.startswith("//jokes")):
    txt = reddit.jokes()
    await msg.channel.send(txt)
    
keep_alive()
client.run(os.environ['TOKEN'])
