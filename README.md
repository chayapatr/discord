# hackerman 101

## Grader (โปรแกรมตรวจการบ้าน)

เราสามารถใช้บอท hackerman เพื่อตรวจโค้ดการบ้านของเราได้ โดยบอทจะทำการเช็ค output ของโค้ดเรากับ output ที่ควรจะได้

command: `$test <challenge_name> <your_code>`

ตัวอย่าง:

```
$test one a = int(input())
b = int(input())
print(a+b)
```

*Note: ระวัง space ที่เว้นด้วย เพราะ python จะ error ถ้า spacing ไม่ดี*

## How to add commands (เพิ่มคำสั่ง)

เราสามารถเพิ่ม commands ได้สองวิธี

### 1. ใช้ compiler ของเรา

เราได้ set ไว้ว่าเราจะสามารถแปลงโค้ดใน `user_src` ทั้งหมดให้กลายเป็นโค้ดที่สามารถนำไปใช้คุมบอทได้ (ซึ่งอยู่ใน destination folder)

ง่าย ๆ เลยคือเราแปลโค้ดทั้งหมดในโฟลเดอร์ `user_src` ให้กลายเป็นโค้ดที่ใช้คุมบอทได้ แต่จะมีข้อจำกัดคือเราจะสามารถทำได้แค่คำสั่งเบสิก ๆ เท่านั้น

ใน `user_src/`:

```python
a = input()
b = input()
print(int(a)+int(b))
```

ใน `DONTFUCKINGTOUCHTHIS/` จะกลายเป็น:

```python
from discord.ext import commands

@commands.command()
async def add(ctx,*args):
  _idx = 0
  def input(*argumentholder):
    nonlocal _idx
    _idx += 1
    return args[_idx - 1]
  async def print(*message):
    await ctx.send(''.join([str(x) for x in message]))
  a = input()
  b = input()
  await print(int(a)+int(b))
@add.error
async def clear_error(ctx,error):
  await ctx.send('error')
  await ctx.send(error)

def setup(bot):
  bot.add_command(add)
  
```

### 2. เพิ่มด้วยวิธีปกติในโฟลเดอร์ commands (advanced)

แนะนำให้ไปอ่าน README.md ในโฟลเดอร์ commands ก่อน จะได้เข้าใจว่าเขียน command ยังไง วิธีนี้อาจจะดูซับซ้อนกว่าวิธีข้างบน แต่จะทำให้เราใช้เครื่องมือต่าง ๆ จาก discord.py ได้โดยตรงเลย เราเลยสามารถทำอะไรคูล ๆ ได้มากกว่าวิธีก่อนหน้านี้

```python
from discord.ext import commands

@commands.command()
async def command_name(ctx, *args):
  # ทำทุกอย่างในนี้
  pass

def setup(bot):
  bot.add_command(command_name)
```
