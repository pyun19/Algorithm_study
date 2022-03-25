# n = int(input())
# start, end, cnt = 0, 0, 0
# for i in range(n):
#     _start, _end = map(int, input().split())
#     if _start < end:
#         continue
#     start, end = _start, _end
#     cnt += 1
# print(cnt)

import sys

# input보다 readline이 더 빠름(시간이 4000ms 넘어가는 분들은 이거 문제일듯)
n = int(sys.stdin.readline())
# 회의 시간[start, end]을 받는 2차원 리스트
# 1. end시간 오름차순 sort 2. end시간으로 정렬된 list를 start시간 오름차순 sort
t = sorted([list(map(int, sys.stdin.readline().split()))
            for x in range(n)], key=lambda x: (x[1], x[0]))
# 변수 선언 시작시간, 끝나는시간, 회의 수 count
start, end, cnt = t[0][0], t[0][1], 1
for i in range(1, n):
    _start, _end = t[i][0], t[i][1]
    # 이전 회의 end시간보다 새로운 회의 start시간이 작다면 다음 회의 검사
    if _start < end:
        continue
    start, end = _start, _end  # 조건이 충족되면 회의 count
    cnt += 1
print(cnt)
