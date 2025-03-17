import telebot
import random
import time
from datetime import date
promo=[]
price=[]
but=[]
nums=[]
from telebot import types
i=0
while i!=40:
                i+=1
                but.append(types.InlineKeyboardButton(str(i),callback_data=str(i)))
                nums.append(str(i))
with open('promo.txt') as f:
    for a in f:
        promo1,price1=a.split()
        promo.append(promo1)
        price.append(int(price1))
name=None
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
bot=telebot.TeleBot('6642421516:AAGYb7sg9cRq7_0lOQSir53QnL0xVGdCQ9U')
while True:
    try:
        @bot.message_handler(commands=['start'])
        def firstText(mess):
            bot.reply_to(mess,"Приветствуем вас в нашем боте! Извините пока не все функции бота работают.")
        @bot.message_handler(commands=['usdat'])
        def q(mess):
            sum,name,log,isP=checkReg(mess)
            if log:
                answ="Ваше имя:"+str(name)+" Ваш балланс:"+str(sum)
                if isP=="yes":
                    answ+=" Вы премиум пользователь"
                bot.reply_to(mess,answ)
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
                            if sum1<=sum:
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
                name1,passw1,sum1,id1,isP=a.split()
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
                    name1,passw1,sum1,id1,isP=a.split()
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
                        name1,passw1,sum1,id1,isP=data.split()
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
                bot.send_message(mess.from_user.id,"С премиум подпиской вы получаете больше шансов при спинах и возможность выводить средства \nСейчас она со скидкой 50% и стоит 2000\nЖелаете приобрести?",reply_markup=clava)
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
                            if sum1>=2000:
                                sum1=sum1-2000
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
            bot.send_message(id,"Спин-классическая рулетка(ставите ставку, если числа совпадут то выигрываете)\nАвто спин-то же самое что и спин, но с выбором количества вращений\nИра 50 на 50-вы выбираете один или два, система тоже если ваши решения совпадут, то ваша ставка умножается на 1,5\nИгра с выбором числа-вы выбираете число от 1 до 40 система выбирает 4 числа, если хотя бы одно из выбранных системой чисел совпадет с вашим, то ваша ставка умножается на 4")
        @bot.message_handler(commands=['num'])
        def numG(mess):
            sum,name,log,isP=checkReg(mess)
            if log:
                bot.send_message(mess.chat.id,"Введите ставку")
                bot.register_next_step_handler(mess,num1)
        def num1(mess):
             sum1=int(mess.text)
             clava=types.InlineKeyboardMarkup()
             for b in but:
                  clava.add(b)
             bot.send_message(mess.from_user.id,"Выберите число",reply_markup=clava)
             lucks(mess,sum1)
        @bot.callback_query_handler(func=lambda call: call.data in nums)#=0$
        def lucks(call,sum2):
            num=int(call)
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
                        id=id1
            luck=random.randint(1,40)
            sum1=sum-sum2
            if num==luck:
                    bot.send_message(call.message.chat.id,"Вы выиграли! Ваша ставка учетверяется!")
                    newSum=sum1+sum2*4
                    with open ('dataTelCas.txt', 'r') as a:
                        old_data = a.read()
                        new_data = old_data.replace(name1+" "+passw1+" "+str(sum)+" "+str(call.message.chat.id)+" "+isP+" "+str(dat1),name1+" "+passw1+" "+str(newSum)+" "+str(id)+" "+isP+" "+str(dat1))
                    with open ('dataTelCas.txt', 'w') as a:
                        a.write(new_data)
            else:
                 bot.send_message(id,"К сожалению вы проиграли")
    except Exception as e:
        time.sleep(10)
        print("Error")
        with open('errs.txt','a+') as ff:
           ff.write("Error "+time.asctime()+str(e))
    bot.polling(none_stop=True,interval=0)