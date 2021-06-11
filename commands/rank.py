from discord.ext import commands
import discord
import os
# from replit import db

import grader.achievement as ach

@commands.command(aliases=['score', 'leaderboard', 'sc'])
async def rank(ctx, *args):
  """
  lists all challenges in the database
  """
  if len(args) != 0:
    if args[0].lower() == "me":
      score = ach.get_achievement(str(ctx.author.id))
      if score:
        ranks = ach.get_ranking()
        user_rank = ranks.index(str(ctx.author.id))+1

        if user_rank <= 3:
          user_rank = "**#{0}**".format(user_rank)

        completed_challenges = ", ".join(score[1])

        embed = discord.Embed(title="{0}".format(ctx.author.display_name), description="Rank: {0}\nScore: {1}\nCompleted Challenges: {2}".format(user_rank, score[0], completed_challenges), colour=discord.Colour.orange())

        return await ctx.send(embed=embed)
      else:
        fail_embed = discord.Embed(title="Rank", description="Can't find your score. Maybe you have't completed any challenges, yet?", colour=discord.Colour.red())

        return await ctx.send(embed=fail_embed)

  ranks = ach.get_ranking()
  name = ""
  score = ""
  rank = 1

  for u in ranks[:20]:
    point = ach.get_achievement(str(u))[0]
    
    name += "{0}: <@{1}>\n".format(rank, u)
    score += "{2} {3}\n".format(rank, u, point, "Points" if point > 1 else "Point")
    rank += 1

  # await ctx.message.delete()
  
  if len(ranks) != 0:
    embed = discord.Embed(title="Ranking", description="type `{}rank me` to see your stats".format(os.getenv("PREFIX")), colour=discord.Colour.teal())

    embed.add_field(name="Name", value=name)
    embed.add_field(name="Score", value=score)

  else:
    embed = discord.Embed(title="Ranking", description="There's no one here yet. 😉", colour=discord.Colour.teal())
  
  await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(rank)