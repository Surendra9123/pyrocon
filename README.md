install pyrocon using pip

```pip3 install -U pyrocon```

#Conversation in pyrogram 

```from pyrocon import patch```

#```patch(client,clear,timeout,stop_cmd,placeholder)```

```client``` : "Client" required parameter ( Pyrogram Client )

```clear``` : "bool" required parameter set true if you want delete msg after get answer(Default to False)

```timeout``` : "int" optional parameter (Default to 30 sec)

```cquery``` : "bool" parameter set True when asking with inline buttons (Default to ```False```)

```stop_cmd``` : "str" optional parameter (Default to ```/cancel```)

```placeholder``` : "str" optional parameter (Custom placeholder for Forcereply)

```filter``` : pyrogram filters optional parameter (Default to filters.text)


#```patch.ask(update,text,cquery,filter)```

```update``` : "Message/CallbacQuery" required parameter (Where to start conv..)

```text``` : "str" Required parameter (Question to ask)

```cquery``` : "bool" Parameter set True when asking with inline buttons (Default to ```False```)

```filter``` : Pyrogram filters optional parameter (Default to filters.text)





#**using example:**

**Create quiz instance**
```
  from pyrocon import patch
  from pyrogram import Client,filters
  
  app = Client(...)
  quiz = (app)
  
  answer = await quiz.ask(message,text)
  if answer.text:
    print(answer.text)
  answer.reply("I got answer..")
```


**handle text messages**

```
  answer = await quiz.ask(message,text)
  if answer.text:
    print(answer.text)
  answer.reply("I got answer..")
  ```

**handle CallbackQuery / inline buttons**

```
  answer = await quiz.ask(CallbacQuery,text,cquery=True)
  if answer.text:
    print(answer.text)
  answer.reply("I got answer..")
  ```

**Using pyrogram filters**

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


