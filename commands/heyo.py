from discord.ext import commands

@commands.command(aliases=["hello"])
async def heyo(ctx):
	"""heyo !!"""
  
	await ctx.reply("Heyo, {name}!".format(name=ctx.author.display_name))

def setup(bot):
	bot.add_command(heyo)