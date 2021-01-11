
T=int(input())
for i in range(1,T+1):
    a=input().split(' ')
    if a[0]<a[1]:
        print('#%d'%i, '<')
    elif a[0]==a[1]:
        print('#%d'%i,'=')
    elif a[0]>a[1]:
        print('#%d'%i,'>')
