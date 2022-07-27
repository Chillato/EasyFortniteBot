import requests
from pyrogram import *
from pyrogram.types import *

api_id = 9
api_hash = ""
bot = ""

fortnite = Client("fortnitestorage", api_id, api_hash, bot_token=bot)

@fortnite.on_message(filters.private & filters.command("start"))
async def avvio(_, message):
    await message.reply_text("messaggio start!")

@fortnite.on_message(filters.command("fortnite"))
async def fortnews(_, message):
    fortnite_news = requests.get("https://fortnite-api.com/v2/news/br").json()
    news = fortnite_news["data"]["image"]
    await fortnite.send_animation(message.chat.id, news, caption="ecco le news di oggi!")


fortnite.run()

# easy fortnite bot :D