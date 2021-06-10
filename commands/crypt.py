import discord
import datetime
from helper import fetch
from discord.ext import commands

@commands.command(aliases=["crypt","crpyto"])
async def btc(ctx):
  """
  returns the bitcoin price as of now
  """

  await ctx.message.delete()

  coin = fetch(" https://api.coindesk.com/v1/bpi/currentprice.json")

  embed = discord.Embed(title="Bitcoin Price", description=coin["bpi"]["USD"]["rate"], colour = discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
	
  await ctx.send(embed=embed)

def setup(bot):
	bot.add_command(btc)