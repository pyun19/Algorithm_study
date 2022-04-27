
import sys

input = sys.stdin.readline

N = int(input())
work = [list(map(int, input().split())) for i in range(N)]

dp = [0 for i in range(N+1)]

for i in range(N-1, -1, -1):
    if i + work[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(work[i][1] + dp[i + work[i][0]], dp[i+1])

print(dp[0])
