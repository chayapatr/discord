import os
import discord
from discord.ext import commands
from .format_result import format_result
from .run_test import run_test
from .format_argument import format_argument

PREFIX = os.getenv("PREFIX")

@commands.command(aliases=["run"])
async def test(ctx):
  """
  Compares user given code to the solution to check if the results match each other.
  """

  message = ctx.message
  question, code = format_argument(message.content)
  code = format_code(code)
  question = question.lower()
  code_path = os.getcwd() + '/grader/code.py'
  # save file
  with open(code_path, "w") as f:
    f.write(code)
  await message.delete()
  result, inputfolder_path = run_test(question)
  correct, result = format_result(result, inputfolder_path)
  status = "Pass!" if correct else "Fail :("

  colour = discord.Colour.green() if correct else discord.Colour.red()
	
  embed = discord.Embed(title="Challenge: {0} -> {1}".format(question, status), colour = colour, description=result.replace("*","\*"))

  embed.set_footer(text="@{user}".format(user=message.author.display_name))

  # server message
  await message.channel.send(embed=embed)

  # private message
  # await ctx.author.send(embed=embed)

# hello for what
def format_code(code):
  prefix = """import multiprocessing
import sys

def runner():
  sys.stdin = open(0)
"""
  suffix = """timeout = 1

if __name__ == '__main__':
  p = multiprocessing.Process(target=runner, name="runner")
  p.start()

  p.join(timeout)

  if p.is_alive():
    print("Terminate  - Exceed Limit Time")
    p.terminate()
    p.join()
"""
  return prefix+"  "+code.replace("\n","\n  ")+"\n\n"+suffix

def setup(bot):
  bot.add_command(test)
