from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Application
from telegram import Update
from log import *
from fractions import Fraction


value1 = None
value2 = None
complex_operation = None
text_message = ""
is_entered = False

async def start_calc_rat(app: Application, update, operation):
    log(update)
    global complex_operation
    complex_operation = operation
    app.add_handler(CommandHandler("calc_rat", answer))
    await question(update)

async def question(update: Update):
    change_text()
    await update.message.reply_text(text_message)

async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    global value1
    global value2
    log(update)
    msg = update.message.text
    try:
        items = msg.split()
        x = int(items[1])
        y = int(items[2])
        if y == 0:
            await update.message.reply_text("Неверный ввод знаменателя. Попробуйте ещё раз.")
            return
        if value1 == None:
            value1 = Fraction(x, y)
            await question(update)
            return
        if value2 == None:
            value2 =  Fraction(x, y)
            await calc(update)
    except ValueError:
        await update.message.reply_text("Неверный ввод. Попробуйте ещё раз.") 

def change_text():
    global text_message
    num = 1
    if(value1 == None):
        num = 1
    elif(value2 == None):
        num = 2
    text_message = f"Введите команду /calc_rat, в сообщении через пробел числитель и знаменатель {num} рационального числа."

async def calc(update: Update):
    global value1
    global value2
    if complex_operation == 11:
        res = value1 + value2
    elif complex_operation == 22:
        res = value1 - value2
    elif complex_operation == 33:
        res = value1 * value2
    elif complex_operation == 44:
        res = value1 / value2
    else:
        res = value1 % value2
    log_in(update, complex_operation, value1, value2, res)
    await update.message.reply_text( f"Результат {res}")
    
    value2 = None
    value1 = None
