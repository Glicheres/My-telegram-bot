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
# теперь добавляем в диспатчер фильтрующие хендлеры.... Помним - что выше стоит, то важнее в обработке(по приоретету)
dispatcher.add_handler(URL_handler)
dispatcher.add_handler(voise_audio_handler)
dispatcher.add_handler(text_handler)
dispatcher.add_handler(forwarded_P_V_handler)
dispatcher.add_handler(photo_video_handler)
updater.start_polling()