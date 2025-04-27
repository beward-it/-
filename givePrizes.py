import telebot
import random
bot=telebot.TeleBot('6642421516:AAGYb7sg9cRq7_0lOQSir53QnL0xVGdCQ9U')
with open('dataTelCas.txt') as f:
    for a in f:
        name,passw,sum,id,isP,v=a.split()
        year,month,dat=v.split("-")
        if int(month)<=3 and int(dat)<14:
            sum=int(sum)
            sum1=random.randint(200,500)
            print(name,sum1,sum)
            with open ('dataTelCas.txt', 'r') as a:
                old_data = a.read()
                new_data = old_data.replace(name+" "+passw+" "+str(sum)+" "+str(id)+" "+isP+" "+v,name+" "+passw+" "+str(sum+sum1)+" "+str(id)+" "+isP+" "+v)
            with open ('dataTelCas.txt', 'w') as a:
                a.write(new_data)
            bot.send_message(id,f"Спасибо за участие в бета тестировании! Вам подарок в размере {sum1} !")
