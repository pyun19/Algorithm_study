sum = 0
T = int(input())
for i in range(1, T + 1):
    a = input().split(' ')
    for j in range(len(a)):
        if int(a[j]) %2 == 1:
            sum += int(a[j])
    print('#%d'%i, sum)
    sum = 0
