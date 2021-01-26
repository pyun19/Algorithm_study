import datetime

T = int(input())
for i in range(1, T+1):
    a,b,c,d = map(int,input().split(' '))

    t1 = datetime.date(2021, a, b)
    t2 = datetime.date(2021, c, d)

    print('#%d'%i,(t2-t1).days+1)
