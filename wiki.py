import wikipedia
import telebot

bot = telebot.TeleBot("5583816002:AAFB1T6_gmru1gm8snjxjHBcwMGLcrXu8DM")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, """🍭 Добро пожаловать в Википедию🪙
📍Здесь вы можете чувствовать себя как в Википедии💫
📍Википедия сейчас является самым крупным и наиболее популярным справочником в Интернете🔥
📍Но здесь она намного удобнее чем на сайте🌟
📍Просто дайте запрос и Википедия бот ответит на все ваши вопросы❤️
--------------------------------------
🪐разработчик @muhammadsaid_vosidov 🌪
📢по поводу рекламы писать @muhammadsaid_vosidov 🌪""")
    
@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id,wikipedia.summary(message.text))

bot.polling(none_stop=True)
