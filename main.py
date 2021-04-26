import telebot
import threading
from threading import Thread
import time

from queue import Queue

q = Queue()

class Sender(Thread):
  def __init__(self, val, message, inputq):
    Thread.__init__(self)
    self.val = val
    self.message = message
  
    self.inputq = inputq
     	
  def run(self):
    while True:
      data = None
      if self.inputq.empty() is False:
        data = self.inputq.get(timeout=1)
        print(data)
        if data[self.message.chat.id] == "stop": break
      time.sleep(self.val)
      self.delayed_send(self.message.chat.id)
  
  def delayed_send(self, id):
    bot.send_message(id, '<3') 
  
  def id(self): 
    return message.chat.id   
  
  def terminate(self):
    self._running = False


TOKEN = open("config").read()
print(TOKEN)
bot = telebot.TeleBot('918854063:AAE8-0Pr5KS_g31hevSpbT-ouF-AJvt0De8')#TOKEN)


@bot.message_handler(commands=['start'])
def reg_text(message):
  bot.send_message(message.chat.id, 'You have to wait..')
  
  Sender(10, message, q).start()

@bot.message_handler(commands=['stop'])
def stop_notifications_for(message):
  q.put({message.chat.id: "stop"}) 

bot.polling(none_stop=True)

