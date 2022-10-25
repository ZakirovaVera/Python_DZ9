from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from menu_com import start


app = ApplicationBuilder().token("5788701934:AAGm-TZzvLXZzqGfbldFQ7rSHER3NTfHsZI").build()

start(app)

print("start")
app.run_polling()
