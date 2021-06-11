from discord.ext import commands
 
@commands.command()
async def bongo(ctx, *args):
  await ctx.message.delete()
  await ctx.send("https://pyxis.nymag.com/v1/imgs/d57/0bb/cacd6910aad2dcff81f39e5823a8737c7b-24-bongo-cat.rsocial.w1200.jpg")
 
def setup(bot):
  bot.add_command(bongo)