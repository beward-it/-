import telebot
global sum1
import random
name="Гость"
f=open('dataTelCas.txt','a+t')
sum=100
bot=telebot.TeleBot('6642421516:AAHOSME3tLkUHdEUdNAnCka0mcLShZYGLvY')
@bot.message_handler(commands=['start'])
def firstText(mess):
    bot.reply_to(mess,"Приветствуем вас в нашем боте! Извините пока не все функции бота работают.")
@bot.message_handler(commands=['usdat'])
def q(mess):
    answ="Ваше имя:"+name+" Ваш балланс:"+str(sum)
    bot.reply_to(mess,answ)
@bot.message_handler(commands=['spin'])
def spin(mess):
    ii=0
    iii=0
    while ii==0:
        while iii==0:
            bot.reply_to(mess,"Введите сколько вы хотите поставить")
            @bot.message_handler(func=lambda message :True)
            def spin1(mess):
                sum1=mess.text
                try:
                    sum1=int(sum1)
                    ii=1
                    iii=1
                    return int(sum1)
                except:
                    bot.reply_to(mess,"Это не число")
        if sum1<=sum:
            sum=sum-sum1
            bot.reply_to(mess,"Крутим!")
            luck=random.randint(1,6)
            luck1=random.randint(1,6)
            luck2=random.randint(1,6)
            lucks="Выпало: "+str(luck)+" "+str(luck1)+" "+str(luck2)
            bot.reply_to(mess,lucks)
            if luck==luck1 and luck==luck2:
                bot.reply_to(lucks,"Три одинаковые цифры, ваша ставка утраивается!")
                sum+=3*sum1
            elif luck==luck1 or luck1==luck2 or luck==luck2:
                bot.reply_to(lucks,"Две одинаковые цифры, Ваша ставка удваивается!")
                sum=2*sum1
            else:
                bot.reply_to(lucks,"К сожалению вы проиграли.")
@bot.message_handler(commands=['support'])
def w(mess):
    answ="Напишите @dictatorgroup10 или @perdunwon"
    bot.reply_to(mess,answ)
bot.polling(none_stop=True,interval=0)
