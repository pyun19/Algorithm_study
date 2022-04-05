import sys

n = int(sys.stdin.readline())
# 내림차순 sort
rope = sorted([int(sys.stdin.readline()) for x in range(n)], reverse=True)
# 큰수부터 로프 수 만큼 곱하면서 최대 무게를 sort하여 구한다.
# ex) [15, 10, 5] --> [15, 20, 15] --> [20, 15, 15]
max_w = sorted([rope[i]*(i+1) for i in range(n)], reverse=True)[0]
print(max_w)
