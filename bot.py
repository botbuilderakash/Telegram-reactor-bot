python
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from aiogram.filters import Command
import asyncio

API_TOKEN = '7609560980:AAEqVWKDKZMYSZbf9GOswKzK8TCOwYiZDCg'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

ইউজার আইডি অনুযায়ী টোকেন আর রিয়েক্ট ইমোজি স্টোর
user_data = {}

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "👋 Welcome to the Reactor Bot Creator!\n\n"
        "➤ Step 1: Go to @BotFather and create a new bot.\n"
        "➤ Step 2: Copy the bot token.\n"
        "➤ Step 3: Send me the token here.\n\n"
        "Then use /setreact to choose your reaction emojis."
    )

@dp.message(Command("setreact"))
async def set_react_handler(message: Message):
[8/14, 1:12 AM] ChatGPT: if message.from_user.id not in user_data:
        await message.answer("❌ Please send your bot token first.")
        return
    await message.answer("📝 Send me the emojis you want to use as reactions (e.g. 💗🥰💫)")

@dp.message()
async def token_or_react_handler(message: Message):
    user_id = message.from_user.id
    text = message.text.strip()

    # যদি ইমোজি হয়
    if user_id in user_data and 'token' in user_data[user_id] and 'reacts' not in user_data[user_id]:
        user_data[user_id]['reacts'] = list(text)
        await message.answer(f"✅ Reactions set: {' '.join(user_data[user_id]['reacts'])}\n\nNow deploy your bot!")
        return

    # নাহলে এটা টোকেন ধরে নিব
    if text.startswith("bot"):
        user_data[user_id] = {'token': text}
        await message.answer("✅ Token saved! Now use /setreact to choose emojis.")
    else:
        await message.answer("❗ Invalid token format. Please send a valid bot token.")
