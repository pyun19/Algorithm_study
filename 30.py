num_list = sorted([int(x) for x in input()], reverse=True)


if num_list[-1] == 0 and sum(num_list) % 3 == 0:
    print(*num_list, sep='')
else:
    print(-1)
