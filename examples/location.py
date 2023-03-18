from pyrogram import filters,Client
from pyrocon import patch

bot = "61668fndmdcdkvcvTp4my-Vpjj_Xue8zYVo"

app = Client("realblt",api_id = 15407,api_hash = "563b5c3b2b4e4149f3d4",bot_token=bot)
quiz = patch(app,clear=True)

@app.on_message(filters.command("start"))  
async def clear(client,message):
    answer = await quiz.ask(message,"How are you bro?")
    await answer.reply(f"your answer is {ans.text}")

app.run()
