# import sys; input = sys.stdin.readline
#
# n = int(input())
# num = sorted([int(input()) for x in range(n)])
# print(num)
# # for i in range(n)

# def solution(progresses, speeds):
#     answer = []
#     _progresses = [100-x for x in progresses]
#     _speeds = speeds.copy()
#     while sum(answer) != len(progresses):
#         cnt = 0
#         for i in range(len(_progresses)):
#             if _progresses[0] <= _speeds[0]:
#                 cnt += 1
#                 del(_progresses[0])
#                 del(_speeds[0])
#             else:
#                 break
#         if cnt:
#             answer.append(cnt)
#         _speeds = [_speeds[x]+speeds[x] for x in range(len(_speeds))]
#     return answer


# import math
# def solution(n):
#     a, b = 1, 2
#     if n == 1:
#         return 1
#     for i in range(2,n):
#         a, b = b, a+b
#     return b % 1234567

import math


def solution(n, k):
    answer = []
    lst = [x+1 for x in range(n)]

    while lst:
        print(lst)
        temp = math.factorial(n-1)
        q, r = divmod(k, temp)
        print(q, r)
        if r == 0:
            q = q-1
        else:
            q
        answer.append(lst.pop(q))

        n -= 1
        k = r

    print(answer)
    return answer


solution(4, 15)
