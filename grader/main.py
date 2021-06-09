import os
import discord
from discord.ext import commands
from .format_result import format_result
from .run_test import run_test
from .format_argument import format_argument

# save file
# async def test(ctx, *args):
async def test(message):
  if not message.content.startswith('$test'):
    return
  print(message.content)
  question, code = format_argument(message.content)
  code_path = os.getcwd() + '/grader/code.py'
  with open(code_path, "w") as f:
    f.write(code)
  await message.delete()
  print("-------------------")
  result = run_test(question)
  correct, result = format_result(result)
  status = "Pass!" if correct else "Fail :("

  colour = discord.Colour.green() if correct else discord.Colour.red()
	
  embed = discord.Embed(title="Quiz: {0} -> {1}".format(question, status), colour = colour, description=result)

  embed.set_footer(text="by @{user}".format(user=message.author.display_name))

  # if result:
  #   await ctx.send(result)
  # else:
  #   await ctx.send("expected: "+expected+"\nreturn: "+output
  print(result)
  # await ctx.send(result)
  await message.channel.send(embed=embed)
  # await ctx.author.send(embed=embed)

def setup(bot):
  bot.add_listener(test,'on_message')