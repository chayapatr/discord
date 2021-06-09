import discord
from discord.ext import commands
from os import getenv

prefix = getenv("PREFIX")
 
@commands.command()
async def help(ctx, *args):
  """Provides help information"""

  embed = discord.Embed(title="Help", description="type {0}help <command> to get information about a command".format(prefix), colour=discord.Colour.blurple())
  
  embed.add_field(name="something", value="also somethinggggggggggg")

  # helptext = "```"
  # 
  # for command in self.bot.commands:
  #   helptext+=f"{command}\n"
  # 
  # helptext+="```"
  # 
  # await ctx.send(helptext)

  await ctx.send(embed=embed)
 
def setup(bot):
  bot.add_command(help)