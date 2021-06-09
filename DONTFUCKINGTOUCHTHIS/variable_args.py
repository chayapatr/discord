from discord.ext import commands

@commands.command()
async def variable_args(ctx,*args):
  _idx = 0
  def input(*argumentholder):
    nonlocal _idx
    _idx += 1
    return args[_idx - 1]
  async def print(*message):
    await ctx.send(''.join([str(x) for x in message]))
  n = int(input())
  
  sum = 0
  for i in range(n):
    x = int(input())
    sum += x
  
  await print(sum)
@variable_args.error
async def clear_error(ctx,error):
  await ctx.send('error')
  await ctx.send(error)

def setup(bot):
  bot.add_command(variable_args)
  