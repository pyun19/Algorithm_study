# import sys
#
# input = sys.stdin.readline
# n = input().rstrip()
# card_0, card_1 = '0', '1'
# cnt_0, cnt_1, temp = 0, 0, n[0]
#
# for i in range(1, len(n)):
#     if temp == card_0:
#         if n[i] == card_0 and i != len(n)-1:
#             continue
#         cnt_0 += 1
#         if i == len(n)-1 and n[i] == card_1:
#             cnt_1 += 1
#             break
#         temp = n[i]
#
#     else:
#         if n[i] == card_1 and i != len(n)-1:
#             continue
#         cnt_1 += 1
#         if i == len(n)-1 and n[i] == card_0:
#             cnt_0 += 1
#             break
#         temp = n[i]
#
# print(min(cnt_0, cnt_1))
import re
n=input()
n=re.sub(r'0+','0',n)
print(n)
n=re.sub(r'1+','1',n)
print(n)
one, zero = 0, 0
for c in n:
    if c=='0': zero+=1
    else: one+=1
print(min(zero,one))
