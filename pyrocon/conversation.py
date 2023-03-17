from pyrogram.types import ForceReply,Message,CallbackQuery
import asyncio
import logging
from .errors import errors
from pyrogram import Client,filters
from pyrogram.filters import Filter

class quiz:
  async def ask(client,update,ask,timeout=30,cquery=False,filter=False,stop_cmd = "/cancel",placeholder = "Send required information...",msg_limit=80):
     if not isinstance(client,Client):
        print("1st parameter/client must be pyrogram Client object")
        return errors.basic
     if not isinstance(cquery,bool):
        print("5th parameter/cquery must be Boolean (True or False)")
        return errors.basic
     if (cquery and (not isinstance(update,CallbackQuery))) or ((not cquery) and (not isinstance(update,Message))):
        if cquery:
         print("2nd parameter/msg must be CallbackQuery object")
         return errors.basic
        else:
         print("2nd parameter/msg must be Message object")
         return errors.basic      
     if not isinstance(ask,str):
        print("3rd parameter/ask must be str")
        return errors.basic
     if not isinstance(timeout,int):
        print("4th parameter/timeout must be Integer")
        return errors.basic
     if not isinstance(stop_cmd,str):
        print("7th parameter/stop_cmd must be str")
        return errors.basic
     if not isinstance(placeholder,str):
        print("8th parameter/placeholder must be str")
        return errors.basic
     if not (isinstance(filter,bool) or isinstance(filter,Filter)):
        print("6th parameter/filter must be filter object")
        return errors.basic
     try:
      ans = await asyncio.wait_for(quiz.wait(client,update,ask,placeholder,msg_limit,stop_cmd,cquery,filter),timeout= timeout)
     except Exception as e:
      logging.info("Time Out!")
      ans = errors.timeout
     return ans      


  async def wait(c,msg,ask,placeholder,msg_limit,stop_cmd,cquery,filter):
   try:
     if msg.from_user:
      anonymous = False
      user_id = msg.from_user.id
     else:
      anonymous = True
      user_id = msg.sender_chat.id
   except Exception as e:
     logging.info(e)
     user_id = None
   if user_id:
    if cquery:
     uv = await c.send_message(msg.message.chat.id,ask,reply_markup=ForceReply(selective=True, placeholder=placeholder))
    else:
     uv = await msg.reply(ask,reply_to_message_id = msg.id,reply_markup=ForceReply(selective=True, placeholder=placeholder))
    while True:
     try:
      ids = [uv.id+x for x in range(msg_limit)]
      ids.pop(0)
      for ans in (await c.get_messages(uv.chat.id,ids)):
        ans.error = errors.unknown
        try:
          if anonymous:
           user_id2 = ans.sender_chat.id
          else:
           user_id2 = ans.from_user.id
        except:
         user_id2 = "Nonne"
        if filter:
         is_user = True
        else:
         is_user = True if (user_id2 == user_id) else False
        if ans and (not ans.empty) and (ans.text == stop_cmd) and is_user:
           ans = errors.cancel
           break
        if ans and (not ans.empty) and is_user:
          if filter:
            fil = await filter(c,ans)
          else:
           fil = await filters.text(c,ans)
          if fil:
           ans.error = ans.cancel = ans.timeout = ans.anon = ans.unknown= False
           break
      if (not ans.error) or (ans == errors.cancel):
       break
     except Exception as e:
      logging.info(e)
      break
    return ans
   else:
    return errors.unknown
