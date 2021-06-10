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

  # await ctx.message.delete()
  
  if len(args) != 0:
    try:
      with open("{0}/{1}/README.md".format(challenge_path, args[0].lower()), 'r') as f:
        title = f.readline()
        res = f.read()
        embed = discord.Embed(title=title, description=res, colour=discord.Colour.gold())
        await ctx.send(embed=embed)
    except EnvironmentError:
      embed = discord.Embed(title=args[0], description="Can't find the challenge you requested", colour=discord.Colour.red())
      await ctx.send(embed=embed)
  
  else:
    if 'README_template.md' in challenge_list:
      challenge_list.remove('README_template.md')
    res = ""
    for challenge in challenge_list:
      with open("{0}/{1}/README.md".format(challenge_path, challenge), 'r') as f:
        title = f.readline()
        description = f.read().split("`Input`")
      res += "`{0}`{1}".format(title, description[0])
    embed = discord.Embed(title="Challenge List", description=res, colour=discord.Colour.gold())
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(challenge)