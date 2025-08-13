python
from telegram.ext import CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text("Welcome! Send /create to begin creating your own reactor bot.")

def create(update, context):
    steps = (
        "1. Go to @BotFather\n"
        "2. Create a new bot\n"
        "3. Copy the bot token\n"
        "4. Send me the token here"
    )
    update.message.reply_text(steps)

def handle_token(update, context):
    token = update.message.text.strip()
    if len(token) > 40:
        update.message.reply_text("Got the token. Setting up your bot...")
        # এখানে custom bot setup কোড থাকবে
    else:
        update.message.reply_text("Invalid token. Please try again.")

def setup_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("create", create))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_token))
