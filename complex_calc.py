from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Application
from telegram import Update
from log import *


value1 = None
value2 = None
complex_operation = None
text_message = ""
is_entered = False

async def start_calc_com(app: Application, update, operation):
    log(update)
    global complex_operation
    complex_operation = operation
    app.add_handler(CommandHandler("calc_com", answer))
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
        x = float(items[1])
        y = float(items[2])
        if value1 == None:
            value1 = [x, y]
            await question(update)
            return
        if value2 == None:
            value2 = [x, y]
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
    text_message = f"Введите команду /calc_com, в сообщении через пробел мнимую и вещественную часть {num} комплексного числа."

async def calc(update: Update):
    global value1
    global value2 
    c1 = complex(value1[0], value1[1])
    c2 = complex(value2[0], value2[1])
    if complex_operation == 1:
        res = c1 + c2
    elif complex_operation == 2:
        res = c1 - c2
    elif complex_operation == 3:
        res = c1 * c2
    else:
        res = c1 / c2
    log_in(update, complex_operation, c1, c2, res)
    await update.message.reply_text( f"Результат {res}")
    
    value2 = None
    value1 = None
