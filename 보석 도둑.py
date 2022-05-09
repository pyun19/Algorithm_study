# import sys
#
# input = sys.stdin.readline
# n, k = map(int, input().rstrip().split())
# jew = sorted([list(map(int, input().rstrip().split())) for x in range(n)], key=lambda x: (x[1],x[0]), reverse=True)
# bag = sorted([int(input().rstrip()) for x in range(k)], reverse=True)
#
# result, cnt = 0, 0
# for i in range(len(jew)):
#     if jew[i][0] < bag[cnt]:
#         result += jew[i][1]
#         cnt += 1
#         if cnt == len(bag):
#             break
# print(result)


import sys, heapq

input = sys.stdin.readline
n, k = map(int, input().rstrip().split())
jew = sorted([list(map(int, input().rstrip().split())) for x in range(n)])
bag = sorted([int(input().rstrip()) for x in range(k)])

result, temp = 0, []
for i in bag:
    while jew and i >= jew[0][0]:
        heapq.heappush(temp, -jew[0][1])
        heapq.heappop(jew)
    if temp:
        result -= heapq.heappop(temp)
    elif not jew:
        break
print(result)
