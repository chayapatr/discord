def getprefix(command_name):
  return """from discord.ext import commands

@commands.command()
async def {}(ctx,*args):
  \"\"\"
  <a compiled function>
  \"\"\"

  _idx = 0
  def input(*argumentholder):
    nonlocal _idx
    _idx += 1
    return args[_idx - 1]
  async def print(*message):
    await ctx.send(''.join([str(x) for x in message]))""".format(command_name)

def getsuffix(command_name):
  return """
@{}.error
async def clear_error(ctx,error):
  print(error)

def setup(bot):
  bot.add_command({})
  """.format(command_name,command_name)