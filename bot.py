python
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

user_states = {}

def create(update, context):
    update.message.reply_text(
        "1. Go to BotFather\n"
        "2. Create a new bot\n"
        "3. Copy the bot token\n"
        "4. Send it here"
    )
    user_states[update.effective_user.id] = 'awaiting_token'

def handle_token(update, context):
    user_id = update.effective_user.id
    if user_states.get(user_id) == 'awaiting_token':
        token = update.message.text.strip()
        update.message.reply_text("Setting up your reactor bot...")
        import subprocess
        subprocess.Popen(["python", "reactor_bot_runner.py", token])
        update.message.reply_text("Your bot is live with reactor features!")
        user_states[user_id] = None

updater = Updater("7609560980:AAEqVWKDKZMYSZbf9GOswKzK8TCOwYiZDCg", use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("create", create))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_token))
updater.start_polling()
