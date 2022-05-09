import sys

input = sys.stdin.readline

l, p, v = map(int, input().rstrip().split())
i = 0
while l != 0:
    result = 0
    i += 1
    cnt = v//p
    if v%p > l:
        _p = l
    else:
        _p = v%p
    result = l*cnt + _p
    print('Case {}:'.format(i), result)
    l, p, v = map(int, input().rstrip().split())
