import telebot
import config
from random import randint
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open("static/AnimatedSticker.tgs", "rb")
    bot.send_animation(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('сложение (+)')
    item2 = types.KeyboardButton('вычитание (-)')
    item3 = types.KeyboardButton('умножение (*)')
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     f"Привет, {message.from_user.first_name}!\nДавай я проверю насколько ты хорош в арифметике.\n",
                     parse_mode='html', reply_markup=markup)

res = 'афжловыалд'

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        a, b = randint(1, 100), randint(10, 100)
        global res
        if message.text == 'сложение (+)':
            msg = f"Чему будет равно:\n{a} + {b}"
            bot.send_message(message.chat.id, msg)
            res = f"{a + b}"
        elif message.text == 'вычитание (-)':
            msg = f"Чему будет равно:\n{a} - {b}"
            bot.send_message(message.chat.id, msg)
            res = f"{a - b}"
        elif message.text == 'умножение (*)':
            msg = f"Чему будет равно:\n{a} * {b//10}"
            bot.send_message(message.chat.id, msg)
            res = f"{a * (b//10)}"
        elif message.text == res:
            bot.send_message(message.chat.id, "Ответ верный! 👍")
            # markup = types.InlineKeyboardMarkup(row_width=2)
            # item1 = types.InlineKeyboardButton('Хорошо', callback_data='good')
            # item2 = types.InlineKeyboardButton('Плохо', callback_data='bad')
            # markup.add(item1, item2)
            # bot.send_message(
            #     message.chat.id, 'Отлично! Как сам?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Ответ неверный! ☹️')


# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     try:
#         if call.message:
#             if call.data == res:
#                 bot.send_message(call.message.chat.id,
#                                  "Очень хорошо, я за тебя рад")
#             elif call.data == 'bad':
#                 bot.send_message(call.message.chat.id,
#                                  "Надеюсь, что в будущем будет всё хорошо!")

#             bot.edit_message_text(
#                 chat_id=call.message.chat.id,
#                 message_id=call.message.message_id,
#                 reply_markup=None
#             )
#     except Exception as e:
#         print(repr(e))


bot.polling(none_stop=True)