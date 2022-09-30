import wikipedia
import telebot

bot = telebot.TeleBot("5029797787:AAECfpsaru2HPn-wo2e4-A3lCWhKST0WbcY")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id,wikipedia.summary(message.text))

bot.polling(none_stop=True)
