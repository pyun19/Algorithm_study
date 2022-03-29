import sys
input = int(sys.stdin.readline())

han_num = 0
for i in range(1, input+1):
    if i < 100:
        han_num += 1
    elif int(str(i)[0])-int(str(i)[1]) == int(str(i)[1])-int(str(i)[2]):
        han_num += 1
print(han_num)
