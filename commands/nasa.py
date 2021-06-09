from helper import fetch
import discord
from discord.ext import commands
import datetime

@commands.command(aliases=["nasa", "space"])
async def pic(ctx):
  """
  outputs an image
  """

  await ctx.message.delete()
  nasa = fetch("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
	
	embed = discord.Embed(title=nasa["title"], description=nasa["copyright"], timestamp=datetime.datetime.utcnow(), color=discord.Color.blurple())
  
	embed.set_image(url=nasa["hdurl"])
	
	await ctx.send(embed=embed)

def setup(bot):
	bot.add_command(pic)