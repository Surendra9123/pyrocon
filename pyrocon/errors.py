from pyrogram.types import ForceReply
import asyncio
import logging

class errors:
   class timeout:
     code,text,anon,cancel = 100,None,False,False
     timeout = error = "[100] Time Out!"
   class anon:
     code,text,timeout,cancel = 101,None,False,False
     anon = error = "[101] Anonymous users can't be used this module...!"
   class cancel:
     code,text,timeout,anon = 102,None,False,False
     cancel = error = "[102] Listening cancelled...!"
      