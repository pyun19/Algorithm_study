import sys
n = int(sys.stdin.readline())
spec = [list(map(int, sys.stdin.readline().split())) for x in range(n)]

for i in spec:
    rank = 1
    for j in spec:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")
