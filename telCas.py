import telebot
import random
import time
from telebot import types
name=None
def checkReg(mess):
    log=False
    f=open('dataTelCas.txt')
    for a in f :
        name1,passw1,sum1,id1=a.split()
        id=mess.from_user.id
        if int(id1)==int(id):
            log=True
            return sum1,name1,log
    if log==False:
        bot.send_message(id,"Сначала зарегистрируйтесь. Нажмите /reg")
        return 0,"None",log
bot=telebot.TeleBot('6642421516:AAGYb7sg9cRq7_0lOQSir53QnL0xVGdCQ9U')
while True:
    try:
        @bot.message_handler(commands=['start'])
        def firstText(mess):
            bot.reply_to(mess,"Приветствуем вас в нашем боте! Извините пока не все функции бота работают.")
        @bot.message_handler(commands=['usdat'])
        def q(mess):
            sum,name,log=checkReg(mess)
            if log:
                answ="Ваше имя:"+str(name)+" Ваш балланс:"+str(sum)
                bot.reply_to(mess,answ)
        @bot.message_handler(commands=['spin'])
        def spin(mess):
            sum,name,log=checkReg(mess)
            id=mess.from_user.id
            ii=0
            iii=0
            if log:
                bot.reply_to(mess,"Введите сколько вы хотите поставить")
                @bot.message_handler(func=lambda message :True)
                def spin1(mess):
                    sum,name,log=checkReg(mess)
                    id=mess.from_user.id
                    sum1=mess.text
                    try:
                        sum1=int(sum1)
                    except:
                        bot.reply_to(mess,"Это не число")
                    if int(sum1)<=int(sum):
                                oldSum=sum
                                sum=int(sum)-sum1
                                bot.reply_to(mess,"Крутим!")
                                luck=random.randint(1,6)
                                luck1=random.randint(1,6)
                                luck2=random.randint(1,6)
                                lucks="Выпало: "+str(luck)+" "+str(luck1)+" "+str(luck2)
                                bot.reply_to(mess,lucks)
                                if luck==luck1 and luck==luck2:
                                    bot.reply_to(mess,"Три одинаковые цифры, ваша ставка утраивается!")
                                    sum+=3*sum1
                                    bot.reply_to(mess,"Ваш выигрыш:"+str(sum1*3))
                                elif luck==luck1 or luck1==luck2 or luck==luck2:
                                    bot.reply_to(mess,"Две одинаковые цифры, Ваша ставка удваивается!")
                                    sum+=2*sum1
                                    bot.reply_to(mess,"Ваш выигрыш:"+str(sum1*2))
                                else:
                                    bot.reply_to(mess,"К сожалению вы проиграли.")
                                answ="Ваш балланс сейчас:"+str(sum)
                                bot.send_message(id,answ)
                                with open ('dataTelCas.txt', 'r') as a:
                                    old_data = a.read()
                                    new_data = old_data.replace(str(oldSum), str(sum))
                                with open ('dataTelCas.txt', 'w') as a:
                                    a.write(new_data)
                    else:
                        id=mess.from_user.id
                        mess="У вас недостаточно средств. Ваш балланс:"+str(sum)
                        bot.send_message(id,mess)
        @bot.message_handler(commands=['support'])
        def w(mess):
            answ="Напишите @dictatorgroup10 или @perdunwon"
            bot.reply_to(mess,answ)
        @bot.message_handler(commands=['reg'])
        def reg(mess):
            f=open('dataTelCas.txt')
            log=False
            for a in f:
                name1,passw1,sum1,id1=a.split()
                id=mess.from_user.id
                if int(id1)==int(id):
                    bot.send_message(mess.chat.id,"Вы уже зарегистрированы")
                    log=True
            if log==False:
                id=mess.from_user.id
                bot.send_message(id,"Введите свое имя")
                bot.register_next_step_handler(mess,reg1)
        def reg1(mess):
            f1=open('m.txt','w')
            id=mess.from_user.id
            name=mess.text
            bot.send_message(id,"Придумайте пароль")
            f1.write(name)
            bot.register_next_step_handler(mess,reg2)
            f1.close()
        def reg2(mess):
                        sum=0
                        f1=open('m.txt','r')
                        f=open('dataTelCas.txt','a')
                        id=mess.from_user.id
                        name=f1.read()
                        passw=mess.text
                        bot.send_message(id,"Вы зарегистрированы!\nВы получаете подарок за регистрацию в размере от 100 до 200!")
                        sum2=random.randint(100,200)
                        bot.send_message(id,f"Ваш подарок:{str(sum2)}!")
                        sum+=sum2
                        print(name,passw,str(sum),str(id),file=f)
                        f.close()
                        f1.close()
        @bot.message_handler(commands=['aut'])
        def aut(mess):
            with open('dataTelCas.txt') as f:
                log=False
                for a in f:
                    name1,passw1,sum1,id1=a.split()
                    id=mess.from_user.id
                    if int(id1)==int(id):
                        bot.send_message(mess.chat.id,"Вы уже автоизованы")
                        log=True
            if log==False:
                id=mess.from_user.id
                bot.send_message(id,"Введите свое имя")
                bot.register_next_step_handler(mess,aut1)
        def aut1(mess):
            f1=open('m.txt','w')
            log=False
            id=mess.from_user.id
            name=mess.text
            bot.send_message(id,"Введите пароль")
            f1.write(name)
            bot.register_next_step_handler(mess,aut2)
            f1.close()
        def aut2(mess):
            passw=mess.text
            id=mess.from_user.id
            with open('m.txt') as f:
                with open('dataTelCas.txt') as f1:     
                    name=f.read()
                    for data in f1:
                        name1,passw1,sum1,id1=data.split()
                        if name1==name and passw1==passw:
                            bot.send_message(id,"Вы успешно вошли в свой аккаунт.")
                            log=True
            with open ('dataTelCas.txt', 'r') as a:
                old_data = a.read()
                new_data = old_data.replace(str(id1),str(id))
            with open ('dataTelCas.txt', 'w') as a:
                a.write(new_data)
            if log==False:
                bot.send_message(id,"Неправильное имя пользователя или пароль.")
        @bot.message_handler(commands=["dep"])
        def dep(mess):
            id=mess.from_user.id
            sum,name,log=checkReg(mess)
            if log:
                clava=types.InlineKeyboardMarkup()
                crypt=types.InlineKeyboardButton("Криптовалюта",callback_data="crypt")
                rubles=types.InlineKeyboardButton("Рубли",callback_data="rub")
                clava.add(crypt,rubles)
                bot.send_message(id,"Выберите способ пополнения",reply_markup=clava)
                @bot.callback_query_handler(func=lambda call:True)
                def opl(des):
                    if des.data=="crypt":
                        print("crypt")
                        bot.send_message(des.from_user.id,"Выберите валюту(сеть-TON)\n1-TON\n2-USDT")
                        bot.register_next_step_handler(des.message,oplCr)
                    elif des.data=="rub":
                        with open('fDeps.txt','a+t') as fDep:
                            sum1,name1,log1=checkReg(des.message)
                            print("rub")
                            bot.reply_to(des.message.chat.id,"Введите сумму, на которую хотите пополнить баланс")
                            bot.register_next_step_handler(des.message,rub)
                            def rub(mess):
                                sum=int(mess.text)
                                bot.send_message(mess.from_user.id,f"https://vtb.paymo.ru/collect-money/qr/?transaction=1b01d439-c410-421d-a74c-9b8cf4067fff\nСовершите перевод на сумму{sum/2}\nВ сообщении получателю укажите имя в боте, иначе средства не поступят")
                                fDep.write(name+" "+str(sum)+" "+str(sum/2)+"RUB"+"\n")
                def oplCr(mess):
                    id=mess.from_user.id
                    if mess.text==str(1):
                        bot.send_message(id,"Введите сумму, на которую хотите пополнить(1 TON=480):")
                        bot.register_next_step_handler(mess,ton1)
                    else:
                        bot.send_message(id,"Введите сумму, на которую хотите пополнить(1 USDT=180):")
                        bot.register_next_step_handler(mess,usdt1)
                def ton1(mess):
                            with open('fDeps.txt','a+t') as fDep:
                                sum1,name,log=checkReg(mess)
                                id=mess.from_user.id
                                sum=int(mess.text)
                                bot.send_message(id,f"UQCxvHZCH6PFCfUF5wQ0CP45eH0qYt9r7MdVqRtmzSdYjmw8\nВы должны перевести {sum/480} TON на указанный адрес\nВ комментарии укажите свое имя\nПосле этого отправьте @dictatorgroup10 скриншот перевода и свое имя в боте")
                                fDep.write(name+" "+str(sum)+" "+str(sum/480)+" "+"TON")
                def usdt1(mess):
                            with open('fDeps.txt','a+t') as fDep:
                                sum1,name,log=checkReg(mess)
                                id=mess.from_user.id
                                sum=int(mess.text)
                                bot.send_message(id,f"UQCxvHZCH6PFCfUF5wQ0CP45eH0qYt9r7MdVqRtmzSdYjmw8\nВы должны перевести {sum/180} USDT на указанный адрес\В комментарии укажите свое имя\nПосле этого отправьте @dictatorgroup10 скриншот перевода и свое имя в боте")
                                fDep.write(name+" "+str(sum)+" "+str(sum/180)+" "+"USDT"+"\n")
    except:
        time.sleep(10)
        print("Ошибка")
        with open('errs.txt','a+') as ff:
            ff.write("Ошибка "+time.asctime())
    bot.polling(none_stop=True,interval=0)