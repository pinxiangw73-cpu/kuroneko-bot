from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

# /start 指令
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("喵～機器人已啟動！")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    # ⭐ 最重要這一行（一定要有）
    app.run_polling(
        drop_pending_updates=True
    )

if __name__ == "__main__":
    main()
