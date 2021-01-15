# T = int(input())
# money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
# for i in range(1, T+1):
#     a = int(input())
#     print('#%d'%i)
#     money_num = []
#     for j in range(len(money)):
#         money_num.append(a//money[j])
#         a = a%money[j]
#         print(a,end=' ')
#     print(sep='\n')




T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for i in range(1, T+1):
    a = int(input())
    print('#%d'%i)
    for j in range(len(money)):
        print(a//money[j],end=' ')
        a = a%money[j]
    print(sep='\n')
