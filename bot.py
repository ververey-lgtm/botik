from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.message.from_user.first_name
    await update.message.reply_text(f'Привет, {user_name}! Я живу на сервере Render!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = "Вот что я умею:\n/start - Приветствие\n/help - Справка\n/secret - Секрет"
    await update.message.reply_text(help_text)

async def secret(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Сервер работает! ✅')

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("secret", secret))
    
    url = f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}"
    app.run_webhook(
        listen="0.0.0.0",
        port=10000,
        url_path=TOKEN,
        webhook_url=f"{url}/{TOKEN}"
    )

if __name__ == '__main__':
    main()
