from email.mime import application
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from log import *
from complex_calc import start_calc_com
from rational_calc import start_calc_rat

app = None

def start(bot):
    global app
    app = bot

    app.add_handler(CommandHandler("start", start_bot))
    app.add_handler(CommandHandler("help", help_bot))

    app.add_handler(CommandHandler("menu_com", menu_com))
    app.add_handler(CommandHandler("1", menu_complex_sum))
    app.add_handler(CommandHandler("2", menu_complex_minus))
    app.add_handler(CommandHandler("3", menu_complex_multi))
    app.add_handler(CommandHandler("4", menu_complex_div))

    app.add_handler(CommandHandler("menu_rat", menu_rat))
    app.add_handler(CommandHandler("11", menu_rational_sum))
    app.add_handler(CommandHandler("22", menu_rational_minus))
    app.add_handler(CommandHandler("33", menu_rational_multi))
    app.add_handler(CommandHandler("44", menu_rational_div))
    app.add_handler(CommandHandler("55", menu_rational_remainder_division))


async def start_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update)
    text_start = ("/menu_com Калькулятор комплекстных чисел\n"
                 "/menu_rat Калькулятор рациональных чисел\n"
                )
    await update.message.reply_text(text_start)

async def help_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update)
    await update.message.reply_text(f'/start\n/menu_com\n/menu_rat\n/help')

async def menu_com(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update)
    text_menu = ("Калькулятор Комплекстных чисел\n"
                 "/1 Сложение чисел\n"
                 "/2 Вычитание чисел\n"
                 "/3 Умножение чисел\n"
                 "/4 Деление чисел\n"
                 )
    await update.message.reply_text(text_menu)


async def menu_rat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update)
    text_menu = ("Калькулятор Рациональных чисел\n"
                 "/11 Сложение чисел\n"
                 "/22 Вычитание чисел\n"
                 "/33 Умножение чисел\n"
                 "/44 Деление чисел\n"
                 "/55 Взятие остатка от деления"
                 )
    await update.message.reply_text(text_menu)


async def menu_complex_sum(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start_calc_com(app, update,  1)


async def menu_complex_minus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start_calc_com(app, update,  2)


async def menu_complex_multi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start_calc_com(app, update,  3)


async def menu_complex_div(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start_calc_com(app, update,  4)


async def menu_rational_sum(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start_calc_rat(app, update,  11)


async def menu_rational_minus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start_calc_rat(app, update,  22)


async def menu_rational_multi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start_calc_rat(app, update,  33)


async def menu_rational_div(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start_calc_rat(app, update,  44)

async def menu_rational_remainder_division(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start_calc_rat(app, update,  55)

