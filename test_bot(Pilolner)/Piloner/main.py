import contextlib

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
from telegram.ext import CallbackContext

# logging - логи )
import logging
#уникальный id нашего бота
Token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
#udater получает новые сообщения из telegram (получает инфу о событиях)
updater = Updater(token = Token)
#обработчик событий
dispatcher = updater.dispatcher
#прописываем в каком формате  будет логирование
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)



def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += int(number)
    return total

def start(update, context):
    # в контексте боту говорим отправлять сообщение по чат id - текущему чат id
    # у контекста много полей, в том числе .bot (выполнить что то от имени бота)
    # кстати, в update хранится вся информация о событиях  - по сути словарь с информацией
    context.bot.send_message(chat_id=update.effective_chat.id, text="Бот находится на СТАДИИ РАЗРАБОТКИ!\n\n\nP.S /help")
    print(update)
    print(context)

help_text = "\nТестирую как могу, ковыряюсь, разбираюсь пока не станет скучно)\nКоманды моего славненького бота:" \
            "\n/start - начнём переписку)\n/help - узнать информаю о командах\n/sum - введите чиселки, бот их сложит вместо вас" \
            "\n/echo - повторяет за вами"
def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)
    print(update)
    print(context)

def bot_summ(update,context):
    sum_args = context.args
    try:
        for number in sum_args:
            x = int(number)
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ты зачем такое пишешь? Мне числа нужны а ты тут со своими буквами((")
        return 0
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Сумма = {sum_numbers(sum_args)}")

def echo(update, context):
    chat = ' '.join(context.args)
    context.bot.send_message(chat_id=update.effective_chat.id, text=chat)

def text(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ты пишешь мне что-то...\nНо пишешь это без уважения..." \
                                                                    "\nПропиши /help, посмотрим что я могу тебе предлжить")

text_handler = MessageHandler(Filters.text, text) #фильтр
# по команде боту старт выполняем функцию старт
start_handler = CommandHandler('start', start)  #/start
help_handler = CommandHandler('help', help)  #/help
sum_handler = CommandHandler('sum', bot_summ)  #/sum
echo_handler = CommandHandler('echo', echo)  #/echo
# добавляем к обработчику событий этот хэйндлер
# Под handler обычно подразумевается обработчик чего-то (каких-то событий, входящих соединений, сообщений и т.д.)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(sum_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(text_handler)

updater.start_polling()