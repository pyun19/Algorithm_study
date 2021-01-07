sum = 0
T = int(input())
for i in range(1, T + 1):
    a = input().split(' ')
    for j in range(len(a)):
        sum += int(a[j])
    result = round(sum/len(a))
    print('#%d'%i, result)
    sum = 0
