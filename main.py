import discord
import os
from discord.ext import commands
# from replit import db
# import stuffs.main as stuffs

from helper import printList
from command_loader import load
import react
from keep_alive import keep_alive

os.system('clear')

# bot client
PREFIX = os.getenv('PREFIX')
intents = discord.Intents.all()
client = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None, case_insensitive=True)

# add command to client
error_module = load(client)

# debug set up
printList('Loaded command: ', client.walk_commands())
printList('Error Module: ', error_module)

# help command  

@commands.command()
async def help(ctx, *args):
  """Provides help information"""

  # await ctx.message.delete()
  # search for a command
  if len(args) != 0:
    commands_list = []

    for command in client.commands:
      commands_list.append({
        "name": command.name,
        "description": command.help,
        "aliases": command.aliases
      })

    command = next((command for command in commands_list if   command["name"] == args[0].lower() or args[0].lower() in set(command["aliases"])), None)

    if command:

      embed = discord.Embed(title="{0}{1}".format(PREFIX, command["name"]), description=command["description"], colour=discord.Colour.blurple())

      embed.add_field(name="Aliases", value=", ".join(command["aliases"]) if len(command["aliases"]) != 0 else "-")

      embed.set_footer(text="type `{0}help` to get the list of all commands".format(PREFIX))

      return await ctx.send(embed=embed)
    else:
      return await ctx.send("help: command not found, type `{0}help` to get the list of all commands".format(PREFIX))

  # just print out everything
  else:
    embed = discord.Embed(title="Help", description="type {0}help <command> to get information about a command".format(PREFIX), colour=discord.Colour.blurple())

    command_names = map(lambda name: "`{0}`".format(name),[command.name for command in client.commands])
    embed.add_field(name="Commands", value=", ".join(command_names))

    await ctx.send(embed=embed)

client.add_command(help)

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
    await args[0].send("something went wrong.")
    await args[0].send("`{0}`".format(args[1]))
	
  raise

@client.event
async def on_command_error(ctx, exc):
  if isinstance(exc, commands.CommandNotFound):
    await ctx.reply("command not found :(")
  
  elif hasattr(exc, 'original'):
    raise exc.original
    
  else:
    raise exc.original

keep_alive()
client.run(os.getenv('TOKEN'))