from telegram import Update
from google import genai
import os
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)
# debug（一定要）
print("TOKEN =", repr(BOT_TOKEN))

# /start 指令
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("喵～機器人已啟動！")

def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN 沒有設定")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
