import telebot
import random
TOKEN = "7628595465:AAHgUHi-smK7UE8XayKD8ms_EBTF6PsqV-4"
bot = telebot.TeleBot(TOKEN)
users_info = {}
class myex(Exception):
    pass
@bot.message_handler(commands=['start'])
def handle_message(message):

    bot.send_message(message.chat.id, 'hello, i guessed a number from 1 to 100, can you gues it for 7 attempts')

@bot.message_handler(content_types=['text'])
def no_w(message):
    user_id = message.chat.id
    txt = message.text.strip().lower()
    if txt == "начать":
        n = random.randint(1, 100)
        users_info[user_id] = {
            'number': n,
            'tries': 0
        }
        bot.send_message(user_id, "im ready, gues")
    else:
        try:
            n = int(txt)
            if user_id not in users_info:
                raise myex('not start')
            if not 1 <= n <= 100:
                raise myex('not for 1 to 100')
            users_info[user_id]['tries']+=1
            h = users_info[user_id]['number']
            k = users_info[user_id]['tries']
            if n == h:
                bot.send_message(user_id, f' correct {k}')
            elif n<h:
                bot.send_message(user_id, 'bigger')
            else:
                bot.send_message(user_id, 'smaller')
        except ValueError:
            bot.send_message(user_id, 'error, you must type начать')

print('ok')
bot.polling(
    none_stop=True,
    interval=1
)