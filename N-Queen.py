# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0


# def dfs(queen, n, i):
#     count = 0
#     if n == i:
#         return 1
#     # 가로로 한번만 진행
#     for col in range(n):
#         queen[i] = col
#         print(queen)
#         # for-else구문
#         for x in range(i):
#             # 세로로 겹치면 안됨
#             if queen[x] == queen[i]:
#                 break
#             # 대각선으로 겹치면 안됨
#             if abs(queen[x]-queen[i]) == (i-x):
#                 break
#         else:
#             count += dfs(queen, n, i+1)
#         # print(queen)
#     return count
#
#
# def solution(n):
#     queen = [0]*n
#
#     return dfs(queen, n, 0)
#
#
# print(solution(int(input())))

# 1 0 0 0 0 0 0 0
# 0 0 1 0 0 0 0 0
# 0 0 0 0 0 1 0 0
# 0 0 0 0 0 0 0 1
# 0 1 0 0 0 0 0 0
# 0 0 0 1 0 0 0 0
# 0 0 0 0 0 1 0 0
# 0 0 0 0 0 0 0 1

# 0 1 0 0 0 0 0 0
# 0 0 0 1 0 0 0 0
# 0 0 0 0 0 1 0 0
# 0 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0
# 0 0 1 0 0 0 0 0
# 0 0 0 0 1 0 0 0
# 0 0 0 0 0 0 1 0

# import sys
#
# n = int(sys.stdin.readline())
# queen = [[0 for x in range(n)] for x in range(n)]
#
# # j = 0
# for i in range(n):
#     for j in range(n):
#         queen[i][j] = 1
#         if queen[i][j] == queen[i][j]:
#             continue
#
#     print(*queen, sep='\n')


def check(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[i]-col[x]) == x-i:
            return False
    return True


def dfs(x):
    global res
    if x == n:
        res += 1
        return
    for i in range(n):
        col[x] = i
        # print(col)
        if check(x):
            dfs(x+1)


n, res = int(input()), 0
col = [0]*n
dfs(0)

print(res)
