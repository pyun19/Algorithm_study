
# n = int(input())
# num, cnt = 1, 0
# for i in range(2, n+1):
#     if num > n:
#         break
#     num += i
#     cnt += 1
# print(cnt)

s = int(input())
n = 1
while n * (n + 1) / 2 <= s:
    n += 1
print(n - 1)
