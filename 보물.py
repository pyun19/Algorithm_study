import sys

n = int(sys.stdin.readline())
list1 = sorted(list(map(int, sys.stdin.readline().split())))
list2 = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
result = 0

for i in range(n):
    result += list1[i] * list2[i]
print(result)
