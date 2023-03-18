from pyrogram import filters,Client

from pyrocon import patch

bot = "6166806041:AAE_ZxX0VfcdkvcvTp4my-Vpjj_Xue8zYVo"

app = Client("realblt",api_id = 1415407,api_hash = "118d68f87563b5c3b2b4ef7c4149f3d4",bot_token=bot)

 
quiz = patch(app,clear=True)


@app.on_message(filters.command("start"))  

async def clear(client,message):

    answer = await quiz.ask(message,"How are you bro?")

    await answer.reply(f"your answer is {ans.text}")

app.run()
