# from discord.ext import commands
from discord.utils import get

role_message_id = 852161510611615754
role_id = 851182716573319218
guild_id = 843853192902737970
textchannel_id = 851963652973789214

client = None
guild = None
textchannel = None
message = None

async def on_raw_reaction_add(payload):
  if payload.message_id == role_message_id:
    try:
      role = get(guild.roles, id=role_id)
      member = get(guild.members, id=payload.user_id)
      await member.add_roles(role)
    except:
      print('role assignment error has occur')
    
async def on_raw_reaction_remove(payload):
  if payload.message_id == role_message_id:
    try:
      role = get(guild.roles, id=role_id)
      member = get(guild.members, id=payload.user_id)
      await member.remove_roles(role)
    except:
      print('role assignment error has occur')

async def setup(bot):
  global client
  global guild
  global textchannel
  global message

  client = bot
  guild = client.get_guild(guild_id)
  textchannel = get(guild.text_channels, id=textchannel_id)
  message = await textchannel.fetch_message(role_message_id)
  await message.add_reaction('👍')
  
  bot.add_listener(on_raw_reaction_add)
  bot.add_listener(on_raw_reaction_remove)