import sys

input = int(sys.stdin.readline())
n, cnt = 666, 1

while input != cnt:
    n += 1
    if '666' in str(n):
        cnt += 1
print(n)
