from discord.ext import commands
 
@commands.command(aliases=["join", "code"])
async def edit(ctx, *args):
  """
  please feel free to contribute to our project!
  """

  await ctx.send('Bot\'s code: https://replit.com/join/otetiocn-chayapatra')
 
def setup(bot):
  bot.add_command(edit)
