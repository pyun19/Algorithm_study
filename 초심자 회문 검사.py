



T = int(input())
for i in range(1, T + 1):
    a = input()
    if a[0] == a[-1]:
        b = 1
    else:
        b = 0
    print('#%d'%i, b)
