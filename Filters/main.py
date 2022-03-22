import contextlib
import random

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Defaults
from telegram import Update, ParseMode, MessageEntity
from telegram.ext import CallbackContext

# logging - логи )
import logging
#уникальный id нашего бота
Token = "xxxxxxxxxx"
#udater получает новые сообщения из telegram (получает инфу о событиях)
updater = Updater(token = Token)
#обработчик событий
dispatcher = updater.dispatcher
#прописываем в каком формате  будет логирование
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)



def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет Мир!\n\n/put [переменная] [значение]\n/get переменная[]\n/sum [переменная] [переменная] = #сумма#")

def number(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    key = context.args[0]
    value = context.args[1]
    print(context.user_data)
    context.user_data[key] = value
    print(context.user_data)
    context.bot.send_message(chat_id=update.effective_chat.id, text=key+" = "+value)


def get(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    key = context.args[0]
    if key in context.user_data:
        update.message.reply_text(context.user_data[key])
    else:
        update.message.reply_text("Error")

def sum(update: Update, context: CallbackContext) -> None:
    key1 = context.args[0]
    key2 = context.args[1]
    if (key1 and key2) in context.user_data:
        update.message.reply_text(int(context.user_data[key1])+int(context.user_data[key2]))
    else:
        update.message.reply_text("Error")

def text(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ты пишешь мне что-то...\nНо пишешь это без уважения..." \
                                                                    "\nПропиши /start, посмотрим что я могу тебе предлжить")

#photo_video
def p_v(update,context):
    x = random.randint(0,4)
    mess_opt = ["Я нахожусь на стадии разработки, не могу ничем помочь тебе с этим","И что мне делать с этим?","Я не умею редактировать ни фото, ни видео(","Да, да... красивое)","Ого...\n\n\nТы прислал мне то, с чем я ничего не могу поделать("]
    context.bot.send_message(chat_id=update.effective_chat.id, text=mess_opt[x])

def f_p_v(update,context):
    text = "*Что-то интересное ты мне прислал...\nЖаль что не могу посмотреть(*"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode = ParseMode.MARKDOWN)
def voise_audio(update,context):
    x = random.randint(0,3)
    mess_opt = ["Голосовое, как мило","Эти прекрасные звуки, ох эти прекрасные звуки","Я глухой, но не немой, прекрати меня мучать","Стадия разработки тебе о чём-нибудь говорит?\nНу не умею я пока ничего("]
    context.bot.send_message(chat_id=update.effective_chat.id, text=mess_opt[x])

def URL(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Интересная ссылка)\n\nСделаем вид что я её не видел :з")


text_handler = MessageHandler(Filters.text, text) #фильтр текста
photo_video_handler = MessageHandler(Filters.photo | Filters.video,p_v) #фильтр Фото и видео
forwarded_P_V_handler = MessageHandler(Filters.forwarded & (Filters.photo | Filters.video),f_p_v ) #пересланные сообщения
URL_handler = MessageHandler(Filters.entity(MessageEntity.URL),URL) #ссылка
voise_audio_handler = MessageHandler(Filters.voice,voise_audio) #ссылка

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler("put", number))
dispatcher.add_handler(CommandHandler("get", get))
dispatcher.add_handler(CommandHandler("sum", sum))

# теперь добавляем в диспатчер фильтрующие хендлеры.... Помним - что выше стоит, то важнее в обработке(по приоретету)
dispatcher.add_handler(URL_handler)
dispatcher.add_handler(voise_audio_handler)
dispatcher.add_handler(text_handler)
dispatcher.add_handler(forwarded_P_V_handler)
dispatcher.add_handler(photo_video_handler)

updater.start_polling()