from discord.ext import commands

@commands.command()
async def multiply(ctx,*args):
  """
  <a compiled function>
  """

  _idx = 0
  def input(*argumentholder):
    nonlocal _idx
    _idx += 1
    return args[_idx - 1]
  async def print(*message):
    await ctx.send(''.join([str(x) for x in message]))
  a = input()
  b = input()
  await print(int(a)*int(b))
@multiply.error
async def clear_error(ctx,error):
  print(error)

def setup(bot):
  bot.add_command(multiply)
  