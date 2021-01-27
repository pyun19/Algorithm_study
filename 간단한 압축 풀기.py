
T=int(input())
for i in range(1,T+1):
    n = []
    print('#%d'%i)
    for j in range(int(input())):
        a,b = map(str,input().split(' '))
        for x in range(int(b)):
            n.append(a)
    for y in range(len(n)):
        if y>=10 and y%10 == 0:
            print(sep='\n')
        print(n[y],end='')
    print('\n')
