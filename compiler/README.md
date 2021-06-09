# goal
To change native python file into discord command

### original code
```python
paid = float(input()) # input 1
price = float(input()) # input 2

exchange = paid - price

res = ""

res += "100->{exchange}\n".format(exchange = exchange//100)
exchange = exchange % 100
res += "20->{exchange}\n".format(exchange = exchange//20)
exchange = exchange % 20
res += "5->{exchange}\n".format(exchange = exchange//5)
exchange = exchange % 5
res += "1->{exchange}\n".format(exchange = exchange//1)
print(res)
```
### compiled code
```python
from discord.ext import commands

@commands.command()
async def atm(ctx, *args):
  paid = float(args[0]) # input 1
  price = float(args[1]) # input 2

  exchange = paid - price

  res = ""

  res += "100->{exchange}\n".format(exchange = exchange//100)
  exchange = exchange % 100
  res += "20->{exchange}\n".format(exchange = exchange//20)
  exchange = exchange % 20
  res += "5->{exchange}\n".format(exchange = exchange//5)
  exchange = exchange % 5
  res += "1->{exchange}\n".format(exchange = exchange//1)
  await ctx.send(print(res))

def setup(bot):
  bot.add_command(atm)
```

## todo
- fix ton of bugs that may happen
- argument checker