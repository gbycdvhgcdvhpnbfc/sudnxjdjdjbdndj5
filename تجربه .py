import telebot
import requests

bot = telebot. TeleBot ("7264213709:AAEHqc9rpM4wqMjc8I5yJPuc5_60u7UlwVg")

@bot.message_handler(commands=["start","help"]
def srart(message):
	bot.send_message(message.chat.id,f" Hi Trakos ")
	
	
	bot.polling()