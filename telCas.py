import telebot
import random
import time
from datetime import date
promo=[]
price=[]
but=[]
nums=[]
spisok=[]
nado=[]
for i in range(40):
     nado.append("tick "+str(i))
i=0
while i!=1000:
     spisok.append("nam "+str(i))
     i+=1
from telebot import types
with open('promo.txt') as f:
    for a in f:
        promo1,price1=a.split()
        promo.append(promo1)
        price.append(int(price1))
name=None
def data(mess):
    with open('dataTelCas.txt') as f:
        for a in f :
                            name,passw,sum1,id1,isP1,dat=a.split()
                            if int(mess.from_user.id)==int(id1):
                                return name,passw,sum1,id1,isP1,dat
def checkReg(mess):
    log=False
    f=open('dataTelCas.txt')
    for a in f :
        name1,passw1,sum1,id1,isP,dat=a.split()
        if int(mess.from_user.id)==int(id1):
            log=True
            return sum1,name1,log,isP
    if log==False:
        bot.send_message(mess.chat.id,"Сначала зарегистрируйтесь. Нажмите /reg")
        f.close()
        return 0,"None",log,"no"
bot=telebot.TeleBot('6642421516:AAGXqsEfdQLhQz09duztg9RR1Gt1yZS6ezk')
while True:
    #try:
        @bot.message_handler(commands=['start'])
        def firstText(mess):
            bot.reply_to(mess,"Приветствуем вас в нашем боте! Извините пока не все функции бота работают.")
        @bot.message_handler(commands=['usdat'])
        def q(mess):
            log=False
            f=open('dataTelCas.txt')
            for a in f :
                name1,passw1,sum1,id1,isP1,dat=a.split()
                if int(mess.from_user.id)==int(id1):
                    log=True
                    name=name1
                    sum=sum1
                    passw=passw1
                    isP=isP1
            if log:
                answ="Ваше имя:"+str(name)+" Ваш балланс:"+str(sum)+" Ваш пароль: ||"+passw+"||"
                if isP=="yes":
                    answ+=" Вы премиум пользователь"
                bot.send_message(mess.chat.id,answ,parse_mode="MarkdownV2")
        @bot.message_handler(commands=['spin'])
        def spin(messg):
            sum,name,log,isP=checkReg(messg)
            if log:
                n=7
                mess=""
                if isP=="yes":
                    mess=" (шансы повышены так как у вас есть премиум)"
                    n=5
                bot.send_message(messg.from_user.id,"Введите сколько вы хотите поставить"+mess)
                @bot.message_handler(func=lambda message :True)
                def spin1(mess):
                    sum,name,log,isP=checkReg(mess)
                    id=mess.from_user.id
                    sum1=mess.text
                    try:
                        if int(sum1)<=int(sum):
                                sum1=int(sum1)
                                oldSum=sum
                                sum=int(sum)-sum1
                                bot.reply_to(mess,"Крутим!")
                                luck=random.randint(1,n)
                                luck1=random.randint(1,n)
                                luck2=random.randint(1,n)
                                lucks="Выпало: "+str(luck)+" "+str(luck1)+" "+str(luck2)
                                bot.reply_to(mess,lucks)
                                if luck==luck1 and luck==luck2:
                                    bot.reply_to(mess,"Три одинаковые цифры, ваша ставка утраивается!")
                                    sum+=2*sum1
                                    bot.reply_to(mess,"Ваш выигрыш:"+str(sum1*3))
                                elif luck==luck1 or luck1==luck2 or luck==luck2:
                                    bot.reply_to(mess,"Две одинаковые цифры, Ваша ставка удваивается!")
                                    sum+=sum1
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
                    except:
                        bot.reply_to(mess,"Это не число")
        @bot.message_handler(commands=['support'])
        def w(mess):
            answ="Напишите @dictatorgroup10 или @perdunwon"
            bot.reply_to(mess,answ)
        @bot.message_handler(commands=['reg'])
        def reg(mess):
            log=False
            f=open('dataTelCas.txt')
            for a in f:
                name1,passw1,sum1,id1,isP,dat=a.split()
                id=mess.from_user.id
                if int(id1)==int(id):
                    bot.send_message(mess.chat.id,"Вы уже зарегистрированы")
                    log=True
            if log==False:
                id=mess.from_user.id
                bot.send_message(id,"Введите свое имя")
                bot.register_next_step_handler(mess,reg1)
        def reg1(mess):
            id=mess.from_user.id
            name=mess.text
            bot.send_message(id,"Придумайте пароль")
            bot.register_next_step_handler(mess,reg2,name)
            with open('TicketsOnUser.txt','+a') as f:
                 print(name,file=f)
        def reg2(mess,name):
                        sum=0
                        f=open('dataTelCas.txt','a')
                        id=mess.from_user.id
                        passw=mess.text
                        bot.send_message(id,"Вы зарегистрированы!\nВы получаете подарок за регистрацию в размере от 100 до 200!")
                        sum2=random.randint(100,200)
                        bot.send_message(id,f"Ваш подарок:{str(sum2)}!")
                        sum+=sum2
                        print(name,passw,str(sum),str(id),"no",date.today(),file=f)
                        f.close()
        @bot.message_handler(commands=['aut'])
        def aut(mess):
            with open('dataTelCas.txt') as f:
                log=False
                for a in f:
                    name1,passw1,sum1,id1,isP,dat=a.split()
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
                    log=False
                    for data in f1:
                        name1,passw1,sum1,id1,isP,dat=data.split()
                        if name1==name and passw1==passw:
                            bot.send_message(id,"Вы успешно вошли в свой аккаунт.")
                            log=True
                            name=name1
                            passw=passw1
                            sum=sum1
                            id2=id1
                            break
            with open ('dataTelCas.txt', 'r') as a:
                old_data = a.read()
                new_data = old_data.replace(name+" "+passw+" "+sum+" "+str(id2),name+" "+passw+" "+sum+" "+str(id))
            with open ('dataTelCas.txt', 'w') as a:
                a.write(new_data)
            if log==False:
                bot.send_message(id,"Неправильное имя пользователя или пароль.")
        @bot.message_handler(commands=["dep"])
        def dep(mess):
            id=mess.from_user.id
            sum,name,log,isP=checkReg(mess)
            if log:
                clava=types.InlineKeyboardMarkup()
                crypt=types.InlineKeyboardButton("Криптовалюта",callback_data="crypt")
                rubles=types.InlineKeyboardButton("Рубли",callback_data="rub")
                clava.add(crypt,rubles)
                bot.send_message(id,"Выберите способ пополнения",reply_markup=clava)
                @bot.callback_query_handler(func=lambda call:call.data in["crypt","rub"])
                def opl(des):
                    if des.data=="crypt":
                        print("crypt")
                        bot.send_message(des.from_user.id,"Выберите валюту(сеть-TON)\n1-TON\n2-USDT")
                        bot.register_next_step_handler(des.message,oplCr)
                    else:
                        print("rub")
                        bot.send_message(des.message.chat.id,"Введите сумму, на которую хотите пополнить баланс")
                        bot.register_next_step_handler(des.message,rub)
                def rub(mess):
                    with open('fDeps.txt','+a') as fDep:
                        sum1,name1,log1,isP=checkReg(mess)
                        try:
                            sum=int(mess.text)
                            bot.send_message(mess.from_user.id,f"https://vtb.paymo.ru/collect-money/qr/?transaction=1b01d439-c410-421d-a74c-9b8cf4067fff\nСовершите перевод на сумму {sum/2} рублей\nВ сообщении получателю укажите имя в боте, иначе средства не поступят")
                            fDep.write(name1+" "+str(sum)+" "+str(sum/2)+" RUB"+"\n")
                        except:
                             bot.send_message(mess.from_user.id,"Это не число")
                def oplCr(mess):
                    id=mess.from_user.id
                    if mess.text=="1":
                        bot.send_message(id,"Введите сумму, на которую хотите пополнить(1 TON=480):")
                        bot.register_next_step_handler(mess,ton1)
                    elif mess.text=="2":
                        bot.send_message(id,"Введите сумму, на которую хотите пополнить(1 USDT=180):")
                        bot.register_next_step_handler(mess,usdt1)
                    else:
                         bot.send_message(id,"Пожайлуйста вводите 1 или 2")
                def ton1(mess):
                            with open('fDeps.txt','a+t') as fDep:
                                sum1,name,log,isP=checkReg(mess)
                                id=mess.from_user.id
                                try:
                                    sum=int(mess.text)
                                    bot.send_message(id,f"UQCxvHZCH6PFCfUF5wQ0CP45eH0qYt9r7MdVqRtmzSdYjmw8\nВы должны перевести {sum/480} TON на указанный адрес\nВ комментарии укажите свое имя\nПосле этого отправьте @dictatorgroup10 скриншот перевода и свое имя в боте")
                                    fDep.write(name+" "+str(sum)+" "+str(sum/480)+" "+"TON")
                                except:
                                    bot.send_message(id,"Это не число")
                def usdt1(mess):
                            with open('fDeps.txt','a+t') as fDep:
                                sum1,name,log,isP=checkReg(mess)
                                id=mess.from_user.id
                                try:
                                    sum=int(mess.text)
                                    bot.send_message(id,f"UQCxvHZCH6PFCfUF5wQ0CP45eH0qYt9r7MdVqRtmzSdYjmw8\nВы должны перевести {sum/180} USDT на указанный адрес\В комментарии укажите свое имя\nПосле этого отправьте @dictatorgroup10 скриншот перевода и свое имя в боте")
                                    fDep.write(name+" "+str(sum)+" "+str(sum/180)+" "+"USDT"+"\n")
                                except:
                                     bot.send_message(id,"Это не число")
        @bot.message_handler(commands=['prem'])
        def prem(mess):
            sum1,name1,log,isP=checkReg(mess)
            if log:
                clava=types.InlineKeyboardMarkup()
                yes1=types.InlineKeyboardButton("Да",callback_data="Yes")
                no1=types.InlineKeyboardButton("Нет",callback_data="No")
                clava.add(yes1,no1)
                bot.send_message(mess.from_user.id,"С премиум подпиской вы получаете больше шансов при спинах и возможность выводить средства \nСейчас она стоит 4000\nЖелаете приобрести?",reply_markup=clava)
        @bot.callback_query_handler(func=lambda call:call.data in("Yes","No"))
        def knopki(des1):
                log=False
                f=open('dataTelCas.txt')
                for a in f :
                    name,passw,sum,id1,isP1,dat=a.split()
                    if int(des1.message.chat.id)==int(id1):
                        log=True
                        sum1=sum
                        name1=name
                        passw1=passw
                        isP=isP1
                        dat1=dat
                        id=id1
                        print(name,passw,sum,id1,isP1,dat)
                if log==False:
                    bot.send_message(des1.message.chat.id,"Сначала зарегистрируйтесь. Нажмите /reg")
                    f.close()
                sum1=int(sum1)
                oldSum=sum1
                if log:
                    if isP=="yes":
                        bot.send_message(des1.message.chat.id,"У вас уже есть премиум")
                    else:
                        if des1.data=="Yes":
                            if sum1>=4000:
                                sum1=sum1-4000
                                with open ('dataTelCas.txt', 'r') as a:
                                    old_data = a.read()
                                    new_data = old_data.replace(name1+" "+passw1+" "+str(oldSum)+" "+str(id)+" "+"no"+" "+dat1,name1+" "+passw1+" "+str(sum1)+" "+str(id)+" "+"no "+dat1)
                                with open ('dataTelCas.txt', 'w') as a:
                                    a.write(new_data)
                                with open ('dataTelCas.txt', 'r') as a:
                                    old_data = a.read()
                                    new_data = old_data.replace(name1+" "+passw1+" "+str(sum1)+" "+str(id)+" "+"no "+dat1,name1+" "+passw1+" "+str(sum1)+" "+str(id)+" "+ "yes "+dat1)
                                with open ('dataTelCas.txt', 'w') as a:
                                    a.write(new_data)
                                bot.send_message(des1.message.chat.id,"Поздравляем с покупкой подписки!")
                                print(name1+" "+passw1+" "+str(oldSum)+" "+str(id)+" "+"no "+dat1,name1+" "+passw1+" "+str(sum1)+" "+str(id)+" "+"no"+dat1)
                            else:
                                bot.send_message(des1.message.chat.id,"У вас недостаточно средств")
                        else:
                            bot.send_message(des1.message.chat.id,"Покупка отменена")
        @bot.message_handler(commands=['withdraw'])
        def withdraw(mess):
            id=mess.from_user.id
            sum,name,log,isP=checkReg(mess)
            if log:
                if isP=="yes":
                    clava1=types.InlineKeyboardMarkup()
                    fb=types.InlineKeyboardButton("Да",callback_data="y")
                    sb=types.InlineKeyboardButton("Нет",callback_data="n")
                    clava1.add(fb,sb)
                    bot.send_message(id,"Пока вывод доступен только в промокоды")
                    bot.send_message(id,"1-подписка PREMIER на 55 дней за 1 рубль - 500\n2-скидка 31% на первый заказ из магнита от 1500 руб - 300\n3-яндекс плюс с опцией 'покупки с пакетом от х5 клуба' на месяц-2000\n4-Виртуальная карта в магазин метро с 3000 на балансе-5000\n5-доступ к смотрим, амедиатеке, онлайн кинотеатру премьер,стaрт и viju-1500\nСкоро появятся новые промокоды!\nЖелаете что нибудь приобрести?",reply_markup=clava1)
                else:
                    bot.send_message(id,"У вас нет премиума, для покупки нажмите /prem")
        @bot.callback_query_handler(func=lambda call:call.data in ["y","n"])
        def des(call):
                if call.data=="y":
                    clava=types.InlineKeyboardMarkup()
                    fir=types.InlineKeyboardButton("1",callback_data="1")
                    sec=types.InlineKeyboardButton("2",callback_data="2")
                    th=types.InlineKeyboardButton("3",callback_data="3")
                    four=types.InlineKeyboardButton("4",callback_data="4")
                    fith=types.InlineKeyboardButton("5",callback_data="5")
                    clava.add(fir,sec,th,four,fith)
                    bot.send_message(call.message.chat.id,"Какой именно?",reply_markup=clava)
                else:
                    bot.send_message(call.message.chat.id,"Покупка отменена")
        @bot.callback_query_handler(func=lambda call: call.data in ["1","2","3","4","5"])
        def opl(call):
                promNum=int(call.data)-1
                prom=promo[promNum]
                sum2=price[promNum]
                log=False
                f=open('dataTelCas.txt')
                for a in f :
                    name,passw,sum,id1,isP1,dat=a.split()
                    if int(call.message.chat.id)==int(id1):
                        log=True
                        sum1=sum
                        name1=name
                        passw1=passw
                        isP=isP1
                        dat1=dat
                f.close()
                oldSum=sum1
                sum1=int(sum1)
                if sum1>=sum2:
                    sum1=sum1-sum2
                    with open ('dataTelCas.txt', 'r') as a:
                        old_data = a.read()
                        new_data = old_data.replace(name1+" "+passw1+" "+str(oldSum)+" "+str(call.message.chat.id)+" "+isP+" "+str(dat1),name1+" "+passw1+" "+str(sum1)+" "+str(id)+" "+isP+" "+str(dat1))
                    with open ('dataTelCas.txt', 'w') as a:
                        a.write(new_data)
                    bot.send_message(call.message.chat.id,"Успешная покупка! Ваш промокод: "+prom)
                else:
                    bot.send_message(call.message.chat.id,"У вас недотаточно средств")
        @bot.message_handler(commands=['info'])
        def info(mess):
            id=mess.from_user.id
            bot.send_message(id,"Спин-классическая рулетка(ставите ставку, если числа совпадут то выигрываете)\nАвто спин-то же самое что и спин, но с выбором количества вращений\nИра 50 на 50-вы выбираете один или два, система тоже если ваши решения совпадут, то ваша ставка умножается на 1,5\nИгра с выбором числа-вы выбираете число от 1 до 25 система выбирает 4 числа, если хотя бы одно из выбранных системой чисел совпадет с вашим, то ваша ставка умножается на 5")
        @bot.message_handler(commands=['num'])
        def numG(mess):
            sum,name,log,isP=checkReg(mess)
            text=""
            if isP=="yes":
                 text=" (Шансы повышены так как у вас есть премиум)"
            if log:
                bot.send_message(mess.chat.id,"Введите ставку"+text)
                bot.register_next_step_handler(mess,num1)
        def num1(mess):
            sum,name,log,isP=checkReg(mess)
            sum2=int(mess.text)
            if sum2<0:
                 bot.send_message(mess.chat.id,"Пожайлуйста введите число больше нуля")
                 return None
            if int(sum)>=sum2:
                clava=types.InlineKeyboardMarkup()
                i=10
                while i!=35:
                    i+=1
                    clava.add(types.InlineKeyboardButton(str(i-10),callback_data=str(i)+" "+str(sum2)))
                    nums.append(str(i)+" "+str(sum2))
                bot.send_message(mess.from_user.id,"Выберите число",reply_markup=clava)
            else:
                bot.send_message(mess.from_user.id,"У вас недостаточно средств")
        @bot.callback_query_handler(func=lambda call: call.data in nums)#=0$
        def lucks(call):
                        num,sum2=call.data.split()
                        num=int(num)-10
                        sum2=int(sum2)
                        f=open('dataTelCas.txt')
                        for a in f :
                                name,passw,sum,id1,isP1,dat=a.split()
                                if int(call.message.chat.id)==int(id1):
                                    log=True
                                    sum1=int(sum)
                                    name1=name
                                    passw1=passw
                                    isP=isP1
                                    dat1=dat
                                    id=int(id1)
                        luck=random.randint(1,25)
                        luck1=random.randint(1,25)
                        luck2=random.randint(1,25)
                        luck3=random.randint(1,25)
                        sum1=sum1-sum2
                        bot.send_message(call.message.chat.id,"Выпавшие числа: "+str(luck)+" "+str(luck1)+" "+str(luck2)+" "+str(luck3))
                        if num==luck or num==luck1 or num==luck2 or num==luck3:
                                bot.send_message(call.message.chat.id,"Вы выиграли! Ваша ставка умножается на пять!")
                                newSum=sum1+sum2*5
                                bot.send_message(call.message.chat.id,"Ваш балланс сейчас: "+str(newSum))
                                with open ('dataTelCas.txt', 'r') as a:
                                    old_data = a.read()
                                    new_data = old_data.replace(name1+" "+passw1+" "+str(sum)+" "+str(call.message.chat.id)+" "+isP+" "+str(dat1),name1+" "+passw1+" "+str(newSum)+" "+str(call.message.chat.id)+" "+isP+" "+str(dat1))
                                with open ('dataTelCas.txt', 'w') as a:
                                    a.write(new_data)
                        else:
                                newSum=sum1
                                bot.send_message(id,"К сожалению вы проиграли")
                                with open ('dataTelCas.txt', 'r') as a:
                                    old_data = a.read()
                                    new_data = old_data.replace(name1+" "+passw1+" "+str(sum)+" "+str(call.message.chat.id)+" "+isP+" "+str(dat1),name1+" "+passw1+" "+str(newSum)+" "+str(call.message.chat.id)+" "+isP+" "+str(dat1))
                                with open ('dataTelCas.txt', 'w') as a:
                                    a.write(new_data)
                                bot.send_message(call.message.chat.id,"Ваш балланс сейчас: "+str(newSum))
        @bot.message_handler(commands=['repabug'])
        def bug(mess):
            id=mess.from_user.id
            sum,name,log,isP=checkReg(mess)
            if log:
                bot.send_message(id,"Обнаружили баг? Кратко опишите его суть и при каких обстоятельствах он возник")
                bot.register_next_step_handler(mess,bug1)
        def bug1(mess):
             with open('repedbugs.txt','a+t') as f:
                  f.write(mess.text+" @"+mess.from_user.username+"\n")
                  bot.send_message(mess.chat.id,"Спасибо! Баг отправлен")
                  bot.send_message(5072448240,"Новый баг: "+str(mess.text)+" @"+mess.from_user.username)
        @bot.message_handler(commands=['five'])
        def five(mess):
            sum,name,log,isP=checkReg(mess)
            if log:
                bot.send_message(mess.chat.id,"Введите ставку")
                bot.register_next_step_handler(mess,five1)
        def five1(mess):
            sum1=int(mess.text)
            sum,name,log,isP=checkReg(mess)
            if sum1<=int(sum):
                clava=types.InlineKeyboardMarkup()
                odin=types.InlineKeyboardButton("1",callback_data="odin "+str(sum1))
                dva=types.InlineKeyboardButton("2",callback_data="dva "+str(sum1))
                clava.add(odin,dva)
                bot.send_message(mess.chat.id,"Выберите:",reply_markup=clava)
                @bot.callback_query_handler(func=lambda call: call.data in ["odin "+str(sum1),"dva "+str(sum1)])
                def five2(call):
                    with open('dataTelCas.txt') as f:
                        for a in f :
                            name,passw,sum1,id1,isP1,dat=a.split()
                            if int(call.message.chat.id)==int(id1):
                                log=True
                                sum=int(sum1)
                                name1=name
                                passw1=passw
                                isP=isP1
                                dat1=dat
                                id=int(id1)
                    des,sum2=call.data.split()
                    sum2=int(sum2)
                    if des=="odin":
                        des=1
                    else:
                         des=2
                    luck=random.randint(1,2)
                    newSum=sum-sum2
                    bot.send_message(id,"Выпавшее число-"+str(luck))
                    if des==luck:
                        newSum=newSum+sum2/2+sum2
                        bot.send_message(call.message.chat.id,"Вы выиграли! Ваша ставка умножается на 1,5!")
                        bot.send_message(id,"Ваш выигрыш: "+str(sum2/2))
                    else:
                         bot.send_message(call.message.chat.id,"К сожалению вы проиграли")
                    with open ('dataTelCas.txt', 'r') as a:
                            old_data = a.read()
                            new_data = old_data.replace(f"{name1} {passw1} {str(sum)} {str(id)} {isP} {dat1}",f"{name1} {passw1} {str(int(newSum))} {str(id)} {isP} {dat1}")
                    with open ('dataTelCas.txt', 'w') as a:
                            a.write(new_data)
                    bot.send_message(id,"Ваш балланс сейчас: "+str(newSum))
            else:
                 bot.send_message(mess.chat.id,"У вас недостаточно средств")
        @bot.message_handler(commands=['autspin'])
        def autspin(mess):
             sum,nam,isLog,isP=checkReg(mess)
             if isLog:
                bot.send_message(mess.chat.id,"Введите сумму ставки")
                bot.register_next_step_handler(mess,avt)
        def avt(mess):
            try:
                sum1=int(mess.text)
            except:
                bot.send_message(mess.chat.id,"Это не число")
            else:
                 sum,name,log,isP=checkReg(mess)
                 if int(sum)>=sum1:
                      bot.send_message(mess.chat.id,"Введите количество вращений")
                      bot.register_next_step_handler(mess,numof,sum1)
        def numof(mess,sum1):
            try:
                numofs=int(mess.text)
            except:
                bot.send_message(mess.chat.id,"Это не число")
            else:
                 bot.send_message(mess.chat.id,"Введите задежку между спинами")
                 bot.register_next_step_handler(mess,tim,sum1,numofs)
        def tim(mess,sum1,numofs):
            try:
                num=mess.text
            except:
                bot.send_message(mess.chat.id,"Это не число")
            else:
                sum,name,log,isP=checkReg(mess)
                i=0
                n=7
                if isP=="yes":
                     n=5
                id=mess.from_user.id
                while i!=numofs:
                                sum,name,log,isP=checkReg(mess)
                                i+=1
                                oldSum=sum
                                sum=int(sum)-sum1
                                luck=random.randint(1,n)
                                luck1=random.randint(1,n)
                                luck2=random.randint(1,n)
                                lucks="Выпало: "+str(luck)+" "+str(luck1)+" "+str(luck2)
                                bot.send_message(id,lucks)
                                if luck==luck1 and luck==luck2:
                                    bot.send_message(id,"Три одинаковые цифры, ваша ставка утраивается!")
                                    sum+=3*sum1
                                    bot.send_message(id,"Ваш выигрыш:"+str(sum1*2))
                                elif luck==luck1 or luck1==luck2 or luck==luck2:
                                    bot.send_message(id,"Две одинаковые цифры, Ваша ставка удваивается!")
                                    sum+=2*sum1
                                    bot.send_message(id,"Ваш выигрыш:"+str(sum1))
                                else:
                                    bot.send_message(id,"К сожалению вы проиграли.")
                                answ="Ваш балланс сейчас:"+str(sum)
                                bot.send_message(id,answ)
                                with open ('dataTelCas.txt', 'r') as a:
                                    old_data = a.read()
                                    new_data = old_data.replace(str(oldSum), str(sum))
                                with open ('dataTelCas.txt', 'w') as a:
                                    a.write(new_data)
                                if int(sum)<int(sum1):
                                     bot.send_message(mess.chat.id,"У вас закончились средства")
                                     i=numofs
                                     break
                                time.sleep(int(num))
        @bot.message_handler(commands=['adminp'])
        def admin_panel(mess):
            bot.send_message(mess.from_user.id,"скорo")
        @bot.message_handler(commands=['lottery'])
        def lottery(mess):
            i=0
            ii=0
            with open('TicketsOnUser.txt')as f:
                 for a in f:
                      if len(a.split())==1:
                           ii+=1
                      i+=1
            with open('tickets.txt') as f:
                if f.read()=="" and ii==i:
                    i1=0
                    with open('tickets.txt','+a') as f:
                        i1+=1
                        f.write(str(i)+" ")
                    with open('winsWithTickets.txt','w') as f:
                        f.write("")
                    with open('prize.txt','w') as f:
                         f.write("")
                    bot.send_message(mess.chat.id,"Отпрвьте команду /lottery ещё раз")
                elif f.read()=="":
                    with open('winsWithTickets.txt') as f:
                         if f.read=="":
                              import lottery
                    sum,name,log,isp=checkReg(mess)
                    if log:
                        with open ('prize.txt') as f:
                            if name in f.read():
                                bot.send_message(mess.chat.id,"Вы уже забрали призы")
                                return
                        with open ('winsWithTickets.txt') as f:
                            ii=0
                            th=[]
                            pit=[]
                            dv=[]
                            sto=[]
                            tic=[]
                            prom=[]
                            trP=["Получите 300 рублей при оформлении сим карты т-банк\nZVONI","Магнит Маркет – Скидка 700₽ от 3500₽ ДЛЯ ВСЕХ!\nSSG7917","700 бонусов делимобиль\ng6mr25b4576","Яндекс книги бесплатно на месяц\n5R8W6W6PJL","Яндекс Плюс — 30 дней бесплатно при оформление карты Пэй!\n2EWU2BNL2A"]
                            for i in f:
                                if ii==0:
                                    prem=int(i)
                                else:
                                    for a in i.split():
                                        if ii==1:
                                            th.append(a)
                                        elif ii==2:
                                            pit.append(a)
                                        elif ii==3:
                                            dv.append(a)
                                        elif ii==4:
                                            sto.append(a)
                                        else:
                                            prom.append(a)
                                ii+=1
                            print(prem,"\n",*th,"\n",*pit,"\n",*dv,"\n",*sto,"\n",*prom)
                            sto1=""
                            th1=""
                            pit1=""
                            dv1=""
                            prom1=""
                            nWin=""
                            trp1=""
                            prem1=""
                            with open('TicketsOnUser.txt', 'r') as f:
                                user_tickets = {}
                                for line in f:
                                    parts = line.strip().split()
                                    if parts:
                                        user = parts[0]
                                        user_tickets[user] = parts[1:]
                            user_tickets_str = ", ".join(user_tickets.get(name, [])) if name in user_tickets else "у вас нет билетов"
                            for i in user_tickets_str.split(","):
                                    tic.append(int(i))
                            if len(tic)==1:
                                bot.send_message(mess.chat.id,"У вас нет билетов")
                                return
                            win=0
                            nP="no"
                            for aa in tic:
                                aa=str(aa)
                                if aa in sto:
                                    sto1+=aa+" "
                                    win+=100
                                elif aa in th:
                                    th1+=aa+" "
                                    win+=1000
                                elif aa in pit:
                                    pit1+=aa+" "
                                    win+=500
                                elif aa in dv:
                                    dv1+=aa+" "
                                    win+=250
                                elif aa in prom:
                                    prom1+=aa+" "
                                    trp1+=random.choice(tuple(set(*trP) - set(trp1.split)))+" "
                                elif aa==prem:
                                    prem1=aa
                                    if isp=="yes":
                                        win+=2000
                                    else:
                                        nP="yes"
                                else:
                                    nWin+=aa+" "
                            clava=types.InlineKeyboardMarkup()
                            clava.add(types.InlineKeyboardButton("Забрать денежные призы",callback_data="zabrat_"+nP+"_"+str(win)))
                            bot.send_message(mess.chat.id,f"Билеты, выигравшие 100: "+sto1+"\nБилеты, выигравшие 250: "+dv1+"\nБилеты, выигравшие 500: "+pit1+"\nБилеты, выигравшие 1000: "+th1+"\nБилеты, выигравшие промокоды: "+prom1+"\nБилеты, выигравшие премиум: "+aa+"\nОбщий выигрыш в монетах: "+str(win),reply_markup=clava)
                            bot.send_message(mess.chat.id,"Ваши промокоды: "+trp1)
                else:
                    sum, name, log, isP = checkReg(mess)
                    if not log:
                        return

                    try:
                        with open('tickets.txt', 'r') as f:
                            tickets = [int(num) for line in f for num in line.split() if num.isdigit()]
                        
                        with open('TicketsOnUser.txt', 'r') as f:
                            user_tickets = {}
                            for line in f:
                                parts = line.strip().split()
                                if parts:
                                    user = parts[0]
                                    user_tickets[user] = parts[1:]
                        
                        markup = types.InlineKeyboardMarkup()
                        for ticket in sorted(tickets):
                            btn = types.InlineKeyboardButton(str(ticket), callback_data=f"tick_{ticket}")
                            markup.add(btn)

                        user_tickets_str = ", ".join(user_tickets.get(name, [])) if name in user_tickets else "нет"

                        msg = (
                            "🎟 Розыгрыш призов 🎟\n"
                            "Призы:\n"
                            "• Премиум подписка\n"
                            "• 1000 монет\n"
                            "• 500 монет\n"
                            "• 250 монет\n"
                            "• 100 монет\n"
                            "• Различные промокоды\n\n"
                            f"Цена билета: 250 монет\n"
                            f"Ваши билеты: {user_tickets_str}\n"
                            f"Доступные билеты ({len(tickets)}):"
                        )
                        
                        bot.send_message(mess.from_user.id, msg, reply_markup=markup)

                    except Exception as e:
                        bot.send_message(mess.from_user.id, "Произошла ошибка при загрузке лотереи")
                        print(f"Lottery error: {e}")
        @bot.callback_query_handler(func=lambda call: call.data.startswith('tick_'))
        def buy_ticket(call):
            try:
                _, ticket_num = call.data.split('_')
                ticket_num = int(ticket_num)
                
                # Получаем данные пользователя
                with open('dataTelCas.txt', 'r') as f:
                    user_data = None
                    for line in f:
                        parts = line.strip().split()
                        if len(parts) >= 6 and int(parts[3]) == call.message.chat.id:
                            user_data = {
                                'name': parts[0],
                                'passw': parts[1],
                                'balance': int(parts[2]),
                                'isP': parts[4]
                            }
                            break
                    
                    if not user_data:
                        bot.answer_callback_query(call.id, "Ошибка: пользователь не найден")
                        return

                # Проверяем баланс
                if user_data['balance'] < 250:
                    bot.answer_callback_query(call.id, "Недостаточно средств!")
                    return

                # Обновляем список доступных билетов
                with open('tickets.txt', 'r+') as f:
                    tickets = [int(num) for line in f for num in line.split() if num.isdigit()]
                    if ticket_num not in tickets:
                        bot.answer_callback_query(call.id, "Билет уже куплен!")
                        return
                    
                    tickets.remove(ticket_num)
                    f.seek(0)
                    f.write(' '.join(map(str, sorted(tickets))))
                    f.truncate()

                # Обновляем билеты пользователя
                user_tickets = []
                updated = False
                lines = []
                with open('TicketsOnUser.txt', 'r') as f:
                    for line in f:
                        parts = line.strip().split()
                        if parts and parts[0] == user_data['name']:
                            user_tickets = parts[1:] + [str(ticket_num)]
                            line = ' '.join([parts[0]] + user_tickets) + '\n'
                            updated = True
                        lines.append(line)

                if not updated:
                    user_tickets = [str(ticket_num)]
                    lines.append(f"{user_data['name']} {ticket_num}\n")

                with open('TicketsOnUser.txt', 'w') as f:
                    f.writelines(lines)

                # Обновляем баланс
                new_balance = user_data['balance'] - 250
                with open('dataTelCas.txt', 'r') as f:
                    data = f.read()
                
                old_str = f"{user_data['name']} {user_data['passw']} {user_data['balance']} {call.message.chat.id} {user_data['isP']}"
                new_str = f"{user_data['name']} {user_data['passw']} {new_balance} {call.message.chat.id} {user_data['isP']}"
                new_data = data.replace(old_str, new_str)
                
                with open('dataTelCas.txt', 'w') as f:
                    f.write(new_data)

                # Формируем сообщение
                tickets_str = ', '.join(user_tickets) if user_tickets else 'нет'
                bot.answer_callback_query(call.id, "Билет успешно куплен!")
                bot.send_message(
                    call.message.chat.id,
                    f"🎫 Вы купили билет №{ticket_num}\n"
                    f"💰 Новый баланс: {new_balance}\n"
                    f"📋 Ваши билеты: {tickets_str}"
                )
                # Обновляем клавиатуру с билетами
                with open('tickets.txt', 'r') as f:
                    tickets = [int(num) for line in f for num in line.split() if num.isdigit()]
                
                markup = types.InlineKeyboardMarkup()
                for ticket in sorted(tickets):
                    btn = types.InlineKeyboardButton(str(ticket), callback_data=f"tick_{ticket}")
                    markup.add(btn)

                bot.edit_message_reply_markup(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    reply_markup=markup
                )

            except Exception as e:
                bot.answer_callback_query(call.id, "Ошибка при покупке билета")
                print(f"Buy ticket error: {e}")
            @bot.callback_query_handler(func=lambda call: call.data.startswith("zabrat_"))
            def zabor(call):
                    trash,nP,win=call.data.split("_")
                    win=int(win)
                    with open('dataTelCas.txt') as f:
                        for a in f :
                            name1,passw1,sum1,id1,isP1,dat=a.split()
                            if int(call.message.chat.id)==int(id1):
                                log=True
                                sum=int(sum1)
                                name=name1
                                oldSum=sum
                                passw=passw1
                                isP=isP1
                                id=id1
                                dat1=dat
                                break
                    sum+=win
                    isP2=isP
                    if nP=="yes":
                        isP2="yes"
                    with open ('dataTelCas.txt', 'r') as a:
                        old_data = a.read()
                        new_data = old_data.replace(f"{name} {passw} {str(oldSum)} {str(id)} {isP} {dat}",f"{name} {passw} {str(int(sum))} {str(id)} {isP2} {dat}")
                    with open ('dataTelCas.txt', 'w') as a:
                                    a.write(new_data)
                    with open('prize.txt','+a') as f:
                            print(str(name),file=f)
                    with open('TicketsOnUser.txt','r') as f:
                        old=f.read()
                        user_tickets = {}
                        for line in f:
                                parts = line.strip().split()
                                if parts:
                                    user = parts[0]
                                    user_tickets[user] = parts[1:]
                        user_tickets_str = " ".join(user_tickets.get(name, [])) if name in user_tickets else "нет"
                        new=old.replace(user_tickets_str,"")
                    bot.send_message(call.message.chat.id,"Успешно")
                    bot.send_message(call.message.chat.id,"Ваш балланс сейчас: "+str(sum))
        @bot.message_handler(commands=['mins'])
        def stavka(mess):
             bot.send_message(mess.chat.id,"Введите ставку")
             bot.register_next_step_handler(mess,mins)
        def mins(mess):
             stavka1=mess.text
             sum,name,log,isp=checkReg(mess)
             if log!=True:
                  return
             clava=types.InlineKeyboardMarkup()
             for i in range(30):
                r=random.randint(1,3)
                if r in[1,2]:
                     isw="win"
                else:
                     isw="lose"
                clava.add(types.InlineKeyboardButton("?",None,isw+"_"+stavka1))
             clava.add(types.InlineKeyboardButton("Забрать приз",callback_data="exit_"+stavka1))
             bot.send_message(mess.chat.id,"Выбирайте(забрать выигрыш можно в любой момент)",reply_markup=clava)
             @bot.callback_query_handler(func=lambda call:call.data.startswith(("win","lose","exit")))
             def des1(call):
                    try:
                         win=win
                    except:
                         win=0
                    with open('dataTelCas.txt') as f:
                        for a in f :
                            name1,passw1,sum1,id1,isP1,dat=a.split()
                            if int(call.message.chat.id)==int(id1):
                                log=True
                                sum=int(sum1)
                                name=name1
                                oldSum=sum
                                passw=passw1
                                isP=isP1
                                id=id1
                                dat1=dat
                                break
                    luck,stavka1=call.data.split("_")
                    stavka1=int(stavka1)
                    if luck=="win":
                        sum=round(sum+stavka1/10*2)
                        win=round((win+stavka1*2/10))
                        bot.send_message(call.message.chat.id,"Вы выиграли! Ваша ставка умножается на 1,2")
                        bot.send_message(call.message.chat.id,"Ваш выигрыш:  "+str(win))
                    elif luck=="lose":
                        bot.send_message(call.message.chat.id,"Бомба! Вы проиграли")
                        sum=sum-stavka1
                        with open ('dataTelCas.txt', 'r') as a:
                            old_data = a.read()
                            new_data = old_data.replace(f"{name} {passw} {str(oldSum)} {str(id)} {isP} {dat}",f"{name} {passw} {str(int(sum))} {str(id)} {isP} {dat}")
                        with open ('dataTelCas.txt', 'w') as a:
                            a.write(new_data)
                    else:
                        bot.send_message(id,"Хорошо")
                        with open ('dataTelCas.txt', 'r') as a:
                            old_data = a.read()
                            new_data = old_data.replace(f"{name} {passw} {str(oldSum)} {str(id)} {isP} {dat}",f"{name} {passw} {str(int(sum))} {str(id)} {isP} {dat}")
                        with open ('dataTelCas.txt', 'w') as a:
                            a.write(new_data)
        bot.polling(none_stop=True,interval=0)
    #except Exception as e:
    #    time.sleep(10)
    #   print(f"Error {e}")
    #   with open('errs.txt','a+') as ff:
    #      ff.write("Error "+time.asctime()+" "+str(e)+"\n")