from discord.ext import commands

@commands.command(aliases=["suffer"])
async def bug(ctx):
  """
  bug i kwai
  """

  await ctx.message.delete()

  await ctx.send("https://f.ptcdn.info/114/052/000/os8vamgl4TQdXXSm2iI-o.jpg")

def setup(bot):
  bot.add_command(bug)