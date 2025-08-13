python
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import asyncio

Dictionary to keep track of running bots
running_bots = {}

Example user data (you can load from file/db)
user_data = {
    "123456789": {
        "token": "7609560980:AAEqVWKDKZMYSZbf9GOswKzK8TCOwYiZDCg",
        "reacts": ["💗", "🥰", "💫", "🌸", "😍", "🤩", "💖", "💓"]
    }
}

async def start_bot(user_id, token, reacts):
    bot = Bot(token=token)
    dp = Dispatcher(bot)

    @dp.message_handler()
    async def react_to_messages(msg: Message):
        for emoji in reacts:
            try:
                await msg.reply(emoji)
            except:
                pass

    running_bots[user_id] = bot
    await dp.start_polling()

def run_all_bots():
    loop = asyncio.get_event_loop()
    for user_id, data in user_data.items():
        loop.create_task(start_bot(user_id, data["token"], data["reacts"]))
    loop.run_forever()

if _name_ == "_main_":
    run_all_bots()
