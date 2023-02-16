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
  answer = await smod(c,msg,ask)
  if not answer.error:
   print(answer.text)
 

app.run()
