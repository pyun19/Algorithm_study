#
# n = int(input())
# num = sorted(list(map(int, input().split())))
# kind = list(map(int, input().split()))
# _kind = kind.copy()
# # + - * /
# # max_val, min_val = []
# # 젤 큰걸 곱하고 젤 낮은 걸 나눈다.
# # 젤 큰걸 더하고 젤 낮을 걸 뺸다.
# # 최댓값: 1 - 2 ÷ 3 + 4 + 5 × 6
# # 최솟값: 1 + 2 + 3 ÷ 4 - 5 × 6
# max_val, min_val = num[0], num[0]
#
# for j in range(1, n):
#     # print(max_val)
#     if kind[1]:
#         max_val -= num[j]
#         kind[1] -= 1
#     elif kind[3]:
#         if max_val < 0:
#             max_val = -divmod(abs(max_val), num[j])[0]
#         else:
#             max_val = max_val // num[j]
#         kind[3] -= 1
#     elif kind[0]:
#         max_val += num[j]
#         kind[0] -= 1
#     elif kind[2]:
#         max_val = max_val * num[j]
#         kind[2] -= 1
#     # min_val
#     if _kind[1]:
#         if _kind[0]:
#             min_val += num[j]
#             _kind[0] -= 1
#         elif _kind[3]:
#             if min_val < 0:
#                 min_val = -divmod(abs(min_val), num[j])[0]
#             else:
#                 min_val = min_val // num[j]
#             _kind[3] -= 1
#         elif _kind[1]:
#             min_val -= num[j]
#             _kind[1] -= 1
#         elif _kind[2]:
#             min_val = min_val * num[j]
#             _kind[2] -= 1
#     else:
#         if _kind[2]:
#             min_val = min_val * num[j]
#             _kind[2] -= 1
#         elif _kind[0]:
#             min_val += num[j]
#             _kind[0] -= 1
#         elif _kind[1]:
#             min_val -= num[j]
#             _kind[1] -= 1
#         elif _kind[3]:
#             if min_val < 0:
#                 min_val = -divmod(abs(min_val), num[j])[0]
#             else:
#                 min_val = min_val // num[j]
#
#
# print(max_val, min_val, sep='\n')


n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -1e9
min_val = 1e9


def dfs(i, visit):
    global add, sub, mul, div, max_val, min_val
    if i == n:
        max_val = max(max_val, visit)
        min_val = min(min_val, visit)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, visit + num[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, visit - num[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, visit * num[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(visit / num[i]))
            div += 1


dfs(1, num[0])

print(max_val)
print(min_val)
