# https://www.freecodecamp.org/news/create-a-discord-bot-with-python/

import discord
import os

from os import listdir
from os.path import isfile, join

dirpath = "/function"
commands = [f for f in listdir(dirpath) if isfile(join(dirpath, f))]

print(commands)

from function.crypt import crypt
import nasa

from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  # print(message.author + ': ' + message.content)
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')
    return

  if message.content.startswith('$crypt'):
    embed = discord.Embed(title="Crypt",description=crypt(), color=discord.Color.blurple())
    await message.channel.send(embed=embed)
    return

  if message.content.startswith('$pic'):
    let pic = nasa.pic()
    await message.channel.send()
    
keep_alive()
client.run(os.getenv('TOKEN'))