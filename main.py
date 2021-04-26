import telebot
import threading
from datetime import datetime
from datetime import timedelta

import time

TOKEN = open("config").read()
print(TOKEN)
bot = telebot.TeleBot('918854063:AAE8-0Pr5KS_g31hevSpbT-ouF-AJvt0De8')#TOKEN)

@bot.message_handler(content_types=['text'])
def reg_text(message):
  bot.send_message(message.chat.id, 'You have to wait..')
  now = datetime.now()
  run_at = now + timedelta(seconds=5)
  delay = (run_at - now).total_seconds()
  
  #threading.Timer(delay, delayed_send, message).start()  
  time.sleep(delay)
  delayed_send(message) 

def delayed_send(message):
  bot.send_message(message.chat.id, '<3') 
bot.polling(none_stop=True)
