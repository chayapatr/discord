import discord
import datetime
from helper import fetch
from discord.ext import commands

@commands.command(aliases=["crypt", "crypto"])
async def btc(ctx):
  """
  returns the crypto prices as of now
  """

  await ctx.message.delete()

  # coin = fetch(" https://api.coindesk.com/v1/bpi/currentprice.json")

  # embed = discord.Embed(title="Bitcoin Price", description=coin["bpi"]["USD"]["rate"], colour = discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())

  coins = fetch("https://static.coinpaper.io/api/coins.json")
  
  embed = discord.Embed(title="Cryto Prices", colour=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())

  embed.set_image(url="https://specials-images.forbesimg.com/imageserve/5ea6d49e165a170006a5d625/960x0.jpg?fit=scale")

  for coin in coins[:6]:
    embed.add_field(name="{0} ({1})".format(coin["name"], coin["symbol"]), value=coin["price"])
	
  await ctx.send(embed=embed)

def setup(bot):
	bot.add_command(btc)