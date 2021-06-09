import discord
from discord.ext import commands
import os

challenge_path = "grader/challenge"

challenge_list = os.listdir(challenge_path)

@commands.command(aliases=['challenges', 'listchallenges', 'ch'])
async def challenge(ctx, *args):
  """
  lists all challenges in the database
  """

  await ctx.message.delete()
  
  if len(args) != 0:
    try:
      with open("{0}/{1}/README.md".format(challenge_path, args[0]), 'r') as f:
        title = f.readline()
        res = f.read()
        embed = discord.Embed(title=title, description=res, colour=discord.Colour.gold())

        await ctx.send(embed=embed)
    except EnvironmentError:
      await ctx.send("Can't find the challenge you requested")
  
  else:
    await ctx.send(", ".join(challenge_list))

def setup(bot):
  bot.add_command(challenge)