#Conversation in pyrogram 

```from pyrocon import quiz```

#```await quiz.ask(c,msg,ask,timeout,stop_cmd,placeholder)```

```client``` : "Client" required parameter ( Pyrogram Client )

```update``` : Message/CallbacQuery request parameter (where to start conv..)

```ask``` : "str" required parameter (Question to ask)

```timeout``` : "int" optional parameter (default to 30 sec)

```cquery``` : "bool" parameter set True when asking with inline buttons (default to ```False```)

```stop_cmd``` : "str" optional parameter (default to ```/cancel```)

```placeholder``` : "str" optional parameter (custom placeholder for Forcereply)

```filter``` : pyrogram filters optional parameter (default to filters.text)


#**using example:**

**handle text messages**
```
  from pyrocon import quiz

  answer = await quiz.ask(c,message,ask)
  if answer.text:
    print(answer.text)
  answer.reply("I got answer..")
  ```
**handle CallbackQuery / inline buttons**


```
  from pyrocon import quiz

  answer = await quiz.ask(c,CallbacQuery,ask,cquery=True)
  if answer.text:
    print(answer.text)
  answer.reply("I got answer..")
  ```

**Using pyrogram filters**

 __single filter__ 

```
  from pyrocon import quiz
  from pyrogram import filters

  answer = await quiz.ask(c,update,ask,filter=filters.photo)
  print(answer.photo)

  ```
 __multiple filters__

```
  from pyrocon import quiz
  from pyrogram import filters

  answer = await quiz.ask(c,update,ask,filter=(filters.photo & filters.group))
  print(answer.photo)

  ```


#**Handle any kind of errors**

```
  from pyrocon import quiz

  answer = await quiz.ask(c,update,ask)
  if answer.error:
    print(answer.error)
  ```

#**Handle timeout Errors**

```
  from pyrocon import quiz

  answer = await quiz.ask(c,update,ask)
  if answer.timeout:
    print(answer.timeout)
  ```

#**Handle cancellation Errors**

```
  from pyrocon import quiz

  answer = await quiz.ask(c,update,ask)
  if answer.cancel:
    print(answer.cancel)
  ```

Facts:

#if successful answer is Message object otherwise an error

#answer must be in reply to orginal message and should be a text message otherwise message will be ignored 


