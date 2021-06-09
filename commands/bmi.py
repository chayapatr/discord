from discord.ext import commands

@commands.command()
async def bmi(ctx, *args):
  """
  computes the bmi given two properties (<width>, <height>)
  """
	
  if len(args) != 2:
    return await ctx.send("$bmi <weight> <height>")
    
  weight = float(args[0])
  height = float(args[1])

  if height > 2.72:
    height = height / 100

  BMI = weight / height ** 2

  result = ""

  if BMI < 18.5:
    result = "Underweight"
  elif BMI < 24.9:
    result = "Normal"
  elif BMI < 29.9:
    result = "Overweight"
  else:
    result = "Obese"
    
  await ctx.send("{bmi} ({res})".format(bmi=round(BMI, 2), res=result))


def setup(bot):
  bot.add_command(bmi)