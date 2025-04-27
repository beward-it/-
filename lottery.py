trP=["T1PW4SLKN2","gb30na2xf652","GBL6553","2EWU2BNL2A"]
import random as r
prem=r.randint(1,40)
while True:
    thous=[r.randint(1,40),r.randint(1,40)]
    if thous[0] not in (thous[1],prem) and thous[1]!=prem:
        break
pitsot=[r.choice(tuple(set(range(1, 41)) - set((*thous,prem)))),r.choice(tuple(set(range(1, 41)) - set((*thous,prem)))),r.choice(tuple(set(range(1, 41)) - set((*thous,prem))))]
dvestip=[r.choice(tuple(set(range(1, 41)) - set((*thous,prem,*pitsot)))),r.choice(tuple(set(range(1, 41)) - set((*thous,prem,*pitsot)))),r.choice(tuple(set(range(1, 41)) - set((*thous,prem,*pitsot)))),r.choice(tuple(set(range(1, 41)) - set((*thous,prem,*pitsot)))),]
sto=[r.choice(tuple(set(range(1, 41)) - set((*thous,prem,*pitsot,*dvestip)))),r.choice(tuple(set(range(1, 41)) - set((*thous,prem,*pitsot,*dvestip)))),r.choice(tuple(set(range(1, 41)) - set((*thous,prem,*pitsot,*dvestip)))),r.choice(tuple(set(range(1, 41)) - set((*thous,prem,*pitsot,*dvestip)))),]
prom=[r.choice(tuple(set(range(1, 41)) - set((*thous,prem,*pitsot,*dvestip,*sto)))),r.choice(tuple(set(range(1, 41)) - set((*thous,prem,*pitsot,*dvestip,*sto)))),r.choice(tuple(set(range(1, 41)) - set((*thous,prem,*pitsot,*dvestip,*sto)))),r.choice(tuple(set(range(1, 41)) - set((*thous,prem,*pitsot,*dvestip,*sto)))),r.choice(tuple(set(range(1, 41)) - set((*thous,prem,*pitsot,*dvestip,*sto)))),]                                                                                                                                                                                                                             
with open('winsWithTickets.txt','a+') as f:
    print(prem,"\n",*pitsot,"\n",*dvestip,"\n",*sto,"\n",*prom,file=f)
