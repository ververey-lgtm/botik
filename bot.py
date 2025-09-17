# Временный диагностический код
def check_file_content():
    try:
        with open(__file__, 'r', encoding='utf-8') as f:
            content = f.read()
            print("=== НАЧАЛО ФАЙЛА ===")
            print(repr(content[:200]))  # Покажем первые 200 символов
            print("=== КОНЕЦ ФАЙЛА ===")
            
            # Ищем проблемную строку
            if '* text=auto' in content:
                print("ОБНАРУЖЕНА ПРОБЛЕМНАЯ СТРОКА!")
                print("Её позиция:", content.find('* text=auto'))
    except Exception as e:
        print("Ошибка при чтении файла:", e)

# Вызовем проверку до всего остального
check_file_content()

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.message.from_user.first_name
    await update.message.reply_text(f'Привет, {user_name}! Я работаю на Render!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = "Я тестовый бот. Команды: /start, /help"
    await update.message.reply_text(help_text)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    
    url = f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}"
    print(f"Bot starting with URL: {url}")
    
    app.run_webhook(
        listen="0.0.0.0",
        port=10000,
        url_path=TOKEN,
        webhook_url=f"{url}/{TOKEN}"
    )

if __name__ == '__main__':
    main()
