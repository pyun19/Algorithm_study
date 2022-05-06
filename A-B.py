import sys

input = sys.stdin.readline
a, b = map(int, input().rstrip().split())
cnt = 1
while a != b:
    temp = b
    cnt += 1
    if b%2 == 0:
        b = int(b/2)
    elif b%10 == 1:
        b = b//10

    if temp == b:
        print(-1)
        break
else:
    print(cnt)
