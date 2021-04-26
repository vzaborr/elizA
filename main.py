import telebot
from threading import Thread
import time

class Sender(Thread):
  def __init__(self, val, message):
    Thread.__init__(self)
    self.val = val
    self.message = message

  def run(self):
    time.sleep(self.val)
    self.delayed_send(self.message.chat.id)
  
  def delayed_send(self, id):
    bot.send_message(id, '<3') 

   

TOKEN = open("config").read()
print(TOKEN)
bot = telebot.TeleBot('918854063:AAE8-0Pr5KS_g31hevSpbT-ouF-AJvt0De8')#TOKEN)

@bot.message_handler(content_types=['text'])
def reg_text(message):
  bot.send_message(message.chat.id, 'You have to wait..')
  
  Sender(10, message).start()

bot.polling(none_stop=True)

