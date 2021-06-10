import discord
from discord.ext import commands
 
@commands.command()
async def cat(ctx, *args):
	"""
	Sends a random cat image.
	The text will display whatever argument was passed through.
  Sends a random cat image.
	The text will display whatever argument was passed through.
  Sends a random cat image.
	The text will display whatever argument was passed through.
  Sends a random cat image.
	The text will display whatever argument was passed through.
	"""
	await ctx.message.delete()
	
	embed = discord.Embed()

	if len(args) > 0:
		embed.set_image(url="https://cataas.com/cat/cute/says/{text}".format(text=args[0]))
	else:
		embed.set_image(url="https://cataas.com/cat/cute")
	
	await ctx.send(embed=embed)
 
def setup(bot):
  bot.add_command(cat)