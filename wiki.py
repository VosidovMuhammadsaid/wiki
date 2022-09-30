import wikipedia
import telebot

bot = telebot.TeleBot("5583816002:AAFB1T6_gmru1gm8snjxjHBcwMGLcrXu8DM")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id,wikipedia.summary(message.text))

bot.polling(none_stop=True)
