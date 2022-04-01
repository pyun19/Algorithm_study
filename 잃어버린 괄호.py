import sys

input = sys.stdin.readline().split('-')
p_num, s_num = 0, 0

p_num += sum(list(map(int, input[0].split('+'))))
for i in range(1, len(input)):
    s_num += sum(list(map(int, input[i].split('+'))))
print(p_num - s_num)
