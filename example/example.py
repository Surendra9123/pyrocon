#Example how to use conv module
from pyrogram import filters,Client
import time
bot = "token616dnddndzYVo"
from pyrogram.types import Message
app = Client("znznxn",api_id=73962605,api_hash="59csgnshmhm30695447fdb83a89016571ba9eb9d")


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
