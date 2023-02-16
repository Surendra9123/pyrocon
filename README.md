# Pyrogram-Conversation {only for bots}

Conversation in pyrogram 

```from pyrocon import pyrocon```

#```await pyrocon.ask(c,msg,ask,timeout,stop_cmd,placeholder)```

```c``` : "Client" required parameter ( Pyrogram Client )

```msg``` : "Message" request parameter (Msg where to start conv..)

```ask``` : "str" required parameter (Question to ask)

```timeout``` : "int" optional parameter (default to 30 sec)

```stop_cmd``` : "str" optional parameter (default to ```/cancel```)

```placeholder``` : "str" optional parameter (custom placeholder for Forcereply)


#**using example:**

```  
  answer = await pyrocon.ask(c,msg,ask)
  if not answer.error:
    print(answer.text)
  ```


#**Handle any kind of errors**

```
  answer = await pyrocon.ask(c,msg,ask)
  if answer.error:
    print(answer.error)
  ```

#**Handle timeout Errors**

```
  answer = await pyrocon.ask(c,msg,ask)
  if answer.timeout:
    print(answer.timeout)
  ```

#**Handle cancellation Errors**

```
  answer = await pyrocon.ask(c,msg,ask)
  if answer.cancel:
    print(answer.cancel)
  ```

Facts:

#if successful answer is Message object otherwise an error

#answer must be in reply to orginal message and should be a text message otherwise message will be ignored 


