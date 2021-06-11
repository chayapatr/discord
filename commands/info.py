import discord
from discord.ext import commands
import os

with open("./commands/INFO.md", "r") as f:
  title = f.readline()
  content = "".join(f.read()).replace("PREFIX", os.getenv("PREFIX"))

@commands.command()
async def info(ctx, *args):
  """
  returns info about how to contribute to the bot
  """

  await ctx.message.delete()
  embed = discord.Embed(title=title, description=content, colour=discord.Colour.gold())
  await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(info)