from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8695440286:AAHW04Ejm-bQya3xLjVLIx-gFuuFfGidaAY"

def reply(text):
    text = text.lower()

    if "在嗎" in text:
        return "哼……我一直都在。"
    if "你好" in text:
        return "……有事嗎。"
    if "喜歡" in text:
        return "別亂說笨蛋。"
    
    return "我不想理你。"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("黑貓已連線。")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    await update.message.reply_text(reply(msg))

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, chat))

app.run_polling()
