import sys

input = sys.stdin.readline
n = int(input())
num = [9-x for x in range(10)]
alp = sorted([input().rstrip() for x in range(n)], reverse=True, key=len)
dict = {}

for i in alp:
  idx = len(i) - 1
  for j in i:
    if j in dict:
      dict[j] += pow(10, idx)
    else:
      dict[j] = pow(10, idx)
    idx -= 1

dict = sorted(dict.values(), reverse=True)
result = sum([dict[x] * num[x] for x in range(len(dict))])

print(result)
