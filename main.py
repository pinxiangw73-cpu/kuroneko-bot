from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

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
import os
print("ENV KEYS:", list(os.environ.keys()))
import os
print("ALL ENV:", dict(os.environ))
import os
print(list(os.environ.keys()))
print("BOT_TOKEN =", repr(os.getenv("BOT_TOKEN")))
print("ALL KEYS =", list(os.environ.keys()))
