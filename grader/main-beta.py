import os
from discord.ext import commands
import asyncio
import discord
import threading

import queue

from .worker import worker as run

PREFIX = os.getenv("PREFIX")
q = queue.Queue()

@commands.command(aliases=["run", "grade"])
async def test(ctx):
  """
  Compares user given code to the solution to check if the results match each other.
  """
  
  global q

  for thread in threading.enumerate(): 
    print(thread.name)

  # if worker1.is_alive():
  #   print("still alive")
  #   pass
  # else:
    # worker1 = threading.Thread(target=asyncio.run_coroutine_threadsafe, args=(run(q), bot.loop))
    # worker1.start()
    print("is ded")

  q.put(ctx)
  
def setup(bot):
  worker1 = threading.Thread(target=asyncio.run_coroutine_threadsafe, args=(run(q), bot.loop))
  worker1.start()
  # worker2 = threading.Thread(target=asyncio.run_coroutine_threadsafe, args=(run(q),bot.loop))
  # worker2.start()
  bot.add_command(test)