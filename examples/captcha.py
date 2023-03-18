import random
from pyrogram import filters,Client
from pyrocon import patch
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ChatPermissions

bot = "token"
app = Client("blt",api_id = 14407,api_hash = "118d6b2b4ef7c4149f3d4",bot_token=bot)
quiz = patch(app,clear=True)



@app.on_message(filters.new_chat_members & filters.group)  
async def clear(client,message):
 await client.restrict_chat_member(message.chat.id,message.from_user.id,ChatPermissions(can_send_messages=False))
 await client.send_message(message.chat.id,"Go to private chat and solve captcha...!",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Click here to go private..",url=f"http://t.me/botx01bot?start=captcha_{str(message.chat.id)}")]]))

@app.on_message(filters.command("start") & filters.private)  
async def clear(client,message):
 try:
  text = message.text[7:].split("_")
  chat_id = int(text[1])
 except:
  text = None
 if text and text[0] == "captcha":
  try:
    chat = await app.get_chat(chat_id)
  except Exception as a:
    await message.reply(a)
    return
  a = random.choice(range(10))
  b = random.choice(range(10))
  c = a + b
  ans = await quiz.ask(message,f"**what is {a} + {b}?**")
  if ans.text == str(c):
    await client.restrict_chat_member(chat_id,message.from_user.id,ChatPermissions(can_send_messages=True))
    await ans.reply(f"Successful! and approved in {chat.title}")
  else:
    await ans.reply("Try again..!")
 else:
     #anything else
     pass

app.run()
