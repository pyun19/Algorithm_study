

num = [x for x in range(1, 10001)]
no_self_num = []
for i in num:
    for j in str(i):
        i += int(j)
    no_self_num.append(i)
self_num = sorted(list(set(num) - set(no_self_num)))
print(*self_num, sep=('\n'))
