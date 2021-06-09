from discord.ext import commands
import os

challenge_list = os.listdir("grader/testcase")

@commands.command(aliases=['challenges', 'ch'])
async def listchallenges(ctx, *args):
  """
  lists all challenges in the database
  """

  await ctx.send(", ".join(challenge_list))  

def setup(bot):
  bot.add_command(listchallenges)