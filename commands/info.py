from discord.ext import commands

content = "this is supposed to be info about how to use the bot"

@commands.command()
async def info(ctx, *args):
  """
  returns info about how to use the bot
  """

  await ctx.message.delete()
  await ctx.send(content)
  await ctx.send('feel free to contribute with \"$edit\"')

def setup(bot):
  bot.add_command(info)