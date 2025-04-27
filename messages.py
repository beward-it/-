t=[]
with open('tickets.txt') as f:
    for a in f:
        for a1 in a.split():
            t.append(int(a1))
print(*t)