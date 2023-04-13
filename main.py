from env import BOT_TOKEN
import telebot
from functions import load_counters, make_dict, main

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['go'])
def welcome(message):
    bot.send_message(message.chat.id, 'Введите дату для выгрузки!')
    bot.register_next_step_handler(message, work_process)


def work_process(message):
    payload = load_counters(message.text)
    main_dict = make_dict(payload)
    result = main(main_dict)
    bot.send_message(message.chat.id, f'Обработанно {result[0]} из {result[1]}. Ошибок {result[2]}')


bot.polling()
