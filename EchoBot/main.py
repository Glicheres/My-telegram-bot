import contextlib

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# logging - логи )
import logging
#уникальный id нашего бота
Token = "xxxxxxxxxxxxxxxxx"
#udater получает новые сообщения из telegram (получает инфу о событиях)
updater = Updater(token = Token)
#обработчик событий
dispatcher = updater.dispatcher
#прописываем в каком формате  будет логирование
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Бот повторяет за вами всё что напишите. Приятного пользования)")
    print(update)
    print(context)

def text(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = update.message.text)
start_handler = CommandHandler('start', start)  #/start
text_handler = MessageHandler(Filters.text, text)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_handler)

updater.start_polling()