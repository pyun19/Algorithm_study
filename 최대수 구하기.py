T = int(input())
for i in range(1, T + 1):
    a = input().split(' ')
    tmp = 0
    for j in range(len(a)):
        if int(a[j]) > tmp:
            tmp = int(a[j])
    print('#%d'%i, tmp)
