install pyrocon using pip

```pip3 install -U pyrocon```

#Conversation in pyrogram 

```from pyrocon import patch```

 **patch(client, clear, timeout, stop_cmd, placeholder)**


__client__ : 'Client' required parameter ( Pyrogram Client )

__clear__ : 'bool' required parameter set true if you want delete msg after get answer(Default to False)

__timeout__ : 'int' optional parameter (Default to 30 sec)

__stop_cmd__ : 'str' optional parameter (Default to __/cancel__)

__placeholder__ : 'str' optional parameter (Custom placeholder for Forcereply)


============================================================


 **patch.ask(update, text, cquery, filter)**


__update__ : 'Message/CallbacQuery' required parameter (Where to start conv..)

__text__ : 'str' Required parameter (Question to ask)

__cquery__ : 'bool' Parameter set True when asking with inline buttons (Default to __False__)

__filter__ : Pyrogram filters optional parameter (Default to __filters.text__)


============================================================


#**using example:**

#**Create quiz instance**
```
  from pyrocon import patch
  from pyrogram import Client,filters
  
  app = Client(...)
  quiz = patch(app)

  @app.on_message(..)  
  async def _(client,message):
    answer = await quiz.ask(message,text)
    if answer.text:
     print(answer.text)
    await answer.reply("I got answer..")

  app.run()
```


#**handle text messages**

```
  answer = await quiz.ask(message,text)
  if answer.text:
    print(answer.text)
  await answer.reply("I got answer..")
  ```

#**handle CallbackQuery / inline buttons**

```
  answer = await quiz.ask(CallbacQuery,text,cquery=True)
  if answer.text:
    print(answer.text)
  await answer.reply("I got answer..")
  ```

#**Using pyrogram filters**

 __single filter__ 

```
  from pyrogram import filters

  answer = await quiz.ask(update,text,filter=filters.photo)
  print(answer.photo)

  ```
 __multiple filters (same as pyrogram)__

```
  from pyrogram import filters

  answer = await quiz.ask(update,text,filter=(filters.photo & filters.group))
  print(answer.photo)

  ```


#**Handle any kind of errors**

```
  answer = await quiz.ask(update,text)
  if answer.error:
    print(answer.error)
  ```

#**Handle timeout Errors**

```
  answer = await quiz.ask(update,text)
  if answer.timeout:
    print(answer.timeout)
  ```

#**Handle cancellation Errors**

```
  answer = await quiz.ask(update,text)
  if answer.cancel:
    print(answer.cancel)
  ```

Facts:

#if successful answer is Message object otherwise an error

#answer must be in reply to orginal message and should be a text message otherwise message will be ignored 


