# Pyrogram-Conversation

Conversation in pyrogram 

Just put conv.py.file where you need to conv and

```from conv import smod```

#```await smod(c,msg,ask,timeout,stop_cmd)```

```c``` : required parameter ( Pyrogram Client )

```msg``` : request parameter (Msg where to start conv..)

```ask``` : required parameter (Question to ask)

```timeout``` : optional parameter (default to 30 sec)

```stop_cmd``` : optional parameter (default to ```/cancel```)

#**using example:**

```  
  answer = await smod(c,msg,ask,timeout,stop_cmd)
  if not answer.error:
    print(answer.text)
  ```


#**Handle any kind of errors**

```
  answer = await smod(c,msg,ask,timeout,stop_cmd)
  if answer.error:
    print(answer.error)
  ```

#**Handle timeout Errors**

```
   answer = await smod(c,msg,ask,timeout,stop_cmd)
   if answer.timeout:
     print(answer.error)```

**Handle cancellation Errors**

```
   answer = await smod(c,msg,ask,timeout,stop_cmd)
   if answer.cancel:
     print(answer.error)

```




