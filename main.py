import discord
import os

from function.crypt import btc
import function.nasa as nasa

from replit import db
import stuffs.main as stuffs

from keep_alive import keep_alive

# set up commands
commands = []
for (dirpath, dirnames, filenames) in os.walk(os.getcwd() + '/function'):
    for f in filenames:
      if f.endswith(".py"):
        commands.append(f[:-3])
    break

# bot client
prefix = "$"
client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  # print(message.author + ': ' + message.content)
  if message.author == client.user:
    return

  if message.content.startswith(prefix):
    msg_parts = message.content[len(prefix):].split()
    command = msg_parts[0]
    arguments = msg_parts[1:]

    # Cool! owwo
    # sfdjlk;

    if command.startswith('hello'):
      await message.channel.send('Hello!')
      return

    if command.startswith('args'):
      await message.channel.send(str(arguments))
      return

    if command.startswith('db'):
      typ, res = stuffs.handle_db(arguments)
      if typ == 0:
        await message.channel.send(str(res))
      elif typ == 1:
        embed = discord.Embed(title="Warning",description=res, color=discord.Color.red())
        await message.channel.send(embed=embed)
      elif typ == 2:
        embed = discord.Embed(title="Info",description=res, color=discord.Color.green())
        await message.channel.send(embed=embed)
      return

    if command.startswith('btc'):
      embed = discord.Embed(title="Bitcoin Price",description=btc() +" USD", color=discord.Color.blurple())
      await message.channel.send(embed=embed)
      return

    if command.startswith('pic'):
      pic = nasa.pic()
      await message.channel.send(pic[0])
      await message.channel.send(pic[1]+" by "+pic[2])
      return
  
  else: return
    
keep_alive()
client.run(os.getenv('TOKEN'))