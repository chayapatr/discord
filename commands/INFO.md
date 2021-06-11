วิธีการใช้งานบอท hackerman

หลัก ๆ แล้วเราสามารถเรียกใช้คำสั่งของ hackerman โดยการพิมพ์ว่า `PREFIX` แล้วตามด้วยชื่อ command

ตัวอย่างเช่น `PREFIXcat`

ทั้งนี้ เราสามารถเรียกคำสั่ง `PREFIXhelp` เพื่อดูคำสั่งทุกอย่าง และ `PREFIXhelp <ชื่อ command>` เพื่อดูข้อมูลเพิ่มเติมของคำสั่งได้

Feature หลัก ๆ ของ hackerman มีดังนี้:

__Grader__

การเรียก command `PREFIXtest` ตามด้วยชื่อ challenge ที่อยากทดสอบ แล้วตามด้วย code ของเราจะทำให้บอทรันโปรแกรมตรวจสอบโค้ดของเรา ซึ่งถ้า output ของโค้ดตรงกับค่าที่ควรจะเป็นหรือเปล่า

`PREFIXtest <challenge_name> <code>`

*Note: สามารถใช้คำสั่ง `PREFIXchallenges` เพื่อดู challenge ทั้งหมดได้*

ตัวอย่างเช่น: 
```
PREFIXtest one a = int(input())
b = int(input())
print(a+b)
```

__การเพิ่ม Command__

`วิธีง่าย`

เพิ่มไฟล์ในโฟลเดอร์ `user_src/` แล้วเขียนแบบปกติเลย โดยโปรแกรมจะแปลง code ในไฟล์นั้นให้กลายเป็น command ที่สามารถใช้กับ discord ได้ โดยจะมีชื่อเหมือนกับไฟล์ที่ตั้งไว้

เช่น ใน `user_src/add.py`:
```python
a = input()
b = input()
print(int(a)+int(b))
```

เสร็จแล้วเราสามารถเรียก command ได้โดยการพิมพ์ว่า `PREFIXadd 1 3` ได้เลย

`วิธี advanced`

วิธีนี้เป็นวิธีที่จะ direct วิธีก่อนหน้านี้มาก เราจึงสามารถทำอะไรได้หลายอย่างกว่า แต่ก็จะทำให้โค้ดของเราซับซ้อนยิ่งขึ้นเหมือนกัน

copy template code นี้แล้วลองไปอ่านไฟล์ README.md ที่อยู่ในโฟลเดอร์ challenges เพื่อทำความเข้าใจกับ discord.py มากขึ้น

Template Code:
```python
from discord.ext import commands

@commands.command()
async def command_name(ctx, *args):
  # ทำทุกอย่างในนี้
  pass

def setup(bot):
  bot.add_command(command_name)
```