from helper import fetch
from discord.ext import commands

@commands.command(aliases=["crypt","crpyto"])
async def btc(ctx):
  """
  returns the bitcoin price as of now
  """

  await ctx.message.delete()

  coin = fetch(" https://api.coindesk.com/v1/bpi/currentprice.json")
	
  await ctx.send(coin["bpi"]["USD"]["rate"])

def setup(bot):
	bot.add_command(btc)