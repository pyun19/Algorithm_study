import sys

input = sys.stdin.readline
n = int(input())
dist, cost = list(map(int, input().split())), list(map(int, input().split()))
result = 0

if cost[0] != min(cost[:-1]):
    for i in range(cost.index(min(cost[:-1]))):
        if cost[i] > cost[i+1]:
            result += cost[i]*dist[i]
        else:
            result += cost[i]*(dist[i]+dist[i+1])
            i += 1
    result += min(cost[:-1]) * sum(dist[cost.index(min(cost[:-1])):])
else:
    result = sum(dist)*cost[0]
print(result)
