
import sys

input = sys.stdin.readline
result = []
for i in range(int(input())):
    num = int(input())
    cnt = 1
    s_list_x = sorted([list(map(int, input().split())) for x in range(num)])
    x, y = min(s_list_x)
    for j in range(1, num):
        if max(x, y) < (s_list_x[j][0] and s_list_x[j][1]):
            continue
        else:
            if x < s_list_x[j][0] and y < s_list_x[j][1]:
                continue
            x, y = s_list_x[j][0], s_list_x[j][1]
            cnt += 1
    result.append(cnt)
print(*result, sep='\n')
