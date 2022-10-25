from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


SOURCE_PATH = "task.csv"


def log(update: Update):
    b = datetime.datetime.now()
    file = open(SOURCE_PATH, 'a')
    file.write(f"{b.strftime(' %Y - %m - %d - %H: %M: %S')}, {update.effective_user.id}, {update.message.text}\n")
    file.close() 

def log_in(update: Update, operation, op1, op2, result):
    b = datetime.datetime.now()
    with open(SOURCE_PATH, 'a', encoding="UTF-8") as source:
        source.write(f"{b.strftime(' %Y - %m - %d - %H: %M: %S')}, {update.effective_user.id} - операция {operation} - {op1} - {op2} - результат {result}\n")
        return 0