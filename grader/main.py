import os
from discord.ext import commands
import discord

from .format import format_argument, format_code, format_result
from .run_test import run_test
from .achievement import set_achievement

PREFIX = os.getenv("PREFIX")

@commands.command(aliases=["run", "grade"])
async def test(ctx):

  message = ctx.message
  question, code = format_argument(message.content)
  code = format_code(code)
  question = question.lower()

  embed = discord.Embed(title="Challenge: {0}".format(question), colour = discord.Colour.gold(), description="Processing...")

  embed.set_footer(text="@{user}".format(user=message.author.display_name))

  await ctx.message.delete()
  process = await ctx.author.send(embed=embed)

  # save file
  code_path = os.getcwd() + '/grader/code.py'
  with open(code_path, "w") as f:
    f.write(code)
  
  result, inputfolder_path = run_test(question)
  if not result:
    fail_embed = discord.Embed(title="Unknown Challenge: {0}".format(question), description="unable to find the challenge you're looking for.", colour=discord.Colour.red())
    return await ctx.author.send(embed=fail_embed)

  correct, result = format_result(result, inputfolder_path)
  status = "Pass!" if correct else "Fail :("

  colour = discord.Colour.green() if correct else discord.Colour.red()

  # print(result)

  await process.delete()
  
  if len(result) <= 6000:
    embed = discord.Embed(title="Challenge: {0} -> {1}".format(question, status), colour = colour, description=result)

    embed.set_footer(text="@{user}".format(user=message.author.display_name))
  else:
    embed = discord.Embed(title="Challenge: {0} -> {1}".format(question, status), colour = colour, description="bruh")

    embed.set_footer(text="@{user}".format(user=message.author.display_name))

  await ctx.author.send(embed=embed)

  if correct:
    res = set_achievement(str(message.author.id), question)

    if res != -1:
      embed_score = discord.Embed(title="Score", description= "You Earn: {0} {1}\nTotal Score: {2} {3}".format(res[1], "Points" if res[1]>1 else "Point", res[0][0], "Points" if res[1]>1 else "Point"), colour=discord.Colour.teal())

      embed_score.set_footer(text="@{0}".format(message.author.display_name))

      await ctx.author.send(embed=embed_score)
  
def setup(bot):
  # worker2 = threading.Thread(target=asyncio.run_coroutine_threadsafe, args=(run(q),bot.loop))
  # worker2.start()
  bot.add_command(test)