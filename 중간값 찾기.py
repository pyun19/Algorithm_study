sum = 0
T = int(input())
num_list = input().split(' ')
temp = []
for i in range(len(num_list)):
    if not int(num_list[i]) in temp:
        temp.append(int(num_list[i]))

result = sorted(temp)
idx = len(temp)//2+1
print(result)
print(result[idx])
