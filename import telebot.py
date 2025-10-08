import telebot
TOKEN = "7628595465:AAHgUHi-smK7UE8XayKD8ms_EBTF6PsqV-4"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def handle_message(message):

    bot.send_message(message.chat.id, 'hello, my name is Тестовый бот')

@bot.message_handler(commands=['help'])
def hel_p(message):

    bot.send_message(message.chat.id, 'no')

print('ok')
bot.polling(
    none_stop=True,
    interval=1
)