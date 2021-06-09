from discord.ext import commands

@commands.command()
async def one_string_args(ctx,*args):
  _idx = 0
  def input(*argumentholder):
    nonlocal _idx
    _idx += 1
    return args[_idx - 1]
  async def print(*message):
    await ctx.send(''.join([str(x) for x in message]))
  a = [int(e) for e in input().split()]
  
  product = 1
  for x in a:
    product *= x
  
  await print(product)
@one_string_args.error
async def clear_error(ctx,error):
  await ctx.send('error')
  await ctx.send(error)

def setup(bot):
  bot.add_command(one_string_args)
  