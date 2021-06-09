# hackerman101

## How to use
1. เพิ่มไฟล์ในโฟลเดอร์ commands (อย่าลืมใส่ .py ด้วย)
2. copy โค้ด template แล้วแทนคำว่า `command_name` ด้วยชื่อ command ที่อยากตั้ง
3. เขียนโปรแกรมทุกอย่างไว้ในฟังก์ชั่น (อยู่ใน `def`)

## Template code
ถ้าอยากรู้ว่าโค้ดนี้ทำงานยังไงถามมาได้ที่ discord นะ 😉

```python
from discord.ext import commands

@commands.command()
async def command_name(ctx, *args):
  # ทำทุกอย่างในนี้

def setup(bot):
  bot.add_command(command_name)
```

## Input
เราสามารถรับ arguments ได้ (ถ้ารัน command `$cat meow mew` arguments จะประกอบด้วย `["meow", "mew"]`)

โดย arguments ทั้งหมดจะอยู่ในตัวแปร `args` และเราสามารถนำไปใช้ได้แบบนี้

```python
@commands.command()
async def test_args(ctx, *args):
  # args = ["meow", "mew"]
	for i in len(args):
		print(args[i])

def setup(bot):
  bot.add_command(test_args)
```

[อ่านต่อเรื่องการเขียน arguments](https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html)

*Note: ในนั้นใช้ @bot.command() แทน @commands.command() ซึ่งทำตัวคล้าย ๆ กัน เลย*

## Output
ctx (context) คือสิ่งที่เราสามารถใช้เพื่อ **รับ, ส่ง** ข้อมูลแบบเบสิก และอื่น ๆ ได้

### ctx features
* รับ message => ```ctx.message.content```
* ส่ง message => ```await ctx.send("message")```
* ตอบกลับคนส่ง => ```await ctx.reply("message")```
* อ่านชื่อคนส่ง message => ```ctx.author.display_name```

## Example

ตัวอย่าง command การคำนวณ bmi

วิธีใช้: พิมพ์ $bmi ตามด้วย น้ำหนัก และ ส่วนสูง

เช่น: `$bmi 50 1.76`

```python
@commands.command()
async def bmi(ctx, *args):
	
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
    
  await ctx.send(str(BMI) + " (" + result + ")")

def setup(bot):
  bot.add_command(bmi)
```

## Extra

เราสามารถ customise command ของเราได้โดยการเพิ่ม alias (ชื่ออีกชื่อของ command เรา)

```python
@commands.command(aliases=['alias1', 'alias2'])
```
เช่น
```python
@commands.command(aliases=['test', 'arguments', 'args'])
async def test_args(ctx, *args):
  await ctx.send('args_list: ' + ", ".join(args))
```

เมื่อเสร็จแล้ว เราสามารถใช้ alias เรียก command ตามชื่อหลักของ command ได้

Ex: `$test_args`, `$test`, `$arguments`, และ `$args` ใช้เรียก command เดียวกัน 

## More info

documentation: https://discordpy.readthedocs.io/en/stable/

ข้อมูลเกี่ยวกับ @commands.command() (เหตุผลว่าทำไมโค้ด template เราถึงเป็นแบบนั้น):

https://discordpy.readthedocs.io/en/stable/ext/commands/extensions.html