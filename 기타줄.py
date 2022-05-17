import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
set_cost = sorted([list(map(int, input().rstrip().split())) for x in range(m)], key= lambda x : x[0])
one_cost = sorted(set_cost, key= lambda x : x[1])
cnt, cost = n, 0
while cnt > 0:
    if set_cost[0][0] < one_cost[0][1] * 6:
        cost += set_cost[0][0] * (n//6)
        cnt = n % 6
        if set_cost[0][0] < one_cost[0][1] * cnt:
            cost += set_cost[0][0]
            break
    cost += one_cost[0][1] * cnt
    cnt = 0

print(cost)

# import sys; input = sys.stdin.readline
# M, N = map(int, input().split())
# for _ in range(N):
#     p, i = map(int, input().split())
#     try:
#         pac = min(pac, p)
#         ind = min(ind, i)
#     except:
#         pac = p
#         ind = i
# q, r = divmod(M, 6)
# answer = min(q * pac, q * ind * 6)
# if r: answer += min(pac, ind * r)
# print(answer)
