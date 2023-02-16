#Example how to use conv module
from pyrogram import filters,Client
import time
bot = "token616dnddndzYVo"
from pyrogram.types import Message
app = Client("exxam",api_id=732605,api_hash="59c30695447fdb83a89016571ba9eb9d")



#smod(c,msg,ask,placeholder = "Send required information...",timeout=30,msg_limit=150,stop_cmd = "/cancel")

from conv import smod

@app.on_message(filters.command("start"))
async def chand(c,msg):
  ask = "What is your name ?"
  x = await smod(c,msg,ask)
  if x.error:
   await msg.reply(x.error)
   return
  y = await smod(c,msg,"Father name!?")
  if y.error:
   await msg.reply(y.error)
  await msg.reply(f"You name is {x.text} and father name is {y.text}...")
 
app.run()
