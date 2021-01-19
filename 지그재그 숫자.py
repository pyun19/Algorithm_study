

T = int(input())
for i in range(1, T+1):
    n = int(input())
    result = 0
    for j in range(n):
        j+=1
        if j%2 == 0:
            result -= j
            continue
        result += j
    print('#%d'%i, result)

# T = int(input())
# for i in range(1, T+1):
#     n = int(input())
#     result = []
#     for j in range(n+1):
#         result.append(j)
#     a =sum(result[1::2])
#     b =sum(result[0::2])
#     print('#%d'%i, a-b)
