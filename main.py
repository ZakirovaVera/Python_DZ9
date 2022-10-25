from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from menu_com import start


app = ApplicationBuilder().token("TOKEN").build()

start(app)

print("start")
app.run_polling()
