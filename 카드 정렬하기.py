

import sys, heapq

input = sys.stdin.readline

n = int(input())
card_list = []
for i in range(n):
    heapq.heappush(card_list, int(input()))
result = 0
while len(card_list) >= 2:
    temp = heapq.heappop(card_list) + heapq.heappop(card_list)
    heapq.heappush(card_list, temp)
    result += temp
print(result)
