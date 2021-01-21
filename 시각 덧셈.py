
T = int(input())
for i in range(1, T+1):
    a1,b1,a2,b2 = map(int, input().split())
    res_h = a1+a2
    if res_h > 12:
        res_h -= 12
    res_m = b1+b2
    if res_m > 60:
        res_h += 1
        res_m -= 60
    print('#%d'%i, res_h,res_m)
