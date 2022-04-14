# import sys
#
# input = sys.stdin.readline
# n = int(input())
# dist, cost = list(map(int, input().split())), list(map(int, input().split()))
# result = 0
#
# if cost[0] != min(cost[:-1]):
#     for i in range(cost.index(min(cost[:-1]))):
#         if cost[i] > cost[i+1]:
#             result += cost[i]*dist[i]
#         else:
#             result += cost[i]*(dist[i]+dist[i+1])
#             i += 1
#     result += min(cost[:-1]) * sum(dist[cost.index(min(cost[:-1])):])
# else:
#     result = sum(dist)*cost[0]
# print(result)

#--반례--

# 5
# 2 3 1 1
# 5 2 4 1 1
# 답 : 19

# 5
# 3 2 1 4
# 5 8 9 4 1
# 46


n = int(input())
dist, cost = list(map(int, input().split())), list(map(int, input().split()))
result, _cost = cost[0]*dist[0], cost[0]

for i in range(1, len(dist)):
    if cost[i] < _cost:
        _cost = cost[i]
    result += _cost*dist[i]

print(result)
