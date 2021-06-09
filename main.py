import discord
import os
from discord.ext import commands
# from replit import db
# import stuffs.main as stuffs

from helper import printList
from command_loader import load
import react
from keep_alive import keep_alive

# bot client
prefix = os.getenv('PREFIX')
intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix,intents=intents)

# add command to client
error_module = load(client)

# debug set up
printList('Loaded command: ', client.walk_commands())
printList('Error Module: ', error_module)

# add event
@client.event
async def on_ready():
  try:
    # reaction role
    await react.setup(client)
  except:
    print('error on reaction message')
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_error(err, *args):
	if err == "on_command_error":
		await args[0].send("something went wrong, check the command line")

	raise

@client.event
async def on_command_error(ctx, exc):
	if isinstance(exc, commands.CommandNotFound):
		pass
	
	elif hasattr(exc, 'original'):
		raise exc.original

	else:
		raise exc.original

# OLD METHOD
# =================
# @client.event
# async def on_message(message):
# 	command = message[1:]
# 	arguments = message.split(' ')[1:]
# 
# 	if message.author == client.user:
# 		return
# 
# 	if message.content.startswith('$'):
# 		if command == 'hello':
# 			await message.channel.send('Hello!')
# =================

keep_alive()
client.run(os.getenv('TOKEN'))