


T=int(input())
for i in range(1,T+1):
    n,x = input().strip(),[] #공백이 있을 수 있음으로 strip 꼭 쓰자
    idx = int(n.count('')//2)
    for j in n:
        x.append(int(j))
    if sum(x[:idx])==sum(x[idx:]):
        print('#%d'%i,'LUCKY')
    else:
        print('#%d'%i,'READY')




# T=int(input())
# for i in range(1,T+1):
#     n = input()
#     idx = int(n.count('')//2)
#     a,b,x = 0,0,0
#     for j in n:
#         x += 1
#         if x <= idx:
#             a += int(j)
#         else:
#             b += int(j)
#     if a == b:
#         print('#%d'%i,'LUCKY')
#     else:
#         print('#%d'%i,'READY')
