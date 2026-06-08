from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8695440286:AAHW04Ejm-bQya3xLjVLIx-gFuuFfGidaAY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("我醒了")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("bot running")
    app.run_polling()

if __name__ == "__main__":
    main()
