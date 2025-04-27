import telebot
bot=telebot.TeleBot('6642421516:AAGYb7sg9cRq7_0lOQSir53QnL0xVGdCQ9U')
@bot.message_handler(commands=['start','usdat','spin','reg','support','aut','withdraw','prem'])
def tehWorks(mess):
    id=mess.chat.id
    bot.send_message(id,"Технические работы. Зайдите в бот позже.")
bot.polling(none_stop=True,interval=0)