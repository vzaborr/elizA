import telebot
import threading
from datetime import datetime
from datetime import timedelta

import time
import schedule

import logging

logging.basicConfig()
schedule_logger = logging.getLogger('schedule')
schedule_logger.setLevel(level=logging.DEBUG)


TOKEN = open("config").read()
print(TOKEN)
bot = telebot.TeleBot('918854063:AAE8-0Pr5KS_g31hevSpbT-ouF-AJvt0De8')#TOKEN)

@bot.message_handler(content_types=['text'])
def reg_text(message):
  bot.send_message(message.chat.id, 'You have to wait..')
  now = datetime.now()
  run_at = now + timedelta(seconds=5)
  delay = (run_at - now).total_seconds()
  """ 
  #threading.Timer(delay, delayed_send, message).start()  
  time.sleep(delay)
  delayed_send(message) 
  """
  schedule.every(3).seconds.do(delayed_send, id=message.chat.id)  
  schedule.run_all()
  
  #schedule.clear()
def delayed_send(id):
  bot.send_message(id, '<3') 

bot.polling(none_stop=True)

while True:
 schedule.run_pending()
